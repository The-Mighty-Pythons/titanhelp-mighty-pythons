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

def test_post_ticket_appears_in_list(client):
    payload = {
        "name": "Appears In List",
        "problem_description": "Check list after create.",
        "priority": "Low"
    }
    client.post(
        "/api/tickets",
        data=json.dumps(payload),
        content_type="application/json"
    )
    response = client.get("/api/tickets")
    data = response.get_json()
    assert any(t["name"] == "Appears In List" for t in data)

def test_post_ticket_missing_name_returns_400(client):
    payload = {
        "problem_description": "No name provided.",
        "priority": "Low"
    }
    response = client.post(
        "/api/tickets",
        data=json.dumps(payload),
        content_type="application/json"
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "errors" in data
    assert "name" in data["errors"]


def test_post_ticket_missing_description_returns_400(client):
    payload = {
        "name": "No Description",
        "priority": "Medium"
    }
    response = client.post(
        "/api/tickets",
        data=json.dumps(payload),
        content_type="application/json"
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "errors" in data
    assert "problem_description" in data["errors"]


def test_post_ticket_invalid_priority_returns_400(client):
    payload = {
        "name": "Bad Priority",
        "problem_description": "This priority is invalid.",
        "priority": "Urgent"
    }
    response = client.post(
        "/api/tickets",
        data=json.dumps(payload),
        content_type="application/json"
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "errors" in data
    assert "priority" in data["errors"]


def test_post_ticket_empty_body_returns_400(client):
    response = client.post(
        "/api/tickets",
        data="{}",
        content_type="application/json"
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "errors" in data

def test_update_ticket_status_success(client):
    created = client.post(
        "/api/tickets",
        data=json.dumps({
            "name": "Patch Me",
            "problem_description": "Will be closed.",
            "priority": "Low"
        }),
        content_type="application/json"
    ).get_json()

    response = client.patch(
        f"/api/tickets/{created['id']}/status",
        data=json.dumps({"status": "Closed"}),
        content_type="application/json"
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "Closed"
    assert data["id"] == created["id"]

def test_update_ticket_status_invalid_returns_400(client):
    created = client.post(
        "/api/tickets",
        data=json.dumps({
            "name": "Bad Status",
            "problem_description": "Invalid status test.",
            "priority": "Medium"
        }),
        content_type="application/json"
    ).get_json()

    response = client.patch(
        f"/api/tickets/{created['id']}/status",
        data=json.dumps({"status": "Pending"}),
        content_type="application/json"
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "errors" in data
    assert "status" in data["errors"]

def test_update_ticket_status_not_found_returns_404(client):
    response = client.patch(
        "/api/tickets/9999/status",
        data=json.dumps({"status": "Closed"}),
        content_type="application/json"
    )
    assert response.status_code == 404
