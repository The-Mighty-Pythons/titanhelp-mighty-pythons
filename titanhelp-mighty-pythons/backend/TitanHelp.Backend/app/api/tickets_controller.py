from flask import Blueprint, jsonify, request

tickets_bp = Blueprint("tickets", __name__)

# TODO - Replace with real Service/Repo calls later.
@tickets_bp.get("/tickets")
def get_tickets():
    return jsonify([]), 200

@tickets_bp.post("/tickets")
def create_ticket():
    return jsonify({"error": "Not implemented yet."}), 501
