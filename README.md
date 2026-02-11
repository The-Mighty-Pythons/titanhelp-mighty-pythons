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
<h3>Development Tools</h3>
<ul>
  <li>
    <strong>Visual Studio Community 2022</strong>
    <ul>
      <li>(Newer versions such as 2026 may work but have not been tested)</li>
      <li>Required workloads:
        <ul>
          <li>Python Development</li>
          <li>Node.js Development</li>
          <li>ASP.NET and Web Development (for web tooling, browser debugging, and HTTP tools)</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><strong>Visual Studio Code</strong> (if preferred for editing)</li>
</ul>
<h3>Required Software</h3>
<ul>
  <li>Python 3.x (latest stable version)</li>
  <li>Git</li>
  <li>Node.js (LTS)</li>
  <li>npm</li>
</ul>
<h3>Git Flow Setup</h3>
<p>
This project uses <strong>Git Flow</strong> for version control.
</p>
<ol>
  <li>Create a folder on your machine to contain the project.</li>
  <li>Open a terminal or command prompt in that folder.</li>
  <li>Initialize Git Flow:
    <pre><code>git flow init</code></pre>
  </li>
  <li>
    When prompted:
    <ul>
      <li>Set <code>main</code> as <strong>master</strong></li>
      <li>Set <code>dev</code> as <strong>development</strong></li>
      <li>Accept all other default options</li>
    </ul>
  </li>
</ol>

<h2 id="plan">Sprint Plan</h2>
<p>
(To be defined)
</p>

<h2 id="backlog">Backlog</h2>
<p>
(To be defined)
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

<h2 id="run">How to Run Locally</h2>
<p>
To be Completed
</p>

<h3>Quick Start</h3>

<h4>Windows (recommended)</h4>
<ol>
  <li>Clone the repo</li>
  <li>From <code>titanhelp-mighty-pythons/</code> run:</li>
</ol>
<pre><code>start-dev.bat</code></pre>
<p>
Frontend: <code>http://localhost:5173</code><br/>
Backend API: <code>http://127.0.0.1:5000/api/tickets</code>
Note: if you need to confirm the frontend ports
open frontend/vite-project/package.json and look for "dev": "vite --port XXXX" in the scripts section.
</p>

<h4>Mac / Linux</h4>
<ol>
  <li>Clone the repo</li>
  <li>From <code>titanhelp-mighty-pythons/</code> run:</li>
</ol>
<pre><code>chmod +x start-dev.sh
./start-dev.sh</code></pre>

