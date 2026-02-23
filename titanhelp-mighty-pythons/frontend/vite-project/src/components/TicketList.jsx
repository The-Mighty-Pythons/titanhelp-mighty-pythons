function TicketList({ tickets }) {
  return (
    <div className="ticket-list">
      <h2>All Tickets</h2>
      <div className="ticket-grid">
      {tickets.map((ticket) => (
        <div key={ticket.id} className="ticket-card">
          <h3>{ticket.name}</h3>
          <p>{ticket.problem_description}</p>
          <p>
            <strong>Priority:</strong> {ticket.priority} | {" "}
            <strong>Status:</strong> {ticket.status}
          </p>
          </div>
        ))}
        </div>
        </div>
        );
}

export default TicketList;