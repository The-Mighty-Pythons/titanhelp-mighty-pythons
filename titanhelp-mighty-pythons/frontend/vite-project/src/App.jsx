import { useEffect, useState } from "react";
import { getTickets, updateTicketStatus } from "./api/ticketApi";
import TicketForm from "./components/TicketForm";
import TicketsPage from "./components/TicketsPage";
import "./App.css";

function App() {
  const [tickets, setTickets] = useState([]);

  async function loadTickets() {
    const data = await getTickets();
    setTickets(data);
  }

  async function handleStatusChange(id, status) {
    await updateTicketStatus(id, status);
    loadTickets();
  }

  useEffect(() => {
    loadTickets();
  }, []);

  return (
    <div className = "app-container">
      <h1>TitanHelp</h1>
      <TicketForm onCreated = {loadTickets} />
      <TicketsPage tickets={tickets} onStatusChange={handleStatusChange} />

    </div>
  );
}

export default App;