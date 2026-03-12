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
  <li><a href="#team">Team Information</a></li>
  <li><a href="#overview">Project Overview</a></li>
  <li><a href="#requirements-analysis">Requirements Analysis</a></li>
  <li><a href="#technical">Technical Implementation</a></li>
  <li><a href="#process">Development Process</a></li>
  <li><a href="#user-docs">User Documentation</a></li>
  <li><a href="#evaluation">Project Evaluation</a></li>
  <li><a href="#repo-requirements">Repository Requirements</a></li>
  <li><a href="#plan">Sprint Plan</a></li>
  <li><a href="#backlog">Backlog</a></li>
  <li><a href="#data">Data Model</a></li>
  <li><a href="#run">How to Run Locally</a></li>
</ol>

<!-- ═══════════════════════════════════════════════════════════════ -->
<h2 id="team">Team Information</h2>

<h3>Team Name</h3>
<p>The Mighty Pythons</p>

<h3>Team Members and Layer Assignments</h3>
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Primary Layer</th>
      <th>Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Amanda Crotty</td>
      <td>Application Management / Business Logic / Unit Tests</td>
      <td>Group Leader</td>
    </tr>
    <tr>
      <td>Sydney Gilchrist</td>
      <td>Presentation (Frontend)</td>
      <td>Team Member</td>
    </tr>
    <tr>
      <td>Sophia Sipayboun</td>
      <td>Data Access</td>
      <td>Team Member</td>
    </tr>
  </tbody>
</table>

<h3>Individual GitHub Contribution Summaries</h3>

<h4>Amanda Crotty — Application / Business Logic Layer &amp; Project Lead</h4>
<ul>
  <li><strong>Primary responsibilities:</strong> API contract, domain model (B2), REST API endpoints (B7), server-side validation (B6), user feedback layer (P5), update ticket status feature (B10), DTO/field mapping (I2), backend test suite (Q1), domain layer documentation, project documentation, end-to-end verification</li>
  <li><strong>Pull requests created:</strong>
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/55">#55 I2 – API markdown</a>,
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/53">#53 B10 – update ticket status</a>,
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/52">#52 Q1 – backend test completion</a>,
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/50">#50 P5 – user feedback</a>,
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/49">#49 – validation uniform</a>,
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/40">#40 F2 – API contract</a>,
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/39">#39 – backend testing layer</a>,
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/33">#33 F1 – repo run instructions</a>,
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/1">#1 – initial README</a>
  </li>
  <li><strong>Note:</strong> As group leader, Amanda also merged several pull requests on behalf of teammates whose work is attributed below.</li>
</ul>

<h4>Sophia Sipayboun — Data Access Layer</h4>
<ul>
  <li><strong>Primary responsibilities:</strong> Flask app factory and configuration (B1), SQLAlchemy ORM model (B3), ticket service / transaction scripts (B5), ticket repository layer (B4), database initialization and migrations (B8), data access documentation, project documentation, end-to-end verification</li>
  <li><strong>Pull requests created:</strong>
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/45">#45 B8 – database initialization and migrations</a>,
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/44">#44 B4 – ticket repository layer</a>,
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/41">#41 B5 – ticket service transaction scripts</a>,
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/36">#36 B3 – SQLAlchemy ORM model</a>
  </li>
</ul>

<h4>Sydney Gilchrist — Presentation Layer</h4>
<ul>
  <li><strong>Primary responsibilities:</strong> React project setup and structure (P1), CORS configuration (F3), ticket list table component (P3), ticket create form with client-side validation (P4), user feedback and error display (P5), page loading/error states (P2), presentation layer documentation</li>
  <li><strong>Pull requests created:</strong>
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/46">#46 P4 – ticket create form with client validation</a>,
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/43">#43 P3 – ticket list table component</a>,
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/35">#35 P1 – Vite frontend setup</a>,
    <a href="https://github.com/The-Mighty-Pythons/titanhelp-mighty-pythons/pull/32">#32 F3 – CORS configuration</a>
  </li>
</ul>


