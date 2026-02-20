import { useState } from "react";
import { createTicket } from "../api/ticketApi";

function TicketForm({ onCreated }) {
  const [form, setForm] = useState({
    name: "",
    problem_description: "",
    priority: "Medium",
  });
  const [error, setError] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    setError(null);

    try {
      await createTicket(form);
      setForm({ name: "", problem_description: "", priority: "Medium" });
      onCreated(); // refresh list
    } catch (err) {
      setError(err.errors);
    }
  }

  return (
    <div className="ticket-form">
      <h2>Create Ticket</h2>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="Name"
          value={form.name}
          onChange={(e) =>
            setForm({ ...form, name: e.target.value })
          }
        />

        <input
          placeholder="Problem Description"
          value={form.problem_description}
          onChange={(e) =>
            setForm({ ...form, problem_description: e.target.value })
          }
        />

        <select
          value={form.priority}
          onChange={(e) =>
            setForm({ ...form, priority: e.target.value })
          }
        >
          <option>Low</option>
          <option>Medium</option>
          <option>High</option>
        </select>

        <button type="submit">Create</button>
      </form>

      {error && (
        <div className="error">
          {Object.entries(error).map(([key, value]) => (
            <div key={key}>{value}</div>
          ))}
        </div>
      )}
    </div>
  );
}

export default TicketForm;