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