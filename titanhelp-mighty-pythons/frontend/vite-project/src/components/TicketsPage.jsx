import React from 'react';
import TicketsTable from './TicketsTable';


const TicketsPage = ({ tickets, onStatusChange }) => {
    return (
        <div>
            <h1>Tickets</h1>
            <TicketsTable tickets={tickets} onStatusChange={onStatusChange} />
        </div>
    );
};

export default TicketsPage;