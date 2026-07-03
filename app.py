from datetime import date, datetime
import sqlite3

from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "library-secret"
DB = "library.db"
FINE_PER_DAY = 5


def db():
    """Open SQLite database connection."""
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con


def init_db():
    """Create tables and insert starter records."""
    con = db()
    con.executescript("""
    CREATE TABLE IF NOT EXISTS users(username TEXT UNIQUE,password TEXT,role TEXT);
    CREATE TABLE IF NOT EXISTS books(id TEXT PRIMARY KEY,name TEXT,author TEXT,category TEXT,description TEXT,quantity INTEGER,image TEXT,rating REAL);
    CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,name TEXT,roll TEXT UNIQUE,department TEXT,phone TEXT,email TEXT);
    CREATE TABLE IF NOT EXISTS issued_books(id INTEGER PRIMARY KEY,book_id TEXT,student_id INTEGER,issue_date TEXT,due_date TEXT,return_date TEXT,status TEXT DEFAULT 'Issued');
    CREATE TABLE IF NOT EXISTS fines(id INTEGER PRIMARY KEY,issue_id INTEGER,late_days INTEGER,amount INTEGER,status TEXT DEFAULT 'Unpaid');
    """)
    con.execute("INSERT OR IGNORE INTO users VALUES('admin','admin123','Admin')")
    books = [
        ("B001", "Python Crash Course", "Eric Matthes", "Programming", "Friendly Python guide", 5, "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=600&q=80", 4.8),
        ("B002", "Clean Code", "Robert Martin", "Software", "Readable code principles", 3, "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=600&q=80", 4.7),
        ("B003", "Design Systems", "Alla Kholmatova", "Design", "Modern UI patterns", 4, "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=600&q=80", 4.6),
    ]
    con.executemany("INSERT OR IGNORE INTO books VALUES(?,?,?,?,?,?,?,?)", books)
    students = [
        ("Aarav", "R101", "CSE", "9876543210", "aarav@mail.com"),
        ("Priya", "R102", "ECE", "9876543211", "priya@mail.com"),
    ]
    con.executemany(
        "INSERT OR IGNORE INTO students(name,roll,department,phone,email) VALUES(?,?,?,?,?)",
        students,
    )
    con.commit()
    con.close()


def logged_in():
    """Check if user is logged in."""
    return "username" in session


def current_theme():
    """Read the selected theme from the session."""
    return session.get("theme", "dark")


def one(con, query):
    """Read one numeric value from database."""
    return con.execute(query).fetchone()[0] or 0


def chart_items(stats):
    """Build dashboard chart values for the template."""
    values = [
        ("Books", stats["total_books"]),
        ("Issued", stats["issued_books"]),
        ("Students", stats["students"]),
        ("Fine", stats["total_fine"]),
    ]
    largest = max([value for _, value in values] + [1])
    return [
        {"label": label, "value": value, "width": round((value / largest) * 100)}
        for label, value in values
    ]


@app.route("/")
def home():
    if not logged_in():
        return redirect("/login")

    search = request.args.get("search", "").strip()
    con = db()
    if search:
        books = con.execute(
            """
            SELECT * FROM books
            WHERE name LIKE ? OR author LIKE ? OR category LIKE ?
            """,
            (f"%{search}%", f"%{search}%", f"%{search}%"),
        ).fetchall()
    else:
        books = con.execute("SELECT * FROM books").fetchall()
    students = con.execute("SELECT * FROM students").fetchall()
    issued = con.execute("""
        SELECT i.*, b.name AS book_name, s.name AS student_name
        FROM issued_books i
        JOIN books b ON b.id = i.book_id
        JOIN students s ON s.id = i.student_id
        ORDER BY i.id DESC
    """).fetchall()
    fines = con.execute("""
        SELECT f.*, b.name AS book_name, s.name AS student_name
        FROM fines f
        JOIN issued_books i ON i.id = f.issue_id
        JOIN books b ON b.id = i.book_id
        JOIN students s ON s.id = i.student_id
    """).fetchall()
    stats = {
        "total_books": one(con, "SELECT COALESCE(SUM(quantity),0) FROM books"),
        "issued_books": one(con, "SELECT COUNT(*) FROM issued_books WHERE status='Issued'"),
        "students": one(con, "SELECT COUNT(*) FROM students"),
        "total_fine": one(con, "SELECT COALESCE(SUM(amount),0) FROM fines WHERE status='Unpaid'"),
        "overdue": one(con, "SELECT COUNT(*) FROM issued_books WHERE status='Issued' AND due_date < date('now')"),
    }
    stats["available_books"] = max(stats["total_books"] - stats["issued_books"], 0)
    charts = chart_items(stats)
    profile = {
        "username": session["username"],
        "role": session.get("role", "User"),
        "initial": session["username"][:1].upper(),
    }
    con.close()
    return render_template(
        "library.html",
        books=books,
        students=students,
        issued=issued,
        fines=fines,
        stats=stats,
        charts=charts,
        search=search,
        profile=profile,
        theme=current_theme(),
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        con = db()
        user = con.execute(
            "SELECT * FROM users WHERE username=? AND password=? AND role=?",
            (request.form["username"], request.form["password"], request.form["role"]),
        ).fetchone()
        con.close()
        if user:
            session["username"] = user["username"]
            session["role"] = user["role"]
            return redirect("/")
        error = "Invalid login details"
    return render_template("login.html", error=error)


@app.route("/register", methods=["GET", "POST"])
def register():
    error = ""
    success = ""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]
        confirm = request.form["confirm"]
        role = request.form["role"]

        if password != confirm:
            error = "Passwords do not match"
        elif not username:
            error = "Username is required"
        else:
            con = db()
            try:
                con.execute("INSERT INTO users VALUES(?,?,?)", (username, password, role))
                con.commit()
                success = "Account created. You can login now."
            except sqlite3.IntegrityError:
                error = "Username already exists"
            finally:
                con.close()

    return render_template("register.html", error=error, success=success)


