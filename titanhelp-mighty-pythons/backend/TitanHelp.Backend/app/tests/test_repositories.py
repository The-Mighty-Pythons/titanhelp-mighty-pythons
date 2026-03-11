from app.repositories.ticket_repository import TicketRepository
from app.models.ticket import Ticket, TicketPriority


def test_get_all_empty(app):
    repo = TicketRepository()
    assert repo.get_all() == []

def test_create_and_retrieve(app):
    repo = TicketRepository()
    ticket = Ticket(
        Name="Repo Ticket",
        Problem_Description="Testing repository create.",
        Priority=TicketPriority.High
    )
    saved = repo.create_ticket(ticket)
    assert saved.ID is not None
    assert saved.Name == "Repo Ticket"

    all_tickets = repo.get_all()
    assert len(all_tickets) == 1
    assert all_tickets[0].Name == "Repo Ticket"