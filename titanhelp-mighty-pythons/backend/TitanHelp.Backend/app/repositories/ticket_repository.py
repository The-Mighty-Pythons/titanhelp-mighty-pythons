from typing import List
from ..extensions import db
from ..models.ticket import Ticket

##this is where you will define the repository for handling ticket-related database operations

class TicketRepository:
    def get_all(self) -> List[Ticket]:
        return Ticket.query.order_by(Ticket.ID.asc()).all()

    def add(self, ticket: Ticket) -> Ticket:
        db.session.add(ticket)
        db.session.commit()
        return ticket