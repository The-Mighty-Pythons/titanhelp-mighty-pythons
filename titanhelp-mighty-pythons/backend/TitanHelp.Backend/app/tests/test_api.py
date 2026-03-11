import json


def test_get_tickets_returns_200(client):
    response = client.get("/api/tickets")
    assert response.status_code == 200

def test_get_tickets_returns_list(client):
    response = client.get("/api/tickets")
    data = response.get_json()
    assert isinstance(data, list)

def test_post_ticket_success(client):
    payload = {
        "name": "Test Ticket",
        "problem_description": "Something is broken.",
        "priority": "High"
    }
    response = client.post(
        "/api/tickets",
        data=json.dumps(payload),
        content_type="application/json"
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Test Ticket"
    assert data["problem_description"] == "Something is broken."
    assert data["priority"] == "High"
    assert data["status"] == "Open"
    assert "id" in data
    assert "date" in data