import enum
from sqlalchemy.sql import func
from app.extensions import db


class TicketPriority(enum.Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"


class Ticket(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    problem_description = db.Column(db.String(1000), nullable=False)

    date = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Open"
    )

    priority = db.Column(
        db.Enum(TicketPriority),
        nullable=False
    )
