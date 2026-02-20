import enum
from sqlalchemy.sql import func
from app.extensions import db


class TicketPriority(enum.Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"


class Ticket(db.Model):
    __tablename__ = "tickets"

    ID = db.Column(db.Integer, primary_key=True)

    Name = db.Column(db.String(100), nullable=False)

    Date = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    Problem_Description = db.Column(db.String(1000), nullable=False)

    Status = db.Column(
        db.String(20),
        nullable=False,
        default="Open"
    )

    Priority = db.Column(
        db.Enum(TicketPriority),
        nullable=False
    )

def to_dict(self):
    # datetime objects are not JSON serializable, so we convert to ISO format string
    iso = (
        self.Date.replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )

    # json contract requires lowercase
    return {
        "id": self.ID,
        "name": self.Name,
        "date": iso,
        "problem_description": self.Problem_Description,
        "status": self.Status,
        "priority": self.Priority.value,
    }
