import { useState } from "react";
import { createTicket } from "../api/ticketApi";


function TicketForm({ onCreated }) {
  const [form, setForm] = useState({
    name: "",
    problem_description: "",
    priority: "Medium",
  });

  //client and backend field errors
  const [validationErrors, setValidationErrors] = useState({});

  //unexpected errors (network, 500, etc.)
  const [generalError, setGeneralError] = useState(null);

  //success feedback
  const [success, setSuccess] = useState(false);

  const maxLengths = {
    name: 100,
    problem_description: 1000,
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
    setGeneralError(null);
    setSuccess(false);

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
      setSuccess(true);
      onCreated();
    } catch (err) {
      if (err.errors) {
        setValidationErrors(err.errors);
      } else {
        setGeneralError("Something went wrong. Please try again.");
      }
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
          onChange={(e) => {
            setSuccess(false);
            setForm({ ...form, name: e.target.value });
          }}
        />
        {validationErrors.name && (
          <div className="error">{validationErrors.name}</div>
        )}

        <textarea
          placeholder="Problem Description"
          value={form.problem_description}
          maxLength={maxLengths.problem_description}
          rows={5}
          onChange={(e) => {
            setSuccess(false);
            setForm({ ...form, problem_description: e.target.value });
          }}
        />
        {validationErrors.problem_description && (
          <div className="error">
            {validationErrors.problem_description}
          </div>
        )}

        <select
          value={form.priority}
          onChange={(e) => {
            setSuccess(false);
            setForm({ ...form, priority: e.target.value });
          }}
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

      {generalError && (
        <div className="error">{generalError}</div>
      )}

      {success && (
        <div className="success">Ticket created successfully!</div>
      )}
    </div>
  );
}

export default TicketForm;