import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function EquipmentList() {
    const [equipment, setEquipment] = useState([]);
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [search, setSearch] = useState('');
    const [category, setCategory] = useState('');
    const [showModal, setShowModal] = useState(false);
    const [selectedEquipment, setSelectedEquipment] = useState(null);
    const [borrowData, setBorrowData] = useState({
        quantity: 1,
        borrow_from: '',
        borrow_to: '',
        purpose: '',
    });
    const [message, setMessage] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (!token) {
            navigate('/login');
            return;
        }

        const userData = JSON.parse(localStorage.getItem('user'));
        setUser(userData);

        fetchEquipment(token);
    }, [navigate, search, category]);

    const fetchEquipment = async (token) => {
        try {
            let url = '/api/equipment/';
            const params = [];
            if (search) params.push(`search=${search}`);
            if (category) params.push(`category=${category}`);
            if (params.length > 0) url += '?' + params.join('&');

            const response = await fetch(url, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
            });

            if (response.ok) {
                const data = await response.json();
                setEquipment(data);
            }
        } catch (err) {
            console.error('Error fetching equipment:', err);
        } finally {
            setLoading(false);
        }
    };

    const openBorrowModal = (item) => {
        setSelectedEquipment(item);
        setShowModal(true);
        setMessage('');
    };

    const handleBorrowSubmit = async (e) => {
        e.preventDefault();
        const token = localStorage.getItem('token');

        try {
            const response = await fetch('/api/borrow-requests/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`,
                },
                body: JSON.stringify({
                    equipment: selectedEquipment.id,
                    ...borrowData,
                }),
            });

            if (response.ok) {
                setMessage('Borrow request submitted successfully!');
                setShowModal(false);
                setBorrowData({ quantity: 1, borrow_from: '', borrow_to: '', purpose: '' });
            } else {
                const data = await response.json();
                setMessage('Error: ' + JSON.stringify(data));
            }
        } catch (err) {
            setMessage('Error submitting request');
        }
    };

    const handleLogout = () => {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        navigate('/login');
    };

    if (loading) {
        return <div className="loading">Loading...</div>;
    }

    return (
        <div>
            <div className="navbar">
                <h2>Equipment Management System</h2>
                <div>
                    <a href="/dashboard">Dashboard</a>
                    <a href="/equipment">Equipment</a>
                    {user && user.role === 'admin' && (
                        <a href="/equipment-manage">Manage Equipment</a>
                    )}
                    {user && (user.role === 'staff' || user.role === 'admin') && (
                        <>
                            <a href="/borrow-requests">Borrow Requests</a>
                            <a href="/maintenance-logs">Maintenance Logs</a>
                        </>
                    )}
                    <a href="/my-requests">My Requests</a>
                    <button onClick={handleLogout}>Logout</button>
                </div>
            </div>

            <div className="container">
                <h1>Equipment List</h1>

                <div className="filters">
                    <input
                        type="text"
                        placeholder="Search equipment..."
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                    />
                    <select value={category} onChange={(e) => setCategory(e.target.value)}>
                        <option value="">All Categories</option>
                        <option value="sports">Sports Equipment</option>
                        <option value="lab">Lab Equipment</option>
                        <option value="camera">Camera & Photography</option>
                        <option value="musical">Musical Instruments</option>
                        <option value="project">Project Materials</option>
                        <option value="other">Other</option>
                    </select>
                </div>

                {message && <div className="success">{message}</div>}

                <div>
                    {equipment.map((item) => (
                        <div key={item.id} className="equipment-card">
                            <h3>{item.name}</h3>
                            <p><strong>Category:</strong> {item.category}</p>
                            <p><strong>Description:</strong> {item.description}</p>
                            <p><strong>Condition:</strong> {item.condition}</p>
                            <p><strong>Available:</strong> {item.available_quantity} / {item.quantity}</p>
                            {item.is_available && (
                                <button className="btn-success btn-small" onClick={() => openBorrowModal(item)}>
                                    Borrow
                                </button>
                            )}
                            {!item.is_available && (
                                <span className="badge badge-danger">Not Available</span>
                            )}
                        </div>
                    ))}
                </div>

                {showModal && (
                    <div className="modal">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h2>Borrow {selectedEquipment.name}</h2>
                                <button className="close-btn" onClick={() => setShowModal(false)}>×</button>
                            </div>
                            <form onSubmit={handleBorrowSubmit}>
                                <div className="form-group">
                                    <label>Quantity:</label>
                                    <input
                                        type="number"
                                        min="1"
                                        max={selectedEquipment.available_quantity}
                                        value={borrowData.quantity}
                                        onChange={(e) => setBorrowData({...borrowData, quantity: e.target.value})}
                                        required
                                    />
                                </div>
                                <div className="form-group">
                                    <label>Borrow From:</label>
                                    <input
                                        type="date"
                                        value={borrowData.borrow_from}
                                        onChange={(e) => setBorrowData({...borrowData, borrow_from: e.target.value})}
                                        required
                                    />
                                </div>
                                <div className="form-group">
                                    <label>Borrow To:</label>
                                    <input
                                        type="date"
                                        value={borrowData.borrow_to}
                                        onChange={(e) => setBorrowData({...borrowData, borrow_to: e.target.value})}
                                        required
                                    />
                                </div>
                                <div className="form-group">
                                    <label>Purpose:</label>
                                    <textarea
                                        value={borrowData.purpose}
                                        onChange={(e) => setBorrowData({...borrowData, purpose: e.target.value})}
                                        rows="3"
                                    ></textarea>
                                </div>
                                {message && <div className="error">{message}</div>}
                                <button type="submit">Submit Request</button>
                            </form>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}

export default EquipmentList;

