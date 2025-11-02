import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function Dashboard() {
    const [stats, setStats] = useState(null);
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (!token) {
            navigate('/login');
            return;
        }

        const userData = JSON.parse(localStorage.getItem('user'));
        setUser(userData);

        fetchStats(token);
    }, [navigate]);

    const fetchStats = async (token) => {
        try {
            const response = await fetch('/api/dashboard/stats/', {
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
            });

            if (response.ok) {
                const data = await response.json();
                setStats(data);
            } else {
                navigate('/login');
            }
        } catch (err) {
            console.error('Error fetching stats:', err);
        } finally {
            setLoading(false);
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
                <h1>Dashboard</h1>
                {user && <h3>Welcome, {user.username} ({user.role})</h3>}

                {stats && (
                    <div className="stats-grid">
                        <div className="stat-card">
                            <h3>{stats.total_equipment}</h3>
                            <p>Total Equipment</p>
                        </div>
                        <div className="stat-card">
                            <h3>{stats.available_equipment}</h3>
                            <p>Available Equipment</p>
                        </div>
                        {user && user.role === 'student' && (
                            <>
                                <div className="stat-card">
                                    <h3>{stats.my_requests}</h3>
                                    <p>My Total Requests</p>
                                </div>
                                <div className="stat-card">
                                    <h3>{stats.my_pending}</h3>
                                    <p>Pending Requests</p>
                                </div>
                                <div className="stat-card">
                                    <h3>{stats.my_issued}</h3>
                                    <p>Currently Borrowed</p>
                                </div>
                            </>
                        )}
                        {user && (user.role === 'staff' || user.role === 'admin') && (
                            <>
                                <div className="stat-card">
                                    <h3>{stats.pending_requests}</h3>
                                    <p>Pending Approvals</p>
                                </div>
                                <div className="stat-card">
                                    <h3>{stats.approved_requests}</h3>
                                    <p>Approved Requests</p>
                                </div>
                                <div className="stat-card">
                                    <h3>{stats.issued_requests}</h3>
                                    <p>Currently Issued</p>
                                </div>
                            </>
                        )}
                    </div>
                )}
            </div>
        </div>
    );
}

export default Dashboard;