<h3>Team Collaboration Assessment</h3>
<p>
  The team held weekly syncs via Discord to coordinate integration points and review pull requests together. 
  Work was distributed evenly across layers with each member taking ownership of their assigned responsibilities. 
  Code reviews were conducted on all pull requests before merging to dev. 
  Weekly merges to main were performed.
</p>

<!-- ═══════════════════════════════════════════════════════════════ -->
<h2 id="overview">Project Overview</h2>

<h3>Description and Purpose</h3>
<p>
  TitanHelp is a full-stack help desk ticket management application. It allows users to submit support tickets
  describing a problem, assign a priority level, and track the resolution status of each ticket. The system
  provides a clean web interface for creating and viewing tickets, with data persisted to a relational database.
</p>
<p>
  The primary purpose of this project is to demonstrate a clear, layered architecture where each layer has a
  single, well-defined responsibility. The application is intentionally scoped to a focused set of features so
  that the architectural structure is the central demonstration.
</p>

<h3>Technology Stack</h3>
<table>
  <thead>
    <tr><th>Layer</th><th>Technology</th><th>Justification</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Presentation</td>
      <td>React 18 (Vite)</td>
      <td>Component-based model maps cleanly to the Template View pattern. Vite provides fast local development with minimal configuration overhead.</td>
    </tr>
    <tr>
      <td>Application / Business Logic</td>
      <td>Python 3 / Flask</td>
      <td>Flask is explicit and lightweight, making it easy to structure code into distinct layers without a heavy framework making architectural decisions for us. This keeps the layering visible and intentional.</td>
    </tr>
    <tr>
      <td>Data Access</td>
      <td>SQLAlchemy + Flask-Migrate</td>
      <td>SQLAlchemy implements the Data Mapper pattern and decouples business objects from database tables. Flask-Migrate (Alembic) provides versioned, repeatable schema migrations.</td>
    </tr>
    <tr>
      <td>Database</td>
      <td>SQLite</td>
      <td>Sufficient for the scope of this project. Requires no separate server process, making local setup straightforward for all team members.</td>
    </tr>
  </tbody>
</table>

<h3>Architecture Overview</h3>
<p>
  The application follows a strict three-layer architecture with a React frontend communicating to a Flask
  backend via a documented JSON REST API. Full architecture documentation, including a layer diagram and
  design pattern justifications, is provided here:
</p>
<p>
  <a href="titanhelp-mighty-pythons/docs/architecture.md">TitanHelp Architecture and Design Documentation</a>
</p>

<!-- ═══════════════════════════════════════════════════════════════ -->
<h2 id="requirements-analysis">Requirements Analysis</h2>

<h3>Initial Project Requirements</h3>
<p>
  The initial goal of TitanHelp was to develop a ticket management application capable of handling
  basic help desk functionality. The core requirements defined at project start were:
</p>
<ul>
  <li>Display all existing tickets in a list or table</li>
  <li>Create new tickets via a form with validation</li>
  <li>Persist tickets to a relational database using an ORM</li>
  <li>Implement clear separation of concerns across Presentation, Application, and Data Access layers</li>
  <li>Apply named architectural patterns appropriate to each layer</li>
</ul>

<h3>Requirement Changes During Development</h3>
<p>
  During development, adjustments were made to ensure alignment with the project specification.
  These included refining validation logic within the service layer and confirming that the database
  model matched the required schema. The following table documents the more significant scope changes:
</p>
<table>
  <thead>
    <tr><th>Change</th><th>Original</th><th>Revised</th><th>Rationale</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Status update added</td>
      <td>Tickets were read-only after creation</td>
      <td>Added <code>PATCH /api/tickets/:id/status</code> with inline table dropdown</td>
      <td>Core help desk workflow requires tickets to be closeable; added as a natural extension of the data model</td>
    </tr>
    <tr>
      <td>Custom React hook deferred</td>
      <td>Plan included a <code>useTickets.js</code> hook for state management</td>
      <td>State management kept in <code>App.jsx</code> directly</td>
      <td>Core features were prioritized; hook extraction is a refactor that does not change behavior and is documented as a future improvement in the architecture docs</td>
    </tr>
  </tbody>
