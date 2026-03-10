import React from 'react';
import TicketsTable from './TicketsTable';


const TicketsPage = ( {tickets} ) => {
    return (
        <div>
            <h1>Tickets</h1>
            <TicketsTable tickets = { tickets } />
        </div>
    );
};

export default TicketsPage;