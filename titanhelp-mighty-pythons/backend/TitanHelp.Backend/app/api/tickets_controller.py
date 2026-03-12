from flask import Blueprint, jsonify, request
from ..schemas.ticket_validation import validate_create_ticket, validate_update_status
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


# PATCH is the HTTP protocol verb for partial updates, a required keyword
@tickets_bp.patch("/tickets/<int:ticket_id>/status")
def update_ticket_status(ticket_id):
    payload = request.get_json(silent=True) or {}

    errors = validate_update_status(payload)
    if errors:
        return jsonify({"errors": errors}), 400

    updated = service.update_ticket_status(ticket_id, payload["status"])
    if updated is None:
        return jsonify({"error": "Ticket not found."}), 404

    return jsonify(updated), 200
