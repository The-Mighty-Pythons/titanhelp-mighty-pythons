from flask import Blueprint, jsonify, request
from ..schemas.ticket_validation import validate_create_ticket
from ..services.ticket_service import TicketService

tickets_bp = Blueprint("tickets", __name__)

service = TicketService()

@tickets_bp.get("/tickets")
def get_tickets():
    # list[Tickets]
    return jsonify(service.get_all_tickets()), 200

@tickets_bp.post("/tickets")
def create_ticket():
    payload = request.get_json(silent=True) or {}

    errors = validate_create_ticket(payload)
    if errors:
        return jsonify({"errors": errors}), 400

    created = service.create_ticket(
        name=payload["name"],
        problem_description=payload["problem_description"],
        priority=payload["priority"],
    )
    
    return jsonify(created), 201
