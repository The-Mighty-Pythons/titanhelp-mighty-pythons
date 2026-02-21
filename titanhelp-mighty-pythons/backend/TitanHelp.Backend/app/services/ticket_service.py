##this is where we will define service functions for handling business logic related to tickets
## todo : get ticket(id), update ticket(id), delete ticket(id), which is a soft delete when the ticket closes

from ..models.ticket import Ticket, TicketPriority
from ..repositories.ticket_repository import TicketRepository

class TicketService:
    def __init__(self, repo: TicketRepository | None = None):
        self.repo = repo or TicketRepository()

    def get_all_tickets(self) -> list[dict]:
        tickets = self.repo.get_all()
        return [t.to_dict() for t in tickets]

    def create_ticket(self, *, name: str, problem_description: str, priority: str) -> dict:
        # defaults + validation (minimal)
        name = (name or "").strip()
        problem_description = (problem_description or "").strip()
        priority = (priority or "Medium").strip()

        if not name:
            raise ValueError("name is required")
        if not problem_description:
            raise ValueError("problem_description is required")

        try:
            priority_enum = TicketPriority(priority)
        except ValueError:
            raise ValueError("priority must be one of: Low, Medium, High")

        ticket = Ticket(
            Name=name,
            Problem_Description=problem_description,
            Priority=priority_enum,
            Status="Open",
        )
        saved = self.repo.add(ticket)
        return saved.to_dict()