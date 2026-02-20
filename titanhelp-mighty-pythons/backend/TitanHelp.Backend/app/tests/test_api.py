def test_get_tickets(client):
    response = client.get("/api/tickets")
    assert response.status_code == 200