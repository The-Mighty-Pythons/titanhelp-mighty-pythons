import { useState } from "react";
import { createTicket } from "../api/ticketApi";
import './TicketForm.css';

function TicketForm({ onCreated }) {
  const [form, setForm] = useState({
    name: "",
    problem_description: "",
    priority: "Medium",
  });

  //backend errors
  const [error, setError] = useState(null);

  //client validation errors
  const [validationErrors, setValidationErrors] = useState({});

  const maxLengths = {
    name: 50,
    problem_description: 300,
  };

  function validateForm() {
    const errors = {};

    // Required checks
    if (!form.name.trim()) {
      errors.name = "Name is required";
    } else if (form.name.length > maxLengths.name) {
      errors.name = `Name must be under ${maxLengths.name} characters`;
    }

    if (!form.problem_description.trim()) {
      errors.problem_description = "Problem description is required";
    } else if (
      form.problem_description.length > maxLengths.problem_description
    ) {
      errors.problem_description =
        `Description must be under ${maxLengths.problem_description} characters`;
    }

    // Priority validation
    if (!["Low", "Medium", "High"].includes(form.priority)) {
      errors.priority = "Invalid priority selected";
    }

    setValidationErrors(errors);
    return Object.keys(errors).length === 0;
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setError(null);

    //client validation
    if (!validateForm()) return;

    try {
      await createTicket(form);

      setForm({
        name: "",
        problem_description: "",
        priority: "Medium",
      });

      setValidationErrors({});
      onCreated();
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
          maxLength={maxLengths.name}
          onChange={(e) =>
            setForm({ ...form, name: e.target.value })
          }
        />
        {validationErrors.name && (
          <div className="error">{validationErrors.name}</div>
        )}

        <input
          placeholder="Problem Description"
          value={form.problem_description}
          maxLength={maxLengths.problem_description}
          onChange={(e) =>
            setForm({ ...form, problem_description: e.target.value })
          }
        />
        {validationErrors.problem_description && (
          <div className="error">
            {validationErrors.problem_description}
          </div>
        )}

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

        {validationErrors.priority && (
          <div className="error">{validationErrors.priority}</div>
        )}

        <button type="submit">Create Ticket</button>
      </form>

      {/*backend errors*/}
      {error && (
        <div className="error">
          {Object.entries(error).map(([key, value]) => (
            <div key = {key} > {value}</div>
          ))}
        </div>
      )}
    </div>
  );
}

export default TicketForm;