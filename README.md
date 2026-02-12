<!-- README.md -->
<div align="center">
  <h1>TitanHelp</h1>
  <p>
    <em>TitanHelp Ticketing System</em><br />
    <strong>By:</strong> Amanda Crotty, Sydney Gilchrist, Sophia Sipayboun
  </p>
</div>

<h2 id="toc">Table of Contents</h2>
<ol>
  <li><a href="#requirements">Repository Requirements</a></li>
  <li><a href="#plan">Sprint Plan</a></li>
  <li><a href="#backlog">Backlog</a></li>
  <li><a href="#data">Data Model</a></li>
  <li><a href="#run">How to Run Locally</a></li>
</ol>

<h2 id="requirements">Repository Requirements</h2>

<h3>Supported Development Environment</h3>
<ul>
  <li><strong>VS Code</strong> (standard team IDE for this repository)</li>
  <li>This repo is designed to run via <strong>VS Code</strong> and the included scripts. We do not support Visual Studio 2022 for running/debugging.</li>
</ul>

<h3>Required Software (All Platforms)</h3>
<ul>
  <li><strong>Git</strong></li>
  <li><strong>Python 3.11+</strong> (3.11 recommended)</li>
  <li><strong>Node.js (LTS)</strong> + <strong>npm</strong></li>
</ul>

<h3>Recommended VS Code Extensions</h3>
<ul>
  <li><code>ms-python.python</code> (Python)</li>
  <li><code>ms-python.vscode-pylance</code> (Pylance)</li>
  <li><code>dbaeumer.vscode-eslint</code> (ESLint)</li>
</ul>

<h3>Repository Setup Notes</h3>
<ul>
  <li>Backend dependencies are managed with <code>requirements.txt</code> and a local virtual environment (<code>.venv</code>).</li>
  <li>Frontend dependencies are managed with <code>npm</code> under <code>frontend/vite-project</code>.</li>
</ul>

<h2 id="plan">Sprint Plan</h2>

<h3>Sprint 1: Foundation (Setup + Contract + Skeleton)</h3>
<ul>
  <li><strong>Goal:</strong> The full stack runs locally for all team members and frontend/backend integrate using a documented API contract.</li>
  <li><strong>Deliverables:</strong>
    <ul>
      <li>US-F1: Repo Setup &amp; Run Instructions completed (clear setup steps; scripts provided; <code>.env.example</code> files present)</li>
      <li>US-F2: API Contract Agreement completed (documented endpoints, payloads, error formats)</li>
      <li>US-F3: Dev CORS Configuration completed (frontend can call backend without CORS errors)</li>
      <li>Backend skeleton in place (Controller → Service → Repository → ORM layering)</li>
      <li>Frontend skeleton in place (Tickets page can load and display ticket list)</li>
    </ul>
  </li>
</ul>

<h3>Sprint 2: Core Ticket Flow (Create + List)</h3>
<ul>
  <li><strong>Goal:</strong> Users can view tickets and create a new ticket from the UI using the real API.</li>
  <li><strong>Deliverables:</strong>
    <ul>
      <li>Backend: implement <code>GET /api/tickets</code> and <code>POST /api/tickets</code> using Service + Repository + SQLAlchemy</li>
      <li>Backend: validate inputs and return error JSON per contract</li>
      <li>Frontend: implement <code>TicketList</code> table + loading/error states</li>
      <li>Frontend: implement <code>TicketForm</code> with client-side validation + success/reset behavior</li>
      <li>End-to-end: create ticket in UI → appears in list</li>
    </ul>
  </li>
</ul>

<h2 id="backlog">Backlog</h2>

<p>
The active product backlog is managed in our GitHub Project Board.
All user stories, tasks, sprint assignments, and status updates are tracked there.
</p>

<p>
<strong>Project Board:</strong><br/>
<a href="https://github.com/orgs/The-Mighty-Pythons/projects/1">
The Mighty Pythons – TitanHelp Project Board
</a>
</p>


<h2 id="data">Data Model</h2>
<h3>Ticket</h3>
<ul>
  <li><strong>ID</strong> – Auto-generated</li>
  <li><strong>Name</strong> – Required, maximum 100 characters</li>
  <li><strong>Date</strong> – Auto-populated with ticket creation date</li>
  <li><strong>Problem Description</strong> – Required, maximum 1000 characters</li>
  <li><strong>Status</strong> – Default value: <em>Open</em></li>
  <li><strong>Priority</strong> – Low / Medium / High</li>
</ul>

<h3>API Contract</h3>
<p>
The frontend and backend communicate using a documented JSON contract.
See:
<a href="titanhelp-mighty-pythons/docs/api-contract.md">
TitanHelp API Contract Specification
</a>.
</p>

<h3>Architecture</h3>
<p>
The application follows a layered architecture with clear separation of concerns. Documentation of the architecture and design decisions is provided in the project link below.
See:
<a href="titanhelp-mighty-pythons/docs/architecture.md">
TitanHelp Architecture and Design Documentation
</a>.
</p>

<h2 id="run">How to Run Locally (VS Code + Scripts)</h2>

<p>
This project is designed to be run from the command line (or VS Code) using the included scripts.
We do not support running the project from Visual Studio 2022.
</p>

<h3>Prerequisites (All Platforms)</h3>
<ul>
  <li><strong>Git</strong></li>
  <li><strong>Python 3.11+</strong> (3.11 recommended)</li>
  <li><strong>Node.js (LTS)</strong> + <strong>npm</strong></li>
  <li><strong>VS Code</strong> (recommended)</li>
</ul>

<h3>Quick Start</h3>

<h4>Windows</h4>
<ol>
  <li>Clone the repo</li>
  <li>Open a terminal in the repo folder: <code>titanhelp-mighty-pythons/</code></li>
  <li>Run:</li>
</ol>
<pre><code>start-dev.bat</code></pre>

<h4>Mac / Linux</h4>
<ol>
  <li>Clone the repo</li>
  <li>Open a terminal in the repo folder: <code>titanhelp-mighty-pythons/</code></li>
  <li>Run:</li>
</ol>
<pre><code>chmod +x start-dev.sh
./start-dev.sh</code></pre>

<h3>What You Should See</h3>
<ul>
  <li><strong>Backend API</strong> running at: <code>http://127.0.0.1:5000/api/tickets</code> (should return <code>[]</code>)</li>
  <li><strong>Frontend</strong> running at the URL printed in the terminal (usually <code>http://localhost:5173</code>)</li>
</ul>

<h3>Notes / Troubleshooting</h3>
<ul>
  <li>
    <strong>Vite port may change.</strong> If <code>5173</code> is already in use, Vite will automatically pick another port (e.g., <code>5174</code>).
    Always use the exact Local URL shown in the terminal output.
  </li>
  <li>
    <strong>First run takes longer.</strong> The scripts will create the Python virtual environment and install dependencies for backend and frontend.
    Future runs should be faster.
  </li>
  <li>
    <strong>If the backend fails to start</strong>, verify you can reach <code>http://127.0.0.1:5000/api/tickets</code> in a browser.
    If it does not load, check the backend terminal for the error message.
  </li>
</ul>

<h3>Optional: Run via VS Code</h3>
<p>
If you are using VS Code, you can also run the full stack from the Run panel:
</p>
<ol>
  <li>Open folder: <code>titanhelp-mighty-pythons/</code></li>
  <li>Go to <strong>Run and Debug</strong> (if you cannot find it, check under View -> Run)</li>
  <li>Select: <code>Full Stack: Backend + Frontend</code></li>
  <li>Click the green play button</li>
</ol>
