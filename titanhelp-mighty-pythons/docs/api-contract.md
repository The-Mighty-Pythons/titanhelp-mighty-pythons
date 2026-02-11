<!-- base URL -->
http://localhost:5000/api


<!-- GET/tickets: 200 response -->
[
  {
    "id": 1,
    "name": "Amanda Crotty",
    "date": "2026-02-09T20:15:12Z",
    "problem_description": "Printer is jammed.",
    "status": "Open",
    "priority": "Medium"
  }
]


<!-- POST/tickets: request -->
{
  "name": "Amanda Crotty",
  "problem_description": "Printer is jammed.",
  "priority": "Medium"
}


<!-- POST/tickets: 200 success -->
{
  "id": 1,
  "name": "Amanda Crotty",
  "date": "2026-02-09T20:15:12Z",
  "problem_description": "Printer is jammed.",
  "status": "Open",
  "priority": "Medium"
}

<!-- GET/tickets: 400 error -->
{
  "error": "Ticket not found."
}

<!-- POST/tickets: 400 error -->
{
  "errors": {
    "name": "Name is required and must be <= 100 chars.",
    "problem_description": "Problem description is required and must be <= 1000 chars.",
    "priority": "Priority must be Low, Medium, or High."
  }
}
