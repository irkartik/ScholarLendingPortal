import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function MyRequests() {
  const [requests, setRequests] = useState([]);
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

    fetchRequests(token);
  }, [navigate]);

  const fetchRequests = async (token) => {
    try {
      const response = await fetch('/api/borrow-requests/my_requests/', {
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
            <a href="/borrow-requests">Borrow Requests</a>
          )}
          <a href="/my-requests">My Requests</a>
          <button onClick={handleLogout}>Logout</button>
        </div>
      </div>

      <div className="container">
        <h1>My Borrow Requests</h1>

        <table>
          <thead>
            <tr>
              <th>Equipment</th>
              <th>Quantity</th>
              <th>From</th>
              <th>To</th>
              <th>Status</th>
              <th>Purpose</th>
              <th>Request Date</th>
              <th>Notes</th>
            </tr>
          </thead>
          <tbody>
            {requests.map((req) => (
              <tr key={req.id}>
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
                <td>{new Date(req.request_date).toLocaleDateString()}</td>
                <td>
                  {req.rejection_reason && <p><strong>Rejection:</strong> {req.rejection_reason}</p>}
                  {req.notes && <p>{req.notes}</p>}
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {requests.length === 0 && (
          <p>No borrow requests found. Go to <a href="/equipment">Equipment</a> to make a request.</p>
        )}
      </div>
    </div>
  );
}

export default MyRequests;