</table>

<h3>Feature Prioritization</h3>
<p>Features were prioritized using a Must Have / Should Have / Future framework:</p>
<ul>
  <li><strong>Must Have (completed):</strong> Create ticket, list tickets, server-side validation, client-side validation, data persistence, CORS, documented API contract</li>
  <li><strong>Should Have (completed):</strong> Update ticket status inline, paginated table, error and loading states, comprehensive backend tests</li>
  <li><strong>Future:</strong> Custom <code>useTickets</code> hook, frontend component tests, single ticket detail view, delete ticket</li>
</ul>

<!-- ═══════════════════════════════════════════════════════════════ -->
<h2 id="technical">Technical Implementation</h2>

<h3>Design Patterns</h3>
<table>
  <thead>
    <tr><th>Pattern</th><th>Where Applied</th><th>Benefit</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Front Controller</td>
      <td>Flask Blueprint (<code>tickets_controller.py</code>)</td>
      <td>All HTTP requests enter through one routing registry; routing logic is separated from business logic</td>
    </tr>
    <tr>
      <td>Transaction Script</td>
      <td><code>ticket_service.py</code></td>
      <td>Each operation (list, create, update status) is one method that runs the full workflow; easy to read and test</td>
    </tr>
    <tr>
      <td>Repository</td>
      <td><code>ticket_repository.py</code></td>
      <td>All database queries are behind a clean interface; the rest of the app never calls SQLAlchemy directly</td>
    </tr>
    <tr>
      <td>Data Mapper</td>
      <td>SQLAlchemy ORM + <code>to_dict()</code></td>
      <td>Domain objects are decoupled from the database; the mapping between Python object and table row is explicit and centralized</td>
    </tr>
    <tr>
      <td>Page Controller</td>
      <td><code>App.jsx</code></td>
      <td>Owns state and orchestrates data loading; child components receive data via props and do not fetch independently</td>
    </tr>
    <tr>
      <td>Template View</td>
      <td><code>TicketForm.jsx</code>, <code>TicketsTable.jsx</code></td>
      <td>Components are responsible only for rendering their props; display logic is separated from data management</td>
    </tr>
  </tbody>
</table>

<h3>Database Schema</h3>
<p>A single <code>tickets</code> table stores all ticket records:</p>
<table>
  <thead>
    <tr><th>Column</th><th>Type</th><th>Constraints</th></tr>
  </thead>
  <tbody>
    <tr><td><code>ID</code></td><td>INTEGER</td><td>Primary key, auto-increment</td></tr>
    <tr><td><code>Name</code></td><td>VARCHAR(100)</td><td>NOT NULL</td></tr>
    <tr><td><code>Date</code></td><td>DATETIME</td><td>NOT NULL, server default = current timestamp</td></tr>
    <tr><td><code>Problem_Description</code></td><td>VARCHAR(1000)</td><td>NOT NULL</td></tr>
    <tr><td><code>Status</code></td><td>VARCHAR(20)</td><td>NOT NULL, default = <code>'Open'</code></td></tr>
    <tr><td><code>Priority</code></td><td>ENUM</td><td>NOT NULL, values: <code>Low</code> / <code>Medium</code> / <code>High</code></td></tr>
  </tbody>
</table>
<p>
  Schema changes are managed with Flask-Migrate (Alembic). The initial migration script is located at
  <code>backend/TitanHelp.Backend/migrations/versions/</code>.
</p>

<h3>API Design</h3>
<p>
  The frontend and backend communicate via a REST API with JSON bodies. All field names use
  <strong>snake_case</strong> consistently. Full endpoint documentation including sample payloads and error
  formats is in the API contract:
</p>
<p><a href="titanhelp-mighty-pythons/docs/api-contract.md">TitanHelp API Contract Specification</a></p>

<!-- ═══════════════════════════════════════════════════════════════ -->
<h2 id="process">Development Process</h2>

