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

def test_update_status(app):
    repo = TicketRepository()
    ticket = Ticket(
        Name="Status Ticket",
        Problem_Description="Will update status.",
        Priority=TicketPriority.Low
    )
    saved = repo.create_ticket(ticket)

    updated = repo.update_status(saved.ID, "Closed")
    assert updated is not None
    assert updated.Status == "Closed"

def test_update_status_not_found(app):
    repo = TicketRepository()
    result = repo.update_status(9999, "Closed")
    assert result is None