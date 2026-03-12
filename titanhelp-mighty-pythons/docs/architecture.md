# TitanHelp — Architecture and Design Documentation

## Overview

TitanHelp is a help desk ticket management system built using a **three-layer architecture**:
- **Presentation Layer** — React (Vite) frontend
- **Application / Business Logic Layer** — Flask service classes
- **Data Access Layer** — SQLAlchemy ORM with SQLite

Each layer has a single responsibility and communicates only with the layer directly adjacent to it. This separation makes the codebase easier to understand, test, and modify independently.

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                       │
│                                                             │
│   App.jsx (state + orchestration)                           │
│     ├── TicketForm.jsx  (create ticket UI + validation)     │
│     └── TicketsPage.jsx                                     │
│           └── TicketsTable.jsx (display + pagination)       │
│                                                             │
│   ticketApi.js  (HTTP calls to backend API)                 │
└───────────────────────┬─────────────────────────────────────┘
                        │  JSON over HTTP (REST)
                        │  GET /api/tickets
                        │  POST /api/tickets
                        │  PATCH /api/tickets/:id/status
┌───────────────────────▼─────────────────────────────────────┐
│               APPLICATION / BUSINESS LOGIC LAYER            │
│                                                             │
│   tickets_controller.py  (Flask Blueprint — routes)         │
│     └── ticket_service.py  (business rules + validation)    │
│           └── ticket_repository.py  (data access only)      │
└───────────────────────┬─────────────────────────────────────┘
                        │  SQLAlchemy ORM
┌───────────────────────▼─────────────────────────────────────┐
│                    DATA ACCESS LAYER                        │
│                                                             │
│   ticket.py (ORM model — maps to "tickets" table)           │
│   SQLite database (titanhelp.db via Flask-Migrate)          │
└─────────────────────────────────────────────────────────────┘
```

---

## Layer Responsibilities

### Presentation Layer (React)

The frontend is responsible for everything the user sees and interacts with.

| File | Responsibility |
|---|---|
| `App.jsx` | Owns application state (ticket list), orchestrates data loading and status updates |
| `TicketForm.jsx` | Controlled form inputs, client-side field validation, calls API on submit, shows feedback |
| `TicketsPage.jsx` | Wrapper that passes ticket data and callbacks down to the table |
| `TicketsTable.jsx` | Renders ticket rows, handles pagination, provides inline status dropdown |
| `ticketApi.js` | Centralizes all HTTP fetch calls — components never call `fetch()` directly |

The frontend does **not** contain business rules. It enforces only basic input constraints (required fields, max lengths) as a usability convenience — the backend always re-validates.

### Application / Business Logic Layer (Flask)

The backend is responsible for all business rules, validation, and coordinating the workflow between the HTTP interface and the database.

| File | Responsibility |
|---|---|
| `tickets_controller.py` | Receives HTTP requests, delegates to service, returns JSON responses with proper status codes |
| `ticket_service.py` | Enforces business rules: required fields, priority values, default status, data normalization |
| `ticket_validation.py` | Schema-level validation helpers called by the controller before the service receives data |

The service layer contains **no Flask objects** (no `request`, no `jsonify`). This means service logic can be tested without running a web server.

### Data Access Layer (SQLAlchemy + SQLite)

The data access layer is responsible only for reading from and writing to the database.

| File | Responsibility |
|---|---|
| `ticket_repository.py` | All SQLAlchemy queries live here — `get_all()`, `create_ticket()`, `update_status()` |
| `ticket.py` (ORM model) | Maps the `Ticket` Python class to the `tickets` database table; includes `to_dict()` for serialization |
| `migrations/` | Flask-Migrate (Alembic) tracks schema changes as versioned migration scripts |

No code outside the repository directly calls `db.session` or issues SQL queries.

---

## Design Patterns

### Backend

**Front Controller (Flask Blueprint)**
All HTTP requests enter through a single routing registry (`tickets_bp` Blueprint registered in `create_app()`). The controller handles routing and delegates immediately — it contains no business logic itself.

**Transaction Script (Service Layer)**
Each operation on a ticket (`list_tickets`, `create_ticket`, `update_ticket_status`) is implemented as a single method in `TicketService`. Each method executes the full workflow for that operation in one place: validate → apply defaults → call repository. This keeps business logic centralized and easy to follow.

**Repository Pattern**
`TicketRepository` provides a clean interface (`get_all`, `create_ticket`, `update_status`) that hides SQLAlchemy from the rest of the application. If we changed from SQLite to PostgreSQL, or from SQLAlchemy to a different ORM, only the repository would need to change.

**Data Mapper (via SQLAlchemy ORM)**
SQLAlchemy maps the `Ticket` Python object to the `tickets` database table automatically. The `to_dict()` method on the model acts as the serialization step, converting the ORM object to a plain dictionary that matches the documented API contract. This keeps the JSON shape explicitly defined in one place.

### Frontend

**Page Controller**
`App.jsx` acts as the page controller for the tickets view. It owns the ticket list state, triggers data loading on mount, and passes data and callback functions down to child components. Components do not fetch data themselves.

**Template View**
`TicketForm.jsx` and `TicketsTable.jsx` are pure rendering components. They receive props and display them — they do not manage shared state or call the API directly (except `TicketForm`, which calls `ticketApi.js` and notifies the parent via the `onCreated` callback).

**API Module (Service Locator for HTTP)**
`ticketApi.js` centralizes all `fetch()` calls. Components import named functions (`getTickets`, `createTicket`, `updateTicketStatus`) rather than constructing HTTP requests themselves. This means the backend URL and request format are defined in exactly one file.

---

## Technology Stack Justification

| Layer | Choice | Reason |
|---|---|---|
| Presentation | React (Vite) | Component-based model maps cleanly to the Template View pattern; Vite provides fast local development |
| Application | Flask (Python) | Lightweight, explicit routing, easy to structure into layers without a heavy framework enforcing decisions |
| Data Access | SQLAlchemy + Flask-Migrate | Mature ORM that implements the Data Mapper pattern; Alembic migrations provide repeatable, versioned schema management |
| Database | SQLite | Sufficient for development and demonstration; no separate server process required |

---

## What We Would Add With More Time

- **`useTickets` custom React hook** — App.jsx currently manages data loading and state directly. A dedicated hook (`useTickets.js`) would extract this logic, making `App.jsx` a cleaner orchestration component and making the data-fetching behavior independently testable. This was deprioritized in favor of completing core functionality.
- **Frontend tests** — Backend tests cover service, repository, and API layers. Frontend component testing with Vitest/React Testing Library was identified as a future improvement.
- **`GET /api/tickets/:id`** — Single ticket retrieval is not yet implemented; the current UI loads all tickets and filters client-side.
