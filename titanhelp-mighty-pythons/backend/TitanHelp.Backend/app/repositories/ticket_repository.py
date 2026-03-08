from __future__ import annotations

from typing import List
from ..extensions import db
from ..models.ticket import Ticket

##this is where you will define the repository for handling ticket-related database operations

class TicketRepository:
    def get_all(self) -> List[Ticket]:
        return Ticket.query.order_by(Ticket.ID.asc()).all()

    def create_ticket(self, ticket: Ticket) -> Ticket:
        db.session.add(ticket)
        db.session.commit()
        db.session.refresh(ticket)
        return ticket

    def update_status(self, ticket_id: int, status: str) -> Optional[Ticket]:
        ticket = Ticket.query.filter_by(ID=ticket_id).first()
        if ticket is None:
            return None

        ticket.Status = status
        db.session.commit()
        db.session.refresh(ticket)
        return ticket