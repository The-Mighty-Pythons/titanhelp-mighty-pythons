import { useEffect, useState } from "react";
import { getTickets } from "./api/ticketApi";
import TicketForm from "./components/TicketForm";
import TicketsPage from "./components/TicketsPage";
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
    <div className = "app-container">
      <h1>TitanHelp</h1>
      <TicketForm onCreated = {loadTickets} />
      <TicketsPage tickets = {tickets} />

    </div>
  );
}

export default App;