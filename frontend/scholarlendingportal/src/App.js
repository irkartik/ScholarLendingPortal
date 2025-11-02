import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './Pages/Login';
import Register from './Pages/Register';
import Dashboard from './Pages/Dashboard';
import EquipmentList from './Pages/EquipmentList';
import EquipmentManage from './Pages/EquipmentManage';
import BorrowRequests from './Pages/BorrowRequests';
import MyRequests from './Pages/MyRequests';
import MaintenanceLogs from './Pages/MaintenanceLogs';

import './App.css';

function App() {
    return (
        <BrowserRouter>
            <div className="App">
                <Routes>
                    <Route path="/" element={<Login />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/dashboard" element={<Dashboard />} />
                    <Route path="/equipment" element={<EquipmentList />} />
                    <Route path="/equipment-manage" element={<EquipmentManage />} />
                    <Route path="/borrow-requests" element={<BorrowRequests />} />
                    <Route path="/my-requests" element={<MyRequests />} />
                    <Route path="/maintenance-logs" element={<MaintenanceLogs />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;