@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    error = ""
    success = ""
    if request.method == "POST":
        username = request.form["username"].strip()
        role = request.form["role"]
        password = request.form["password"]
        confirm = request.form["confirm"]

        if password != confirm:
            error = "Passwords do not match"
        else:
            con = db()
            cur = con.execute(
                "UPDATE users SET password=? WHERE username=? AND role=?",
                (password, username, role),
            )
            con.commit()
            con.close()
            if cur.rowcount:
                success = "Password updated. You can login now."
            else:
                error = "No matching user found"

    return render_template("forgot_password.html", error=error, success=success)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/theme/<mode>")
def switch_theme(mode):
    if mode in ("dark", "light"):
        session["theme"] = mode
    return redirect(request.referrer or "/")


@app.route("/add", methods=["POST"])
def add_book():
    if not logged_in():
        return redirect("/login")
    image = request.form["image"] or "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=600&q=80"
    con = db()
    con.execute(
        "INSERT OR REPLACE INTO books VALUES(?,?,?,?,?,?,?,?)",
        (
            request.form["id"], request.form["name"], request.form["author"],
            request.form["category"], request.form["description"],
            int(request.form["quantity"]), image, 4.5,
        ),
    )
    con.commit()
    con.close()
    return redirect("/#books")


@app.route("/delete/<book_id>")
def delete_book(book_id):
    con = db()
    con.execute("DELETE FROM books WHERE id=?", (book_id,))
    con.commit()
    con.close()
    return redirect("/#books")


@app.route("/student/add", methods=["POST"])
def add_student():
    con = db()
    con.execute(
        "INSERT OR REPLACE INTO students(name,roll,department,phone,email) VALUES(?,?,?,?,?)",
        (request.form["name"], request.form["roll"], request.form["department"], request.form["phone"], request.form["email"]),
    )
    con.commit()
    con.close()
    return redirect("/#students")


@app.route("/student/delete/<int:student_id>")
def delete_student(student_id):
    con = db()
    con.execute("DELETE FROM students WHERE id=?", (student_id,))
    con.commit()
    con.close()
    return redirect("/#students")


@app.route("/issue", methods=["POST"])
def issue_book():
    con = db()
    book = con.execute("SELECT quantity FROM books WHERE id=?", (request.form["book_id"],)).fetchone()
    if book and book["quantity"] > 0:
        con.execute(
            "INSERT INTO issued_books(book_id,student_id,issue_date,due_date) VALUES(?,?,?,?)",
            (request.form["book_id"], request.form["student_id"], request.form["issue_date"], request.form["due_date"]),
        )
        con.execute("UPDATE books SET quantity=quantity-1 WHERE id=?", (request.form["book_id"],))
        con.commit()
    con.close()
    return redirect("/#issue")


@app.route("/return/<int:issue_id>")
def return_book(issue_id):
    today = date.today()
    con = db()
    item = con.execute("SELECT * FROM issued_books WHERE id=? AND status='Issued'", (issue_id,)).fetchone()
    if item:
        late = max((today - datetime.strptime(item["due_date"], "%Y-%m-%d").date()).days, 0)
        con.execute("UPDATE issued_books SET status='Returned',return_date=? WHERE id=?", (today.isoformat(), issue_id))
        con.execute("UPDATE books SET quantity=quantity+1 WHERE id=?", (item["book_id"],))
        if late:
            con.execute("INSERT INTO fines(issue_id,late_days,amount,status) VALUES(?,?,?,'Unpaid')", (issue_id, late, late * FINE_PER_DAY))
        con.commit()
    con.close()
    return redirect("/#issue")


@app.route("/fine/paid/<int:fine_id>")
def mark_fine_paid(fine_id):
    con = db()
    con.execute("UPDATE fines SET status='Paid' WHERE id=?", (fine_id,))
    con.commit()
    con.close()
    return redirect("/#fines")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
