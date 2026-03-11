import pytest
from app.services.ticket_service import TicketService


def test_get_all_tickets_empty(app):
    service = TicketService()
    result = service.get_all_tickets()
    assert result == []
