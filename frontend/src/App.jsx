import { React, useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './screens/Login';
import Dashboard from './screens/Dashboard';
import Transfer from './screens/Transfer';
import Transactions from './screens/Transactions';

function App() {
  return(
    <BrowserRouter>
    <Routes>
      <Route path='/' element={<Login/>} />
      <Route path='/dashboard' element={<Dashboard/>} />
      <Route path='/transfer' element={<Transfer/>} />
      <Route path='/transactions/:accountId' element={<Transactions/>} />
    </Routes>
    </BrowserRouter>
  ); 
}

export default App
