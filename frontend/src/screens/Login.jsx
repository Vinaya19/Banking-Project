import {React, useState} from 'react';
import {useNavigate} from 'react-router-dom';
import axios from 'axios';

function Login(){
    const [email, setEmail] = useState("");
    const navigate = useNavigate();

    const handleLogin = async() => {
        try{
            const res = await axios.post('/api/auth/login', {name: email.split('@')[0] || 'User', email});
            const customer = res.data;
            navigate('/dashboard', { state: { customer } })
        }
        catch(err){
            console.error(err);
            alert("Error logging in");
        }
    }

    return (
        <div style={{padding:100}}>
            <h2>Login</h2>
            <input placeholder="Enter your email" value={email} onChange={event => setEmail(event.target.value)}></input>
            <br />
            <button onClick={handleLogin}>Login</button>
        </div>
    );
}

export default Login;