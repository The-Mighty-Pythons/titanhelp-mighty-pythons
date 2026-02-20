const API_BASE = "http://127.0.0.1:5000/api";

export async function getTickets() {
  const response = await fetch(`${API_BASE}/tickets`);

  if (!response.ok) {
    throw new Error("Failed to fetch tickets");
  }

  return await response.json();
}

export async function createTicket(ticketData) {
  const response = await fetch(`${API_BASE}/tickets`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(ticketData),
  });

  const data = await response.json();

  if (!response.ok) {
    throw data; // backend sends { errors: {...} }
  }

  return data;
}