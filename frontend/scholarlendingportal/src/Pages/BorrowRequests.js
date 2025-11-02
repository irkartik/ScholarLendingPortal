import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function BorrowRequests() {
    const [requests, setRequests] = useState([]);
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [statusFilter, setStatusFilter] = useState('pending');
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

        if (userData.role !== 'staff' && userData.role !== 'admin') {
            navigate('/dashboard');
            return;
        }

        fetchRequests(token);
    }, [navigate, statusFilter]);

    const fetchRequests = async (token) => {
        try {
            let url = '/api/borrow-requests/';
            if (statusFilter) url += `?status=${statusFilter}`;

            const response = await fetch(url, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
            });

            if (response.ok) {
                const data = await response.json();
                setRequests(data);
            }
        } catch (err) {
            console.error('Error fetching requests:', err);
        } finally {
            setLoading(false);
        }
    };

    const handleApprove = async (id) => {
        const token = localStorage.getItem('token');
        try {
            const response = await fetch(`/api/borrow-requests/${id}/approve/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`,
                },
                body: JSON.stringify({ action: 'approve', notes: '' }),
            });

            if (response.ok) {
                setMessage('Request approved!');
                fetchRequests(token);
            } else {
                const data = await response.json();
                setMessage('Error: ' + JSON.stringify(data));
            }
        } catch (err) {
            setMessage('Error approving request');
        }
    };

    const handleReject = async (id) => {
        const reason = prompt('Enter rejection reason:');
        if (!reason) return;

        const token = localStorage.getItem('token');
        try {
            const response = await fetch(`/api/borrow-requests/${id}/reject/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`,
                },
                body: JSON.stringify({ action: 'reject', rejection_reason: reason }),
            });

            if (response.ok) {
                setMessage('Request rejected!');
                fetchRequests(token);
            } else {
                const data = await response.json();
                setMessage('Error: ' + JSON.stringify(data));
            }
        } catch (err) {
            setMessage('Error rejecting request');
        }
    };

    const handleIssue = async (id) => {
        const token = localStorage.getItem('token');
        try {
            const response = await fetch(`/api/borrow-requests/${id}/issue/`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
            });

            if (response.ok) {
                setMessage('Equipment issued!');
                fetchRequests(token);
            } else {
                const data = await response.json();
                setMessage('Error: ' + JSON.stringify(data));
            }
        } catch (err) {
            setMessage('Error issuing equipment');
        }
    };

    const handleReturn = async (id) => {
        const token = localStorage.getItem('token');
        try {
            const response = await fetch(`/api/borrow-requests/${id}/mark_returned/`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
            });

            if (response.ok) {
                setMessage('Equipment returned!');
                fetchRequests(token);
            } else {
                const data = await response.json();
                setMessage('Error: ' + JSON.stringify(data));
            }
        } catch (err) {
            setMessage('Error marking as returned');
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
                <h1>Borrow Requests</h1>

                <div className="filters">
                    <select value={statusFilter} onChange={(e) => setStatusFilter(e.target.value)}>
                        <option value="">All Statuses</option>
                        <option value="pending">Pending</option>
                        <option value="approved">Approved</option>
                        <option value="rejected">Rejected</option>
                        <option value="issued">Issued</option>
                        <option value="returned">Returned</option>
                    </select>
                </div>

                {message && <div className="success">{message}</div>}

                <table>
                    <thead>
                    <tr>
                        <th>User</th>
                        <th>Equipment</th>
                        <th>Quantity</th>
                        <th>From</th>
                        <th>To</th>
                        <th>Status</th>
                        <th>Purpose</th>
                        <th>Actions</th>
                    </tr>
                    </thead>
                    <tbody>
                    {requests.map((req) => (
                        <tr key={req.id}>
                            <td>{req.user_details.username}</td>
                            <td>{req.equipment_details.name}</td>
                            <td>{req.quantity}</td>
                            <td>{req.borrow_from}</td>
                            <td>{req.borrow_to}</td>
                            <td>
                  <span className={`badge badge-${
                      req.status === 'pending' ? 'warning' :
                          req.status === 'approved' ? 'info' :
                              req.status === 'issued' ? 'success' :
                                  req.status === 'returned' ? 'success' : 'danger'
                  }`}>
                    {req.status}
                  </span>
                            </td>
                            <td>{req.purpose}</td>
                            <td>
                                {req.status === 'pending' && (
                                    <>
                                        <button className="btn-success btn-small" onClick={() => handleApprove(req.id)}>
                                            Approve
                                        </button>
                                        <button className="btn-danger btn-small" onClick={() => handleReject(req.id)}>
                                            Reject
                                        </button>
                                    </>
                                )}
                                {req.status === 'approved' && (
                                    <button className="btn-primary btn-small" onClick={() => handleIssue(req.id)}>
                                        Issue
                                    </button>
                                )}
                                {req.status === 'issued' && (
                                    <button className="btn-warning btn-small" onClick={() => handleReturn(req.id)}>
                                        Mark Returned
                                    </button>
                                )}
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default BorrowRequests;

