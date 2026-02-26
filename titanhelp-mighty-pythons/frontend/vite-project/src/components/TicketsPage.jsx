import React from 'react';
import TicketsTable from './TicketsTable';

{/*
const sampleTickets = [
    {
        id: 1,
        name: "Login not working",
        date: "2026-02-22",
        status: "Open",
        priority: "High",
        description: "User reports they cannot log into the syste..."
    },
    {
        id: 1,
        name: "UI bug in dash",
        date: "2026-02-20",
        status: "In progress",
        priority: "Medium",
        description: "Dashboard widgets are overlapping on smaller screens..."
    },
    {
        id: 1,
        name: "Dashboard not loading",
        date: "2026-02-20",
        status: "In progress",
        priority: "Medium",
        description: "Dashboard widgets are overlapping on smaller screens..."
    },
    {
        id: 1,
        name: "UI issue",
        date: "2026-02-20",
        status: "In progress",
        priority: "Medium",
        description: "Dashboard widgets are overlapping on smaller screens..."
    },
    {
        id: 1,
        name: "Page not loading",
        date: "2026-02-20",
        status: "In progress",
        priority: "Medium",
        description: "Dashboard widgets are overlapping on smaller screens..."
    },
    {
        id: 1,
        name: "404 error",
        date: "2026-02-20",
        status: "In progress",
        priority: "Medium",
        description: "Dashboard widgets are overlapping on smaller screens..."
    },
    {
        id: 1,
        name: "Issue with something",
        date: "2026-02-20",
        status: "In progress",
        priority: "Medium",
        description: "Dashboard widgets are overlapping on smaller screens..."
    }
];
*/}


{/* 
    To use sampleTickets above: 
    change TicketsPage = ( tickets ) to TicketsPage = ()
    change tickets = { tickets } to tickets = {sampleTickets}
*/}

const TicketsPage = ( tickets ) => {
    return (
        <div>
            <h1>Tickets</h1>
            <TicketsTable tickets = { tickets } />
        </div>
    );
};

export default TicketsPage;