<h3>GitHub Workflow</h3>
<ul>
  <li>All development work was done on <strong>feature branches</strong> named with the convention <code>feature/[story-id]-[short-description]</code> (e.g., <code>feature/b5-ticket-service</code>)</li>
  <li>No code was committed directly to <code>main</code></li>
  <li>All changes were integrated via <strong>pull requests</strong> requiring at least one team member review before merging</li>
  <li>The <code>dev</code> branch served as the integration branch; <code>main</code> represents stable, reviewed code</li>
</ul>

<h3>Code Review Process</h3>
<p>
  The backend system follows a layered architecture consisting of controllers, services, repositories,
  and ORM models. Each team member implemented specific components within their assigned layer while
  working on separate branches to isolate changes. Pull request reviews were used to verify that new
  code stayed within the correct layer boundary — for example, confirming that SQLAlchemy queries
  remained inside the repository and that service methods contained no Flask objects.
</p>
<ul>
  <li>Pull requests included a description of what changed and why</li>
  <li>Reviewers checked that changes stayed within the correct architectural layer</li>
</ul>

<h3>Issue Tracking</h3>
<p>
  User stories and tasks were tracked on the team GitHub Project Board.
  Each user story was broken into tasks assigned to the responsible layer owner.
</p>
<p>
  <a href="https://github.com/orgs/The-Mighty-Pythons/projects/1">The Mighty Pythons – TitanHelp Project Board</a>
</p>

<h3>Testing Strategy</h3>
<p>Backend testing was implemented across all layers using <strong>pytest</strong>:</p>
<ul>
  <li><strong>API tests</strong> (<code>test_api.py</code>) — Integration tests that call Flask endpoints end-to-end with an in-memory SQLite database</li>
  <li><strong>Service tests</strong> (<code>test_services.py</code>) — Unit tests for business logic: valid inputs, invalid inputs, edge cases</li>
  <li><strong>Repository tests</strong> (<code>test_repositories.py</code>) — Tests that the data access layer correctly reads and writes to the database</li>
  <li><strong>Model tests</strong> (<code>test_models.py</code>) — Tests that the ORM model and <code>to_dict()</code> serialization produce the correct output</li>
</ul>
<p>Frontend testing was identified as a future improvement. Manual end-to-end testing was performed throughout development.</p>

<!-- ═══════════════════════════════════════════════════════════════ -->
<h2 id="user-docs">User Documentation</h2>

<h3>Installation and Setup</h3>
<p>See <a href="#run">How to Run Locally</a> below for full installation and setup instructions.</p>

<h3>User Guide</h3>

<h4>Viewing Tickets</h4>
<p>
  When the application loads, all existing tickets are displayed in a table showing Name, Date, Status,
  Priority, and Problem Description. If no tickets exist yet, the table displays a "No tickets" message.
  Tickets are paginated at 5 per page — use the <strong>Previous</strong> and <strong>Next</strong> buttons
  to navigate.
</p>

<h4>Creating a Ticket</h4>
<ol>
  <li>Fill in the <strong>Name</strong> field (required, max 100 characters)</li>
  <li>Fill in the <strong>Problem Description</strong> field (required, max 1000 characters)</li>
  <li>Select a <strong>Priority</strong> from the dropdown: Low, Medium, or High</li>
  <li>Click <strong>Submit</strong></li>
  <li>The new ticket will appear in the table immediately.</li>
</ol>
<p>
  If any required field is missing or exceeds the character limit, an error message will appear below
  the relevant field before the request is sent. If the server returns a validation error, it will be
  displayed inline as well.
</p>

<h4>Updating Ticket Status</h4>
<p>
  Each ticket row contains a <strong>Status</strong> dropdown. Changing the dropdown value immediately
  sends an update to the server and refreshes the ticket list.
</p>

<h4>Screenshots</h4>

