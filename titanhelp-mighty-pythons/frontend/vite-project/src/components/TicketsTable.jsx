import React, { useState } from "react";
import './TicketsTable.css';

const TicketsTable = ({ tickets = [] }) => {
    const [currentPage, setCurrentPage] = useState(1);
    const ticketsPerPage = 5;
    
    if (!tickets.length) {
        return <p>No Tickets</p>;
    }

    //calculate tickets for current page
    const startIndex = (currentPage -1) * ticketsPerPage;
    const currentTickets = tickets.slice(
        startIndex, 
        startIndex + ticketsPerPage
    );


    return (
        <div className="tickets-table-container">
            <table className="tickets-table">
                <thead>
                    <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Status</th>
                    <th>Priority</th>
                    <th>Description</th>
                    </tr>
                </thead>
                <tbody>
                    {currentTickets.map((ticket) => (
                        <tr key={ticket.id}>
                            <td>{ticket.name}</td>
                            <td>{ticket.date 
                                ? new Date(ticket.date).toLocaleDateString() 
                                : ""}
                                </td>
                            <td>{ticket.status}</td>
                            <td>{ticket.priority}</td>
                            <td>
                                {ticket.problem_description.length > 50
                                ? ticket.problem_description.substring(0, 50) + "..."
                                : ticket.problem_description}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            {/* pagination buttons */}
            <div className="pagination">
                <button
                    onClick={() => setCurrentPage((p) => p - 1)}
                    disabled={currentPage === 1}
                >
                    Previous
                </button>
                <button
                    onClick={() => setCurrentPage((p) => p + 1)}
                    disabled={startIndex + ticketsPerPage >= tickets.length}
                >
                    Next
                </button>
            </div>
        </div>
    );
};

export default TicketsTable;