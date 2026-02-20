import { useEffect, useState } from "react";
import { getTickets } from "./api/ticketApi";
import TicketForm from "./components/TicketForm";
import TicketList from "./components/TicketList";
import "./App.css";

function App() {
  const [tickets, setTickets] = useState([]);

  async function loadTickets() {
    const data = await getTickets();
    setTickets(data);
  }

  useEffect(() => {
    loadTickets();
  }, []);

  return (
    <div className="app-container">
      <h1>TitanHelp</h1>
      <TicketForm onCreated={loadTickets} />
      <TicketList tickets={tickets} />
    </div>
  );
}

export default App;