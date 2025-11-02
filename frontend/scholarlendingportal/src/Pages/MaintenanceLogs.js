import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function MaintenanceLogs() {
    const [logs, setLogs] = useState([]);
    const [equipment, setEquipment] = useState([]);
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [showModal, setShowModal] = useState(false);
    const [formData, setFormData] = useState({
        equipment: '',
        log_type: 'damage',
        description: '',
        cost: '',
    });
    const [message, setMessage] = useState('');
    const [filterEquipment, setFilterEquipment] = useState('');
    const [filterType, setFilterType] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (!token) {
            navigate('/login');
            return;
        }

        const userData = JSON.parse(localStorage.getItem('user'));
        setUser(userData);

        fetchLogs(token);
        fetchEquipment(token);
    }, [navigate]);

    const fetchLogs = async (token, equipmentFilter = '', typeFilter = '') => {
        try {
            let url = '/api/maintenance-logs/';
            const params = [];
            if (equipmentFilter) params.push(`equipment=${equipmentFilter}`);
            if (typeFilter) params.push(`log_type=${typeFilter}`);
            if (params.length > 0) url += '?' + params.join('&');

            const response = await fetch(url, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
            });

            if (response.ok) {
                const data = await response.json();
                setLogs(data);
            }
        } catch (err) {
            console.error('Error fetching logs:', err);
        } finally {
            setLoading(false);
        }
    };

    const fetchEquipment = async (token) => {
        try {
            const response = await fetch('/api/equipment/', {
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
        }
    };

    const handleFilter = () => {
        const token = localStorage.getItem('token');
        fetchLogs(token, filterEquipment, filterType);
    };

    const handleClearFilter = () => {
        setFilterEquipment('');
        setFilterType('');
        const token = localStorage.getItem('token');
        fetchLogs(token);
    };

    const openAddModal = () => {
        setFormData({
            equipment: '',
            log_type: 'damage',
            description: '',
            cost: '',
        });
        setShowModal(true);
        setMessage('');
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const token = localStorage.getItem('token');

        try {
            const submitData = {
                equipment: parseInt(formData.equipment),
                log_type: formData.log_type,
                description: formData.description,
                cost: formData.cost ? parseFloat(formData.cost) : null,
            };

            const response = await fetch('/api/maintenance-logs/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`,
                },
                body: JSON.stringify(submitData),
            });

            if (response.ok) {
                setMessage('Maintenance log added!');
                setShowModal(false);
                fetchLogs(token, filterEquipment, filterType);
            } else {
                const data = await response.json();
                setMessage('Error: ' + JSON.stringify(data));
            }
        } catch (err) {
            setMessage('Error saving log');
        }
    };

    const handleDelete = async (id) => {
        if (!window.confirm('Are you sure you want to delete this log?')) {
            return;
        }

        const token = localStorage.getItem('token');

        try {
            const response = await fetch(`/api/maintenance-logs/${id}/`, {
                method: 'DELETE',
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
            });

            if (response.ok) {
                setMessage('Log deleted!');
                fetchLogs(token, filterEquipment, filterType);
            } else {
                setMessage('Error deleting log');
            }
        } catch (err) {
            setMessage('Error deleting log');
        }
    };

    const handleLogout = () => {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        navigate('/login');
    };

    const formatDate = (dateString) => {
        return new Date(dateString).toLocaleDateString();
    };

    const getLogTypeLabel = (type) => {
        const types = {
            'damage': 'Damage Report',
            'repair': 'Repair',
            'inspection': 'Inspection'
        };
        return types[type] || type;
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
                <h1>Maintenance Logs</h1>

                <div className="filters">
                    <select
                        value={filterEquipment}
                        onChange={(e) => setFilterEquipment(e.target.value)}
                    >
                        <option value="">All Equipment</option>
                        {equipment.map((item) => (
                            <option key={item.id} value={item.id}>{item.name}</option>
                        ))}
                    </select>

                    <select
                        value={filterType}
                        onChange={(e) => setFilterType(e.target.value)}
                    >
                        <option value="">All Types</option>
                        <option value="damage">Damage Report</option>
                        <option value="repair">Repair</option>
                        <option value="inspection">Inspection</option>
                    </select>

                    <button onClick={handleFilter}>Filter</button>
                    <button onClick={handleClearFilter} className="btn-warning">Clear</button>
                    {user && (user.role === 'staff' || user.role === 'admin') && (
                        <button onClick={openAddModal}>Add Log</button>
                    )}
                </div>

                {message && <div className="success">{message}</div>}

                <table>
                    <thead>
                    <tr>
                        <th>Equipment</th>
                        <th>Type</th>
                        <th>Description</th>
                        <th>Reported By</th>
                        <th>Date</th>
                        <th>Cost</th>
                        {user && (user.role === 'staff' || user.role === 'admin') && <th>Actions</th>}
                    </tr>
                    </thead>
                    <tbody>
                    {logs.length === 0 ? (
                        <tr>
                            <td colSpan="7" style={{textAlign: 'center', padding: '2rem', color: 'var(--text-secondary)'}}>No maintenance logs found</td>
                        </tr>
                    ) : (
                        logs.map((log) => (
                            <tr key={log.id}>
                                <td>{log.equipment_details?.name}</td>
                                <td>{getLogTypeLabel(log.log_type)}</td>
                                <td>{log.description}</td>
                                <td>{log.reported_by_details?.username}</td>
                                <td>{formatDate(log.reported_date)}</td>
                                <td>{log.cost ? `$${parseFloat(log.cost).toFixed(2)}` : '-'}</td>
                                {user && (user.role === 'staff' || user.role === 'admin') && (
                                    <td>
                                        <button className="btn-danger btn-small" onClick={() => handleDelete(log.id)}>
                                            Delete
                                        </button>
                                    </td>
                                )}
                            </tr>
                        ))
                    )}
                    </tbody>
                </table>

                {showModal && (
                    <div className="modal">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h2>Add Maintenance Log</h2>
                                <button className="close-btn" onClick={() => setShowModal(false)}>×</button>
                            </div>
                            <form onSubmit={handleSubmit}>
                                <div className="form-group">
                                    <label>Equipment:</label>
                                    <select
                                        value={formData.equipment}
                                        onChange={(e) => setFormData({...formData, equipment: e.target.value})}
                                        required
                                    >
                                        <option value="">Select Equipment</option>
                                        {equipment.map((item) => (
                                            <option key={item.id} value={item.id}>{item.name}</option>
                                        ))}
                                    </select>
                                </div>
                                <div className="form-group">
                                    <label>Log Type:</label>
                                    <select
                                        value={formData.log_type}
                                        onChange={(e) => setFormData({...formData, log_type: e.target.value})}
                                        required
                                    >
                                        <option value="damage">Damage Report</option>
                                        <option value="repair">Repair</option>
                                        <option value="inspection">Inspection</option>
                                    </select>
                                </div>
                                <div className="form-group">
                                    <label>Description:</label>
                                    <textarea
                                        value={formData.description}
                                        onChange={(e) => setFormData({...formData, description: e.target.value})}
                                        rows="4"
                                        required
                                    ></textarea>
                                </div>
                                <div className="form-group">
                                    <label>Cost (optional):</label>
                                    <input
                                        type="number"
                                        step="0.01"
                                        min="0"
                                        value={formData.cost}
                                        onChange={(e) => setFormData({...formData, cost: e.target.value})}
                                        placeholder="0.00"
                                    />
                                </div>
                                {message && <div className="error">{message}</div>}
                                <button type="submit">Add Log</button>
                            </form>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}

export default MaintenanceLogs;

