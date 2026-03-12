# TitanHelp API Contract

**Base URL:** `http://localhost:5000/api`

All request and response bodies use `application/json`.
All JSON field names use **snake_case**.

---

## Ticket Object

| Field               | Type   | Description                              |
|---------------------|--------|------------------------------------------|
| `id`                | int    | Unique identifier                        |
| `name`              | string | Submitter's name (max 100 chars)         |
| `date`              | string | ISO 8601 UTC timestamp (e.g. `2026-02-09T20:15:12Z`) |
| `problem_description` | string | Description of the issue (max 1000 chars) |
| `status`            | string | `"Open"` or `"Closed"`                  |
| `priority`          | string | `"Low"`, `"Medium"`, or `"High"`        |

---

## Endpoints

### GET /api/tickets

Returns all tickets.

**Response 200 OK**
```json
[
  {
    "id": 1,
    "name": "Arthur Everest",
    "date": "2026-02-09T20:15:12Z",
    "problem_description": "Printer is jammed.",
    "status": "Open",
    "priority": "Medium"
  }
]
```

---

### POST /api/tickets

Creates a new ticket.

**Request body**
```json
{
  "name": "Arthur Everest",
  "problem_description": "Printer is jammed.",
  "priority": "Medium"
}
```

**Response 201 Created**
```json
{
  "id": 1,
  "name": "Arthur Everest",
  "date": "2026-02-09T20:15:12Z",
  "problem_description": "Printer is jammed.",
  "status": "Open",
  "priority": "Medium"
}
```

**Response 400 Bad Request**
```json
{
  "errors": {
    "name": "Name is required and must be <= 100 chars.",
    "problem_description": "Problem description is required and must be <= 1000 chars.",
    "priority": "Priority must be Low, Medium, or High."
  }
}
```

> Only failing fields are included in `errors`.

---

### PATCH /api/tickets/{id}/status

Updates the status of an existing ticket.

**Request body**
```json
{
  "status": "Closed"
}
```

**Response 200 OK**
```json
{
  "id": 1,
  "name": "Arthur Everest",
  "date": "2026-02-09T20:15:12Z",
  "problem_description": "Printer is jammed.",
  "status": "Closed",
  "priority": "Medium"
}
```

**Response 400 Bad Request**
```json
{
  "errors": {
    "status": "Status must be Open or Closed."
  }
}
```

**Response 404 Not Found**
```json
{
  "error": "Ticket not found."
}
```
