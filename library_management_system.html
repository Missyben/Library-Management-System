
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&display=swap');
  *{box-sizing:border-box;margin:0;padding:0}
  :root{--ink:#1a1a2e;--paper:#f5f0e8;--cream:#ede8dc;--shelf:#8b5e3c;--gold:#c9a84c;--green:#2d6a4f;--red:#c1121f;--blue:#1b4f72;--mono:'DM Mono',monospace;--serif:'DM Serif Display',serif}
  body{background:var(--paper);color:var(--ink)}
  #app{max-width:960px;margin:0 auto;padding:0 0 2rem}
  header{background:var(--ink);color:var(--paper);padding:1.5rem 2rem;display:flex;align-items:center;gap:1rem;border-bottom:4px solid var(--gold)}
  header h1{font-family:var(--serif);font-size:28px;letter-spacing:0.5px}
  header .subtitle{font-family:var(--mono);font-size:11px;opacity:0.6;margin-top:2px}
  .nav{background:var(--cream);border-bottom:1px solid #d0c8b8;display:flex;gap:2px;padding:0 2rem}
  .nav button{background:none;border:none;padding:10px 18px;font-family:var(--mono);font-size:12px;color:var(--ink);cursor:pointer;opacity:0.6;border-bottom:3px solid transparent;transition:all .2s}
  .nav button.active{opacity:1;border-bottom-color:var(--gold);font-weight:500}
  .nav button:hover{opacity:1}
  .panel{display:none;padding:2rem}
  .panel.active{display:block}
  .grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:1.5rem}
  .field{display:flex;flex-direction:column;gap:6px}
  .field label{font-family:var(--mono);font-size:11px;text-transform:uppercase;letter-spacing:1px;opacity:0.6}
  .field input,.field select{background:white;border:1px solid #d0c8b8;border-radius:4px;padding:8px 12px;font-family:var(--mono);font-size:13px;color:var(--ink);outline:none;transition:border-color .2s}
  .field input:focus,.field select:focus{border-color:var(--gold)}
  .btn{display:inline-flex;align-items:center;gap:6px;background:var(--ink);color:var(--paper);border:none;padding:10px 20px;font-family:var(--mono);font-size:12px;cursor:pointer;border-radius:4px;transition:background .2s;font-weight:500}
  .btn:hover{background:var(--blue)}
  .btn.danger{background:var(--red)}
  .btn.success{background:var(--green)}
  .btn.outline{background:none;border:1px solid var(--ink);color:var(--ink)}
  .btn.outline:hover{background:var(--ink);color:var(--paper)}
  .msg{padding:10px 14px;border-radius:4px;font-family:var(--mono);font-size:12px;margin-bottom:1rem;display:none}
  .msg.ok{background:#d4edda;color:#1a5c2a;border-left:3px solid var(--green);display:block}
  .msg.err{background:#fde8e8;color:#7b0f0f;border-left:3px solid var(--red);display:block}
  table{width:100%;border-collapse:collapse;font-family:var(--mono);font-size:12px}
  th{background:var(--ink);color:var(--paper);padding:10px 12px;text-align:left;font-weight:500;letter-spacing:0.5px}
  td{padding:9px 12px;border-bottom:1px solid #e5dfd4;vertical-align:middle}
  tr:hover td{background:#eee8db}
  .badge{display:inline-block;padding:3px 10px;border-radius:20px;font-size:10px;font-family:var(--mono);font-weight:500;letter-spacing:0.5px}
  .badge.available{background:#d4edda;color:#1a5c2a}
  .badge.issued{background:#fde8e8;color:#7b0f0f}
  .search-row{display:flex;gap:8px;margin-bottom:1.5rem}
  .search-row input{flex:1;background:white;border:1px solid #d0c8b8;border-radius:4px;padding:8px 12px;font-family:var(--mono);font-size:13px;color:var(--ink);outline:none}
  .search-row input:focus{border-color:var(--gold)}
  .section-title{font-family:var(--serif);font-size:20px;margin-bottom:1.2rem;padding-bottom:8px;border-bottom:2px solid var(--cream)}
  .code-block{background:#1a1a2e;color:#c9a84c;padding:1.2rem 1.5rem;border-radius:6px;font-family:var(--mono);font-size:12px;line-height:1.8;overflow-x:auto;margin-bottom:1rem}
  .code-block .kw{color:#7ec8e3}.code-block .fn{color:#98d4a3}.code-block .str{color:#f4b8a0}.code-block .cm{color:#666;font-style:italic}.code-block .cn{color:#e8b4f8}
  .stats-row{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:2rem}
  .stat-card{background:white;border:1px solid #d0c8b8;border-radius:6px;padding:1rem;text-align:center}
  .stat-card .num{font-family:var(--serif);font-size:32px;color:var(--ink)}
  .stat-card .lbl{font-family:var(--mono);font-size:10px;opacity:0.5;text-transform:uppercase;letter-spacing:1px;margin-top:4px}
  .empty{text-align:center;padding:3rem;opacity:0.4;font-family:var(--mono);font-size:13px}
  .action-btns{display:flex;gap:6px}
</style>

<div id="app">
  <header>
    <div style="font-size:32px">📚</div>
    <div>
      <h1>Library Management System</h1>
      <div class="subtitle">class Library: &nbsp;|&nbsp; Internship Project — Python + File Handling</div>
    </div>
  </header>

  <div class="nav">
    <button class="active" onclick="showPanel('dashboard')">Dashboard</button>
    <button onclick="showPanel('add')">Add Book</button>
    <button onclick="showPanel('browse')">Browse / Search</button>
    <button onclick="showPanel('issue')">Issue / Return</button>
    <button onclick="showPanel('code')">View Code</button>
  </div>

  <div id="dashboard" class="panel active">
    <div class="section-title">Library Overview</div>
    <div class="stats-row">
      <div class="stat-card"><div class="num" id="stat-total">0</div><div class="lbl">Total Books</div></div>
      <div class="stat-card"><div class="num" id="stat-avail" style="color:var(--green)">0</div><div class="lbl">Available</div></div>
      <div class="stat-card"><div class="num" id="stat-issued" style="color:var(--red)">0</div><div class="lbl">Issued Out</div></div>
    </div>
    <div class="section-title" style="font-size:15px">Recent Books</div>
    <table id="dash-table">
      <thead><tr><th>ID</th><th>Title</th><th>Author</th><th>Category</th><th>Status</th></tr></thead>
      <tbody id="dash-body"></tbody>
    </table>
  </div>

  <div id="add" class="panel">
    <div class="section-title">Add New Book</div>
    <div id="add-msg" class="msg"></div>
    <div class="grid">
      <div class="field"><label>Book ID</label><input id="in-id" placeholder="e.g. B001" /></div>
      <div class="field"><label>Book Title</label><input id="in-title" placeholder="e.g. Clean Code" /></div>
      <div class="field"><label>Author</label><input id="in-author" placeholder="e.g. Robert C. Martin" /></div>
      <div class="field"><label>Category</label>
        <select id="in-cat">
          <option value="">Select category</option>
          <option>Programming</option><option>Science</option><option>History</option>
          <option>Mathematics</option><option>Literature</option><option>Self-Help</option><option>Other</option>
        </select>
      </div>
    </div>
    <button class="btn success" onclick="addBook()"><i class="ti ti-plus"></i> Add to Library</button>
    <div style="margin-top:2rem;background:var(--cream);border-radius:6px;padding:1.2rem">
      <div style="font-family:var(--mono);font-size:11px;opacity:0.6;margin-bottom:8px;text-transform:uppercase;letter-spacing:1px">📄 books.txt — file preview</div>
      <pre id="file-preview" style="font-family:var(--mono);font-size:11px;color:var(--ink);white-space:pre-wrap;max-height:160px;overflow-y:auto;opacity:0.8">(empty)</pre>
    </div>
  </div>

  <div id="browse" class="panel">
    <div class="section-title">Browse &amp; Search Books</div>
    <div class="search-row">
      <input id="search-in" placeholder="Search by title, author, ID or category…" oninput="renderSearch()" />
      <select id="search-cat" onchange="renderSearch()" style="background:white;border:1px solid #d0c8b8;border-radius:4px;padding:8px 12px;font-family:var(--mono);font-size:12px;color:var(--ink);outline:none">
        <option value="">All categories</option>
        <option>Programming</option><option>Science</option><option>History</option>
        <option>Mathematics</option><option>Literature</option><option>Self-Help</option><option>Other</option>
      </select>
    </div>
    <table>
      <thead><tr><th>ID</th><th>Title</th><th>Author</th><th>Category</th><th>Status</th></tr></thead>
      <tbody id="browse-body"></tbody>
    </table>
  </div>

  <div id="issue" class="panel">
    <div class="section-title">Issue / Return Books</div>
    <div id="issue-msg" class="msg"></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem">
      <div>
        <div style="font-family:var(--mono);font-size:11px;text-transform:uppercase;letter-spacing:1px;opacity:0.6;margin-bottom:10px">Issue a Book</div>
        <div class="field" style="margin-bottom:10px"><label>Book ID</label><input id="issue-id" placeholder="e.g. B001" /></div>
        <button class="btn danger" onclick="issueBook()"><i class="ti ti-book-off"></i> Issue Book</button>
      </div>
      <div>
        <div style="font-family:var(--mono);font-size:11px;text-transform:uppercase;letter-spacing:1px;opacity:0.6;margin-bottom:10px">Return a Book</div>
        <div class="field" style="margin-bottom:10px"><label>Book ID</label><input id="return-id" placeholder="e.g. B001" /></div>
        <button class="btn success" onclick="returnBook()"><i class="ti ti-book"></i> Return Book</button>
      </div>
    </div>
    <div style="margin-top:2rem">
      <div class="section-title" style="font-size:15px">Currently Issued</div>
      <table><thead><tr><th>ID</th><th>Title</th><th>Author</th><th>Category</th></tr></thead>
      <tbody id="issued-body"></tbody></table>
    </div>
  </div>

  <div id="code" class="panel">
    <div class="section-title">Python Source Code</div>
    <p style="font-family:var(--mono);font-size:12px;opacity:0.6;margin-bottom:1.5rem">The full <code>library.py</code> implementation using OOP, file handling, and all required methods.</p>
    <div class="code-block"><pre id="code-display"></pre></div>
    <div style="margin-top:1rem;padding:1rem;background:var(--cream);border-radius:6px;font-family:var(--mono);font-size:11px;line-height:1.8;opacity:0.8">
      <strong>Concepts used:</strong> Class &amp; Constructor (__init__) · Instance methods · File I/O (open/read/write) · Exception handling · Loops &amp; conditionals · String formatting
    </div>
  </div>
</div>

<script>
let books = JSON.parse(localStorage.getItem('lib_books') || '[]');

const pythonCode = `<span class="cm"># library.py — Library Management System</span>
<span class="cm"># Concepts: Class, Constructor, Methods, File Handling</span>

<span class="kw">class</span> <span class="cn">Library</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self, filename=<span class="str">"books.txt"</span>):
        self.filename = filename
        self.books = []
        self.<span class="fn">load_books</span>()   <span class="cm"># Load on startup</span>

    <span class="cm"># ── File Handling ─────────────────────────</span>

    <span class="kw">def</span> <span class="fn">load_books</span>(self):
        <span class="kw">try</span>:
            <span class="kw">with</span> <span class="fn">open</span>(self.filename, <span class="str">"r"</span>) <span class="kw">as</span> f:
                <span class="kw">for</span> line <span class="kw">in</span> f:
                    parts = line.strip().<span class="fn">split</span>(<span class="str">"|"</span>)
                    <span class="kw">if</span> <span class="fn">len</span>(parts) == <span class="cn">5</span>:
                        self.books.<span class="fn">append</span>({
                            <span class="str">"id"</span>: parts[<span class="cn">0</span>],
                            <span class="str">"title"</span>: parts[<span class="cn">1</span>],
                            <span class="str">"author"</span>: parts[<span class="cn">2</span>],
                            <span class="str">"category"</span>: parts[<span class="cn">3</span>],
                            <span class="str">"available"</span>: parts[<span class="cn">4</span>] == <span class="str">"True"</span>
                        })
        <span class="kw">except</span> <span class="cn">FileNotFoundError</span>:
            <span class="fn">print</span>(<span class="str">"No existing data found."</span>)

    <span class="kw">def</span> <span class="fn">save_books</span>(self):
        <span class="kw">with</span> <span class="fn">open</span>(self.filename, <span class="str">"w"</span>) <span class="kw">as</span> f:
            <span class="kw">for</span> b <span class="kw">in</span> self.books:
                f.<span class="fn">write</span>(
                    <span class="str">f"{b['id']}|{b['title']}|{b['author']}"</span>
                    <span class="str">f"|{b['category']}|{b['available']}\n"</span>
                )

    <span class="cm"># ── Core Methods ──────────────────────────</span>

    <span class="kw">def</span> <span class="fn">add_book</span>(self, book_id, title, author, category):
        <span class="kw">for</span> b <span class="kw">in</span> self.books:
            <span class="kw">if</span> b[<span class="str">"id"</span>] == book_id:
                <span class="fn">print</span>(<span class="str">f"Book ID {book_id} already exists."</span>)
                <span class="kw">return</span>
        self.books.<span class="fn">append</span>({
            <span class="str">"id"</span>: book_id, <span class="str">"title"</span>: title,
            <span class="str">"author"</span>: author, <span class="str">"category"</span>: category,
            <span class="str">"available"</span>: <span class="cn">True</span>
        })
        self.<span class="fn">save_books</span>()
        <span class="fn">print</span>(<span class="str">f"'{title}' added successfully."</span>)

    <span class="kw">def</span> <span class="fn">view_books</span>(self):
        <span class="kw">if not</span> self.books:
            <span class="fn">print</span>(<span class="str">"Library is empty."</span>)
            <span class="kw">return</span>
        <span class="fn">print</span>(<span class="str">f"{'ID':<8}{'Title':<25}{'Author':<20}{'Cat':<12}Status"</span>)
        <span class="fn">print</span>(<span class="str">"-" * 70</span>)
        <span class="kw">for</span> b <span class="kw">in</span> self.books:
            status = <span class="str">"Available"</span> <span class="kw">if</span> b[<span class="str">"available"</span>] <span class="kw">else</span> <span class="str">"Issued"</span>
            <span class="fn">print</span>(<span class="str">f"{b['id']:<8}{b['title']:<25}{b['author']:<20}{b['category']:<12}{status}"</span>)

    <span class="kw">def</span> <span class="fn">search_book</span>(self, query):
        query = query.<span class="fn">lower</span>()
        results = [
            b <span class="kw">for</span> b <span class="kw">in</span> self.books
            <span class="kw">if</span> query <span class="kw">in</span> b[<span class="str">"title"</span>].<span class="fn">lower</span>()
            <span class="kw">or</span> query <span class="kw">in</span> b[<span class="str">"author"</span>].<span class="fn">lower</span>()
            <span class="kw">or</span> query <span class="kw">in</span> b[<span class="str">"id"</span>].<span class="fn">lower</span>()
        ]
        <span class="kw">if not</span> results:
            <span class="fn">print</span>(<span class="str">"No books found."</span>)
        <span class="kw">else</span>:
            <span class="kw">for</span> b <span class="kw">in</span> results:
                <span class="fn">print</span>(b)

    <span class="kw">def</span> <span class="fn">issue_book</span>(self, book_id):
        <span class="kw">for</span> b <span class="kw">in</span> self.books:
            <span class="kw">if</span> b[<span class="str">"id"</span>] == book_id:
                <span class="kw">if</span> b[<span class="str">"available"</span>]:
                    b[<span class="str">"available"</span>] = <span class="cn">False</span>
                    self.<span class="fn">save_books</span>()
                    <span class="fn">print</span>(<span class="str">f"'{b['title']}' issued successfully."</span>)
                <span class="kw">else</span>:
                    <span class="fn">print</span>(<span class="str">"Book is already issued."</span>)
                <span class="kw">return</span>
        <span class="fn">print</span>(<span class="str">"Book ID not found."</span>)

    <span class="kw">def</span> <span class="fn">return_book</span>(self, book_id):
        <span class="kw">for</span> b <span class="kw">in</span> self.books:
            <span class="kw">if</span> b[<span class="str">"id"</span>] == book_id:
                <span class="kw">if not</span> b[<span class="str">"available"</span>]:
                    b[<span class="str">"available"</span>] = <span class="cn">True</span>
                    self.<span class="fn">save_books</span>()
                    <span class="fn">print</span>(<span class="str">f"'{b['title']}' returned successfully."</span>)
                <span class="kw">else</span>:
                    <span class="fn">print</span>(<span class="str">"Book was not issued."</span>)
                <span class="kw">return</span>
        <span class="fn">print</span>(<span class="str">"Book ID not found."</span>)


<span class="cm"># ── Main Program ──────────────────────────</span>

lib = <span class="cn">Library</span>()

<span class="kw">while True</span>:
    <span class="fn">print</span>(<span class="str">"\n1. Add Book  2. View Books  3. Search"</span>)
    <span class="fn">print</span>(<span class="str">"4. Issue Book  5. Return Book  6. Exit"</span>)
    choice = <span class="fn">input</span>(<span class="str">"Choice: "</span>)

    <span class="kw">if</span> choice == <span class="str">"1"</span>:
        bid = <span class="fn">input</span>(<span class="str">"Book ID: "</span>)
        t   = <span class="fn">input</span>(<span class="str">"Title: "</span>)
        a   = <span class="fn">input</span>(<span class="str">"Author: "</span>)
        c   = <span class="fn">input</span>(<span class="str">"Category: "</span>)
        lib.<span class="fn">add_book</span>(bid, t, a, c)
    <span class="kw">elif</span> choice == <span class="str">"2"</span>:
        lib.<span class="fn">view_books</span>()
    <span class="kw">elif</span> choice == <span class="str">"3"</span>:
        q = <span class="fn">input</span>(<span class="str">"Search: "</span>)
        lib.<span class="fn">search_book</span>(q)
    <span class="kw">elif</span> choice == <span class="str">"4"</span>:
        bid = <span class="fn">input</span>(<span class="str">"Book ID to issue: "</span>)
        lib.<span class="fn">issue_book</span>(bid)
    <span class="kw">elif</span> choice == <span class="str">"5"</span>:
        bid = <span class="fn">input</span>(<span class="str">"Book ID to return: "</span>)
        lib.<span class="fn">return_book</span>(bid)
    <span class="kw">elif</span> choice == <span class="str">"6"</span>:
        <span class="kw">break</span>`;

function save() { localStorage.setItem('lib_books', JSON.stringify(books)); }

function fileText() {
  if (!books.length) return '(empty)';
  return books.map(b => `${b.id}|${b.title}|${b.author}|${b.category}|${b.available}`).join('\n');
}

function showPanel(id) {
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav button').forEach(b => b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  document.querySelector(`.nav button[onclick="showPanel('${id}')"]`).classList.add('active');
  if (id === 'dashboard') renderDash();
  if (id === 'browse') renderSearch();
  if (id === 'issue') renderIssued();
  if (id === 'add') { document.getElementById('file-preview').textContent = fileText(); }
  if (id === 'code') { document.getElementById('code-display').innerHTML = pythonCode; }
}

function renderDash() {
  const avail = books.filter(b => b.available).length;
  document.getElementById('stat-total').textContent = books.length;
  document.getElementById('stat-avail').textContent = avail;
  document.getElementById('stat-issued').textContent = books.length - avail;
  const tb = document.getElementById('dash-body');
  const recent = [...books].slice(-5).reverse();
  tb.innerHTML = recent.length ? recent.map(b => `<tr>
    <td style="font-family:var(--mono);font-size:11px;opacity:0.6">${b.id}</td>
    <td style="font-weight:500">${b.title}</td>
    <td style="opacity:0.7">${b.author}</td>
    <td><span class="badge" style="background:#e8f0fa;color:#1b4f72">${b.category}</span></td>
    <td><span class="badge ${b.available?'available':'issued'}">${b.available?'Available':'Issued'}</span></td>
  </tr>`).join('') : `<tr><td colspan="5" class="empty">No books yet — add some!</td></tr>`;
}

function addBook() {
  const id = document.getElementById('in-id').value.trim();
  const title = document.getElementById('in-title').value.trim();
  const author = document.getElementById('in-author').value.trim();
  const cat = document.getElementById('in-cat').value;
  const msg = document.getElementById('add-msg');
  msg.className = 'msg';
  if (!id || !title || !author || !cat) { msg.className='msg err'; msg.textContent='All fields are required.'; return; }
  if (books.find(b => b.id === id)) { msg.className='msg err'; msg.textContent=`Book ID "${id}" already exists.`; return; }
  books.push({ id, title, author, category: cat, available: true });
  save();
  msg.className='msg ok'; msg.textContent=`"${title}" added successfully to books.txt`;
  document.getElementById('in-id').value=''; document.getElementById('in-title').value='';
  document.getElementById('in-author').value=''; document.getElementById('in-cat').value='';
  document.getElementById('file-preview').textContent = fileText();
}

function renderSearch() {
  const q = document.getElementById('search-in').value.toLowerCase();
  const cat = document.getElementById('search-cat').value;
  const filtered = books.filter(b =>
    (!q || b.id.toLowerCase().includes(q) || b.title.toLowerCase().includes(q) || b.author.toLowerCase().includes(q) || b.category.toLowerCase().includes(q)) &&
    (!cat || b.category === cat)
  );
  document.getElementById('browse-body').innerHTML = filtered.length ? filtered.map(b => `<tr>
    <td style="font-family:var(--mono);font-size:11px;opacity:0.6">${b.id}</td>
    <td style="font-weight:500">${b.title}</td>
    <td style="opacity:0.7">${b.author}</td>
    <td><span class="badge" style="background:#e8f0fa;color:#1b4f72">${b.category}</span></td>
    <td><span class="badge ${b.available?'available':'issued'}">${b.available?'Available':'Issued'}</span></td>
  </tr>`).join('') : `<tr><td colspan="5" class="empty">No books match your search.</td></tr>`;
}

function issueBook() {
  const id = document.getElementById('issue-id').value.trim();
  const msg = document.getElementById('issue-msg');
  msg.className='msg';
  const b = books.find(x => x.id === id);
  if (!b) { msg.className='msg err'; msg.textContent=`Book ID "${id}" not found.`; return; }
  if (!b.available) { msg.className='msg err'; msg.textContent=`"${b.title}" is already issued.`; return; }
  b.available = false; save();
  msg.className='msg ok'; msg.textContent=`"${b.title}" issued successfully.`;
  document.getElementById('issue-id').value='';
  renderIssued();
}

function returnBook() {
  const id = document.getElementById('return-id').value.trim();
  const msg = document.getElementById('issue-msg');
  msg.className='msg';
  const b = books.find(x => x.id === id);
  if (!b) { msg.className='msg err'; msg.textContent=`Book ID "${id}" not found.`; return; }
  if (b.available) { msg.className='msg err'; msg.textContent=`"${b.title}" was not issued.`; return; }
  b.available = true; save();
  msg.className='msg ok'; msg.textContent=`"${b.title}" returned successfully.`;
  document.getElementById('return-id').value='';
  renderIssued();
}

function renderIssued() {
  const issued = books.filter(b => !b.available);
  document.getElementById('issued-body').innerHTML = issued.length ? issued.map(b => `<tr>
    <td style="font-family:var(--mono);font-size:11px;opacity:0.6">${b.id}</td>
    <td style="font-weight:500">${b.title}</td>
    <td style="opacity:0.7">${b.author}</td>
    <td><span class="badge" style="background:#e8f0fa;color:#1b4f72">${b.category}</span></td>
  </tr>`).join('') : `<tr><td colspan="4" class="empty">No books currently issued.</td></tr>`;
}

if (!books.length) {
  books = [
    {id:'B001',title:'Clean Code',author:'Robert C. Martin',category:'Programming',available:true},
    {id:'B002',title:'A Brief History of Time',author:'Stephen Hawking',category:'Science',available:false},
    {id:'B003',title:'The Pragmatic Programmer',author:'Hunt & Thomas',category:'Programming',available:true},
    {id:'B004',title:'Sapiens',author:'Yuval Noah Harari',category:'History',available:true},
  ];
  save();
}
renderDash();
</script>