<h3>Ticket List View</h3>
<p>The ticket list displays all created tickets with their details in a table format.</p>
<img src="titanhelp-mighty-pythons/docs/screenshots/TicketListView1.png" alt="Ticket List View - Initial Display" width="600" />
<img src="titanhelp-mighty-pythons/docs/screenshots/TicketListView2.png" alt="Ticket List View - Full Table" width="600" />

<h3>Ticket Creation Form</h3>
<p>The ticket form includes validation to ensure all required fields are properly filled.</p>
<img src="titanhelp-mighty-pythons/docs/screenshots/TicketFormError1.png" alt="Ticket Form - Validation Error 1" width="600" />
<img src="titanhelp-mighty-pythons/docs/screenshots/TicketFormError2.png" alt="Ticket Form - Validation Error 2" width="600" />
<img src="titanhelp-mighty-pythons/docs/screenshots/TicketFormError3.png" alt="Ticket Form - Validation Error 3" width="600" />

<h3>Ticket List After Creation</h3>
<p>After successfully creating a ticket, it immediately appears in the ticket list.</p>
<img src="titanhelp-mighty-pythons/docs/screenshots/TicketListAfterCreate.png" alt="Ticket List - After Creating a Ticket" width="600" />

<h3>API Documentation</h3>
<p>
  The full REST API documentation including all endpoints, request and response shapes, and error formats
  is available in the <a href="titanhelp-mighty-pythons/docs/api-contract.md">API Contract</a>.
</p>

<h3>Troubleshooting</h3>
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

<!-- ═══════════════════════════════════════════════════════════════ -->
<h2 id="evaluation">Project Evaluation</h2>

<h3>Technical Achievements</h3>
<ul>
  <li>Implemented a complete, working full-stack application with genuine separation between all three architectural layers</li>
  <li>Backend service layer contains no Flask objects, making it fully decoupled from the HTTP layer and testable in isolation</li>
  <li>Repository pattern successfully hides all SQLAlchemy from the service and controller layers</li>
  <li>Comprehensive backend test suite covering API, service, repository, and model layers with an in-memory test database</li>
  <li>Schema managed through versioned Flask-Migrate migrations, demonstrating repeatable, professional database management</li>
  <li>Consistent API contract documented upfront and honored by both frontend and backend throughout development</li>
  <li>Established a GitHub collaboration workflow with feature branches, pull request reviews, and integration through a shared <code>dev</code> branch</li>
</ul>

<h3>Challenges Encountered</h3>
<ul>
  <li>
    <strong>API contract alignment:</strong> Coordinating the API contract early was essential. We encountered
    a field naming mismatch (camelCase vs. snake_case) during initial integration and resolved it by
    explicitly documenting snake_case in the contract before writing any integration code. This prevented
    the same issue from recurring across subsequent features.
  </li>
  <li>
    <strong>Coordinating development across layers:</strong> Ensuring that database models matched the
    required specification and that each layer's interface was ready for the next required active
    communication across the team. Changes to the data model or API contract had downstream effects that
    needed to be caught early through pull request review.
  </li>
  <li>
    <strong>Unplanned feature scope expansion:</strong> The ability to update a ticket's status was not
    included in the original project plan. During end-to-end testing, the team recognized that a help desk
    system with no way to close a ticket did not reflect a realistic workflow. The
    <code>PATCH /api/tickets/:id/status</code> endpoint and inline status dropdown were added as an unplanned
    sprint item (B10). This reinforced the value of reviewing requirements against real user workflows
    before finalizing scope.
  </li>
  <li>
    <strong>Testing integrated late in development:</strong> Backend unit and integration tests were written
    as a dedicated effort near the end of the project rather than alongside feature development. While the
    final test suite provides good coverage, writing tests after the fact meant bugs were caught later than
    they could have been. In future projects, the team would prioritize writing tests incrementally with
    each feature.
  </li>
</ul>

<h3>Code Quality Assessment</h3>
<p>
  The team followed several best practices to maintain code quality throughout development, including
  clear layer separation, pull request reviews, and structured commit messages. The backend layer
  boundaries are clean and consistently enforced. The frontend component structure is functional but
  could benefit from further decomposition — <code>App.jsx</code> manages state that would ideally live
  in a dedicated <code>useTickets</code> hook. Overall the code is readable, the patterns are applied
  consistently, and the test suite gives confidence in the backend behavior.
