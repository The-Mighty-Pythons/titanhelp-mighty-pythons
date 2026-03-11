import json


def test_get_tickets_returns_200(client):
    response = client.get("/api/tickets")
    assert response.status_code == 200

def test_get_tickets_returns_list(client):
    response = client.get("/api/tickets")
    data = response.get_json()
    assert isinstance(data, list)