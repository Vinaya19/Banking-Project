import React, { useState, useEffect } from 'react';
import { useLocation, Link } from 'react-router-dom';
import axios from 'axios';

function Dashboard(){
    const [accounts, setAccounts] = useState([]);
    const { state } = useLocation();
    const customer = state?.customer;

    useEffect(() => {
        if(!customer) return;

        axios.get(`/api/customers/${customer.id}/accounts`).then(r => setAccounts(r.data)).catch((error) => console.error(error))
    }, [customer]);

    return (
        <div style={{padding: 30}}>
            <h2>Welcome {customer?.name || 'Guest'}</h2>
            <Link to='/transfer'>Go to Transfer</Link>
            <div>
                <h3>Your accounts</h3>
                {accounts.length === 0 && <div>No accounts found. Create one from the API or seed data.</div>}
                <ul>
                    {accounts.map((a) => (
                        <li key={a.id}>
                            {a.account_number} - Balance: {a.balance}
                            <br />
                            <Link to={`/transactions/${a.id}`}>Transactions</Link>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default Dashboard;