</p>

<h3>Future Enhancements</h3>
<ul>
  <li><strong><code>useTickets</code> React hook</strong> — Extract state management and API calls from <code>App.jsx</code> into a dedicated hook for cleaner component separation</li>
  <li><strong>Frontend component tests</strong> — Add Vitest/React Testing Library tests for <code>TicketForm</code> and <code>TicketsTable</code></li>
  <li><strong>Single ticket view</strong> — <code>GET /api/tickets/:id</code> endpoint and a detail page</li>
  <li><strong>Delete ticket</strong> — Allow tickets to be removed from the system</li>
  <li><strong>Authentication</strong> — User login so tickets are associated with the submitter</li>
  <li><strong>Advanced filtering and search</strong> — Filter tickets by status, priority, or date range</li>
  <li><strong>Production database</strong> — Replace SQLite with PostgreSQL for a deployed environment</li>
  <li><strong>Cloud deployment</strong> — Host the application on a cloud platform for public access</li>
</ul>

<h3>Team Collaboration Evaluation</h3>
<p>
  Communication was consistent throughout the project. Establishing the API contract in the first sprint
  prevented the most common full-stack integration problems. Code reviews were thorough and helped catch
  layer violations before they merged to main. If we were to do this again, we would set up the migrations
  earlier in the process to avoid a manual schema reset mid-sprint, and we would write tests alongside
  each feature rather than in a single push at the end.
</p>

<!-- ═══════════════════════════════════════════════════════════════ -->
<h2 id="repo-requirements">Repository Requirements</h2>

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

<!-- ═══════════════════════════════════════════════════════════════ -->
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

<!-- ═══════════════════════════════════════════════════════════════ -->
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

<!-- ═══════════════════════════════════════════════════════════════ -->
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

<!-- ═══════════════════════════════════════════════════════════════ -->
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
<p>For the best experience, use Visual Studio Code</p>

<h3>Ideal Method: Run via VS Code</h3>
<ol>
  <li>Open VS Code</li>
  <li>Select Open folder and open <code>titanhelp-mighty-pythons/</code></li>
  <li>Open a new Terminal in VSCode</li>
  <li>In VSCode use the <code>Ctrl+Shift+P</code> command (<code>Cmd+Shift+P</code> on macOS) to access the Command Palette</li>
  <li>Select <strong>Tasks: Run Task</strong></li>
  <li>Select the <strong>Setup Everything (First Time)</strong> option</li>
  <img src="titanhelp-mighty-pythons/docs/FirstTimeSetup.png" alt="VSCode Task Menu showing Setup Everything (First Time)" width="600" />
  <li>Go to <strong>Run and Debug</strong> (if you cannot find it, check under View → Run)</li>
  <li>Select: <code>Full Stack: Backend + Frontend</code></li>
  <li>Click the green play button</li>
</ol>
<p>You should see a full list of tasks running in the call stack, and no errors in the terminal.</p>
<p>From here, until automatic launch is configured, you will open a new browser window and enter
 <code>http://localhost:5173</code> for the frontend, and <code>http://127.0.0.1:5000/api/tickets</code> for the backend.</p>
<p>Stop the project in VS Code when done.</p>

<h3>Running Tests</h3>
<p>For now you will manually run tests.</p>
<p>Go to the backend directory with file explorer <code>\titanhelp-mighty-pythons\backend\TitanHelp.Backend</code></p>
<p>Open a new terminal session and run <code>python -m pytest -v</code></p>

<h3>Database Location</h3>
<p>For local development, the SQLite database file is stored at:</p>
<p><code>backend/TitanHelp.Backend/instance/titanhelp.db</code></p>
<p>Database schema setup and updates are handled with Flask-Migrate using:</p>
<p><code>flask db init</code></p>
<p><code>flask db migrate</code></p>
<p><code>flask db upgrade</code></p>

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
