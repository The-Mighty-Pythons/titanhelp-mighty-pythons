from app.repositories.ticket_repository import TicketRepository
from app.models.ticket import Ticket, TicketPriority


def test_get_all_empty(app):
    repo = TicketRepository()
    assert repo.get_all() == []
