import pytest
from app.services.ticket_service import TicketService


def test_get_all_tickets_empty(app):
    service = TicketService()
    result = service.get_all_tickets()
    assert result == []

def test_create_ticket_returns_dict(app):
    service = TicketService()
    result = service.create_ticket(
        name="Service Test",
        problem_description="Created via service.",
        priority="Medium"
    )
    assert isinstance(result, dict)
    assert result["name"] == "Service Test"
    assert result["status"] == "Open"
    assert result["priority"] == "Medium"
    assert "id" in result
    assert "date" in result

def test_create_ticket_appears_in_get_all(app):
    service = TicketService()
    service.create_ticket(
        name="List Me",
        problem_description="Should appear in get_all.",
        priority="Low"
    )
    tickets = service.get_all_tickets()
    assert len(tickets) == 1
    assert tickets[0]["name"] == "List Me"

def test_create_ticket_missing_name_raises(app):
    service = TicketService()
    with pytest.raises(ValueError):
        service.create_ticket(
            name="",
            problem_description="No name provided.",
            priority="Low"
        )

def test_create_ticket_missing_description_raises(app):
    service = TicketService()
    with pytest.raises(ValueError):
        service.create_ticket(
            name="Valid Name",
            problem_description="",
            priority="Low"
        )

def test_create_ticket_invalid_priority_raises(app):
    service = TicketService()
    with pytest.raises(ValueError):
        service.create_ticket(
            name="Valid Name",
            problem_description="Valid description.",
            priority="Critical"
        )

def test_update_ticket_status(app):
    service = TicketService()
    created = service.create_ticket(
        name="Close Me",
        problem_description="Will be closed.",
        priority="Low"
    )
    updated = service.update_ticket_status(created["id"], "Closed")
    assert updated is not None
    assert updated["status"] == "Closed"

def test_update_ticket_status_not_found(app):
    service = TicketService()
    result = service.update_ticket_status(9999, "Closed")
    assert result is None
