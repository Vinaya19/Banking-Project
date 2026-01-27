import React, { useState } from 'react';
import axios from 'axios';

function Transfer(){
    const [fromAccountId, setFromAccountId] = useState('');
    const [toAccountNumber, setToAccountNumber] = useState('');
    const [amount, setAmount] = useState('');

    const doTransfer = async () => {
        try{
            await axios.post(`/api/accounts/${fromAccountId}/transfer`, {to_account_number: toAccountNumber, amount: parseFloat(amount)})
            alert("Transfer is complete")
        }
        catch{
            alert("Transfer failed: " + (err.response?.data?.message || err.message))
        }
    }

    return (
        <div style={{padding: 30}}>
            <h2>Transfer</h2>
            <input placeholder='From Account ID' value={fromAccountId} onChange={(e) => setFromAccountId(e.target.value)}/>
            <br />
            <input placeholder='To Account Number' value={toAccountNumber} onChange={(e) => setToAccountNumber(e.target.value)}/>
            <br />
            <input placeholder='Amount' value={amount} onChange={(e) => setAmount(e.target.value)}/>
            <br />
            <button onClick={doTransfer}>Send</button>
        </div>
    )
}

export default Transfer;