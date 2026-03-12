from app.extensions import db
from app.models import Ticket
from app.models.ticket import TicketPriority


def test_create_ticket(app):
    t = Ticket(
        Name="Test",
        Problem_Description="Testing",
        Priority=TicketPriority.Low
        # Status is not provided, so it should default to "Open"
    )
    db.session.add(t)
    db.session.commit()

    result = Ticket.query.all()
    assert len(result) == 1
    assert result[0].Name == "Test"
    assert result[0].Priority == TicketPriority.Low
    assert result[0].Status == "Open"


def test_to_dict_returns_contract_fields(app):
    t = Ticket(
        Name="Dict Test",
        Problem_Description="Testing to_dict output.",
        Priority=TicketPriority.Medium
    )
    db.session.add(t)
    db.session.commit()

    result = t.to_dict()
    assert "id" in result
    assert "name" in result
    assert "date" in result
    assert "problem_description" in result
    assert "status" in result
    assert "priority" in result
    assert result["name"] == "Dict Test"
    assert result["problem_description"] == "Testing to_dict output."
    assert result["status"] == "Open"
    assert result["priority"] == "Medium"
