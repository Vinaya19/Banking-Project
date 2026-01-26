import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

function Transactions(){
    const { accountId } = useParams();
    const [txns, setTxns] = useState([]);

    useEffect(() => {
        axios.get(`/api/accounts/${accountId}/transactions`).then((r) => setTxns(r.data)).catch(() => {})
    }, [accountId])

    return (
        <div style={{padding: 30}}>
            <h2>Transactions</h2>
            <table>
                <thead>
                    <tr>
                        <th>id</th>
                        <th>type</th>
                        <th>amount</th>
                        <th>desc</th>
                        <th>time</th>
                    </tr>
                </thead>
                <tbody>
                    {txns.map((t) => (
                        <tr key={t.id}>
                            <td>{t.type}</td>
                            <td>{t.amount}</td>
                            <td>{t.description}</td>
                            <td>{t.created_at}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default Transactions;