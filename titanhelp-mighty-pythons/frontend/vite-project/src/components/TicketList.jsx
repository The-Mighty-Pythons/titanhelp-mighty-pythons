function TicketList({ tickets }) {
  return (
    <div className="ticket-list">
      <h2>All Tickets</h2>
      <ul>
        {tickets.map((ticket) => (
          <li key={ticket.id}>
            <strong>{ticket.name}</strong> —{" "}
            {ticket.problem_description} (
            {ticket.priority}) [{ticket.status}]
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TicketList;