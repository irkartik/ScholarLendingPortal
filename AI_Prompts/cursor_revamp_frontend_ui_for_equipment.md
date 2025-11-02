# Revamp frontend UI for equipment management
_Exported on 02/11/2025 at 22:32:26 GMT+5:30 from Cursor (1.7.52)_

---

**User**

You're an expert Fullstack developer having experience with Django for backend and React for frontend. This project is a School's Equipment Management System which is used to keep track of and handle the borowing lifecycle of each equipments. 

However, the current UI is quite dull without many responsive elements. Can you help me revamp its frontend UI to ensure its more user friendly. Please keep the codechanges at minimal and do not introduce any unwanted code. 

---

**Cursor**

I'll help you revamp the frontend UI to make it more user-friendly and responsive! Let me start by examining the current frontend structure and then make targeted improvements.

Now I understand the current structure. The application has basic styling with no modern UI elements. Let me revamp the frontend with a clean, modern, and responsive design while keeping code changes minimal.

```css
:root {
  --primary-color: #2563eb;
  --primary-dark: #1e40af;
  --primary-light: #3b82f6;
  --secondary-color: #10b981;
  --danger-color: #ef4444;
  --warning-color: #f59e0b;
  --info-color: #06b6d4;
  --dark-bg: #1f2937;
  --light-bg: #f9fafb;
  --card-bg: #ffffff;
  --border-color: #e5e7eb;
  --text-primary: #111827;
  --text-secondary: #6b7280;
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: var(--light-bg);
  color: var(--text-primary);
  line-height: 1.6;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}

```

```css
.App {
  min-height: 100vh;
}

/* Navbar Styles */
.navbar {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: var(--shadow-md);
  flex-wrap: wrap;
  gap: 1rem;
}

.navbar h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
}

.navbar > div {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.navbar a {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: all 0.2s;
  font-weight: 500;
}

.navbar a:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-1px);
}

.navbar button {
  background-color: rgba(239, 68, 68, 0.9);
  color: white;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 600;
}

.navbar button:hover {
  background-color: rgba(239, 68, 68, 1);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Container */
.container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

/* Auth Container */
.auth-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary-color) 50%, var(--primary-dark) 100%);
  padding: 2rem;
}

.auth-container h2 {
  color: white;
  font-size: 2.5rem;
  margin-bottom: 2rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.auth-container form {
  background: var(--card-bg);
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-xl);
  width: 100%;
  max-width: 450px;
}

.auth-container p {
  color: white;
  margin-top: 1.5rem;
  font-size: 1rem;
}

.auth-container p a {
  color: white;
  font-weight: 700;
  text-decoration: underline;
}

/* Form Styles */
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--text-primary);
  font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 80px;
}

/* Button Styles */
button,
.btn {
  background-color: var(--primary-color);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.2s;
  box-shadow: var(--shadow-sm);
}

button:hover,
.btn:hover {
  background-color: var(--primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.btn-success {
  background-color: var(--secondary-color);
}

.btn-success:hover {
  background-color: #059669;
}

.btn-danger {
  background-color: var(--danger-color);
}

.btn-danger:hover {
  background-color: #dc2626;
}

.btn-warning {
  background-color: var(--warning-color);
}

.btn-warning:hover {
  background-color: #d97706;
}

.btn-small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  margin: 0 0.25rem;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.stat-card {
  background: var(--card-bg);
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-md);
  text-align: center;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.stat-card h3 {
  font-size: 2.5rem;
  margin: 0;
  color: var(--primary-color);
  font-weight: 800;
}

.stat-card p {
  margin: 0.5rem 0 0 0;
  color: var(--text-secondary);
  font-weight: 600;
  font-size: 1rem;
}

/* Equipment Card */
.equipment-card {
  background: var(--card-bg);
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: var(--shadow-sm);
  margin-bottom: 1.25rem;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.equipment-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.equipment-card h3 {
  margin-top: 0;
  color: var(--primary-color);
  font-size: 1.5rem;
}

.equipment-card p {
  margin: 0.5rem 0;
  color: var(--text-secondary);
}

.equipment-card p strong {
  color: var(--text-primary);
}

/* Filters */
.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.filters input,
.filters select {
  flex: 1;
  min-width: 200px;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
}

.filters input:focus,
.filters select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

/* Table Styles */
table {
  width: 100%;
  border-collapse: collapse;
  background: var(--card-bg);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow-md);
  margin-top: 1.5rem;
}

thead {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
}

th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.875rem;
  letter-spacing: 0.05em;
}

td {
  padding: 1rem;
  border-bottom: 1px solid var(--border-color);
}

tbody tr {
  transition: background-color 0.2s;
}

tbody tr:hover {
  background-color: var(--light-bg);
}

tbody tr:last-child td {
  border-bottom: none;
}

/* Modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: var(--card-bg);
  border-radius: 1rem;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-xl);
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 2px solid var(--border-color);
}

.modal-header h2 {
  margin: 0;
  color: var(--primary-color);
  font-size: 1.75rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: var(--text-secondary);
  padding: 0;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.5rem;
  transition: all 0.2s;
}

.close-btn:hover {
  background-color: var(--light-bg);
  color: var(--danger-color);
  transform: none;
}

.modal-content form {
  padding: 1.5rem;
}

/* Badges */
.badge {
  display: inline-block;
  padding: 0.375rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 600;
}

.badge-success {
  background-color: #d1fae5;
  color: #065f46;
}

.badge-warning {
  background-color: #fef3c7;
  color: #92400e;
}

.badge-danger {
  background-color: #fee2e2;
  color: #991b1b;
}

.badge-info {
  background-color: #cffafe;
  color: #164e63;
}

/* Messages */
.error,
.success {
  padding: 1rem;
  border-radius: 0.5rem;
  margin: 1rem 0;
  font-weight: 500;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.error {
  background-color: #fee2e2;
  color: #991b1b;
  border-left: 4px solid var(--danger-color);
}

.success {
  background-color: #d1fae5;
  color: #065f46;
  border-left: 4px solid var(--secondary-color);
}

/* Loading */
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  font-size: 1.5rem;
  color: var(--primary-color);
  font-weight: 600;
}

.loading::after {
  content: '';
  width: 2rem;
  height: 2rem;
  margin-left: 1rem;
  border: 3px solid var(--border-color);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
    flex-direction: column;
    align-items: flex-start;
  }

  .navbar h2 {
    font-size: 1.25rem;
  }

  .navbar > div {
    width: 100%;
    justify-content: flex-start;
  }

  .container {
    padding: 0 1rem;
    margin: 1rem auto;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .filters {
    flex-direction: column;
  }

  .filters input,
  .filters select {
    width: 100%;
    min-width: unset;
  }

  .auth-container form {
    padding: 1.5rem;
  }

  table {
    font-size: 0.875rem;
  }

  th,
  td {
    padding: 0.75rem 0.5rem;
  }

  .modal-content {
    margin: 1rem;
  }
}

@media (max-width: 480px) {
  .navbar a,
  .navbar button {
    font-size: 0.875rem;
    padding: 0.5rem 0.75rem;
  }

  .stat-card h3 {
    font-size: 2rem;
  }

  table {
    display: block;
    overflow-x: auto;
  }
}

```

Perfect! Now let me check the remaining pages and make any small adjustments if needed:

Now let me make a few small adjustments to ensure everything looks perfect:

```javascript
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
                <td colSpan="7" style={{ textAlign: 'center' }}>No maintenance logs found</td>
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


```

```javascript
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


```

```css
.App {
  min-height: 100vh;
}

/* Navbar Styles */
.navbar {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: var(--shadow-md);
  flex-wrap: wrap;
  gap: 1rem;
}

.navbar h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
}

.navbar > div {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.navbar a {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: all 0.2s;
  font-weight: 500;
}

.navbar a:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-1px);
}

.navbar button {
  background-color: rgba(239, 68, 68, 0.9);
  color: white;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 600;
}

.navbar button:hover {
  background-color: rgba(239, 68, 68, 1);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Container */
.container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

/* Auth Container */
.auth-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary-color) 50%, var(--primary-dark) 100%);
  padding: 2rem;
}

.auth-container h2 {
  color: white;
  font-size: 2.5rem;
  margin-bottom: 2rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.auth-container form {
  background: var(--card-bg);
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-xl);
  width: 100%;
  max-width: 450px;
}

.auth-container p {
  color: white;
  margin-top: 1.5rem;
  font-size: 1rem;
}

.auth-container p a {
  color: white;
  font-weight: 700;
  text-decoration: underline;
}

/* Form Styles */
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--text-primary);
  font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 80px;
}

/* Button Styles */
button,
.btn {
  background-color: var(--primary-color);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.2s;
  box-shadow: var(--shadow-sm);
}

button:hover,
.btn:hover {
  background-color: var(--primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.btn-success {
  background-color: var(--secondary-color);
}

.btn-success:hover {
  background-color: #059669;
}

.btn-danger {
  background-color: var(--danger-color);
}

.btn-danger:hover {
  background-color: #dc2626;
}

.btn-warning {
  background-color: var(--warning-color);
}

.btn-warning:hover {
  background-color: #d97706;
}

.btn-primary {
  background-color: var(--primary-color);
}

.btn-primary:hover {
  background-color: var(--primary-dark);
}

.btn-small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  margin: 0 0.25rem;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.stat-card {
  background: var(--card-bg);
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-md);
  text-align: center;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.stat-card h3 {
  font-size: 2.5rem;
  margin: 0;
  color: var(--primary-color);
  font-weight: 800;
}

.stat-card p {
  margin: 0.5rem 0 0 0;
  color: var(--text-secondary);
  font-weight: 600;
  font-size: 1rem;
}

/* Equipment Card */
.equipment-card {
  background: var(--card-bg);
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: var(--shadow-sm);
  margin-bottom: 1.25rem;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.equipment-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.equipment-card h3 {
  margin-top: 0;
  color: var(--primary-color);
  font-size: 1.5rem;
}

.equipment-card p {
  margin: 0.5rem 0;
  color: var(--text-secondary);
}

.equipment-card p strong {
  color: var(--text-primary);
}

/* Filters */
.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.filters input,
.filters select {
  flex: 1;
  min-width: 200px;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
}

.filters input:focus,
.filters select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

/* Table Styles */
table {
  width: 100%;
  border-collapse: collapse;
  background: var(--card-bg);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow-md);
  margin-top: 1.5rem;
}

thead {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
}

th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.875rem;
  letter-spacing: 0.05em;
}

td {
  padding: 1rem;
  border-bottom: 1px solid var(--border-color);
}

tbody tr {
  transition: background-color 0.2s;
}

tbody tr:hover {
  background-color: var(--light-bg);
}

tbody tr:last-child td {
  border-bottom: none;
}

/* Modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: var(--card-bg);
  border-radius: 1rem;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-xl);
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 2px solid var(--border-color);
}

.modal-header h2 {
  margin: 0;
  color: var(--primary-color);
  font-size: 1.75rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: var(--text-secondary);
  padding: 0;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.5rem;
  transition: all 0.2s;
}

.close-btn:hover {
  background-color: var(--light-bg);
  color: var(--danger-color);
  transform: none;
}

.modal-content form {
  padding: 1.5rem;
}

/* Badges */
.badge {
  display: inline-block;
  padding: 0.375rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 600;
}

.badge-success {
  background-color: #d1fae5;
  color: #065f46;
}

.badge-warning {
  background-color: #fef3c7;
  color: #92400e;
}

.badge-danger {
  background-color: #fee2e2;
  color: #991b1b;
}

.badge-info {
  background-color: #cffafe;
  color: #164e63;
}

/* Messages */
.error,
.success {
  padding: 1rem;
  border-radius: 0.5rem;
  margin: 1rem 0;
  font-weight: 500;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.error {
  background-color: #fee2e2;
  color: #991b1b;
  border-left: 4px solid var(--danger-color);
}

.success {
  background-color: #d1fae5;
  color: #065f46;
  border-left: 4px solid var(--secondary-color);
}

/* Loading */
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  font-size: 1.5rem;
  color: var(--primary-color);
  font-weight: 600;
}

.loading::after {
  content: '';
  width: 2rem;
  height: 2rem;
  margin-left: 1rem;
  border: 3px solid var(--border-color);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
    flex-direction: column;
    align-items: flex-start;
  }

  .navbar h2 {
    font-size: 1.25rem;
  }

  .navbar > div {
    width: 100%;
    justify-content: flex-start;
  }

  .container {
    padding: 0 1rem;
    margin: 1rem auto;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .filters {
    flex-direction: column;
  }

  .filters input,
  .filters select {
    width: 100%;
    min-width: unset;
  }

  .auth-container form {
    padding: 1.5rem;
  }

  table {
    font-size: 0.875rem;
  }

  th,
  td {
    padding: 0.75rem 0.5rem;
  }

  .modal-content {
    margin: 1rem;
  }
}

@media (max-width: 480px) {
  .navbar a,
  .navbar button {
    font-size: 0.875rem;
    padding: 0.5rem 0.75rem;
  }

  .stat-card h3 {
    font-size: 2rem;
  }

  table {
    display: block;
    overflow-x: auto;
  }
}

```

Perfect! Let me make one more small improvement to the MyRequests page for a better empty state:

```javascript
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
          <div style={{textAlign: 'center', padding: '3rem', background: 'var(--card-bg)', borderRadius: '0.75rem', marginTop: '2rem'}}>
            <p style={{fontSize: '1.125rem', color: 'var(--text-secondary)'}}>No borrow requests found. Go to <a href="/equipment" style={{color: 'var(--primary-color)', fontWeight: '600'}}>Equipment</a> to make a request.</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default MyRequests;


```

Now let me add a few more finishing touches to make the UI even more polished:

```css
.App {
  min-height: 100vh;
}

/* Navbar Styles */
.navbar {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: var(--shadow-md);
  flex-wrap: wrap;
  gap: 1rem;
}

.navbar h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
}

.navbar > div {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.navbar a {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: all 0.2s;
  font-weight: 500;
}

.navbar a:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-1px);
}

.navbar button {
  background-color: rgba(239, 68, 68, 0.9);
  color: white;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 600;
}

.navbar button:hover {
  background-color: rgba(239, 68, 68, 1);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Container */
.container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

.container h1 {
  color: var(--text-primary);
  font-size: 2rem;
  margin-bottom: 0.5rem;
  font-weight: 700;
}

.container h3 {
  color: var(--text-secondary);
  font-weight: 400;
  margin-bottom: 1.5rem;
}

/* Auth Container */
.auth-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary-color) 50%, var(--primary-dark) 100%);
  padding: 2rem;
}

.auth-container h2 {
  color: white;
  font-size: 2.5rem;
  margin-bottom: 2rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.auth-container form {
  background: var(--card-bg);
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-xl);
  width: 100%;
  max-width: 450px;
}

.auth-container p {
  color: white;
  margin-top: 1.5rem;
  font-size: 1rem;
}

.auth-container p a {
  color: white;
  font-weight: 700;
  text-decoration: underline;
}

/* Form Styles */
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--text-primary);
  font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 80px;
}

/* Button Styles */
button,
.btn {
  background-color: var(--primary-color);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.2s;
  box-shadow: var(--shadow-sm);
}

button:hover,
.btn:hover {
  background-color: var(--primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.btn-success {
  background-color: var(--secondary-color);
}

.btn-success:hover {
  background-color: #059669;
}

.btn-danger {
  background-color: var(--danger-color);
}

.btn-danger:hover {
  background-color: #dc2626;
}

.btn-warning {
  background-color: var(--warning-color);
}

.btn-warning:hover {
  background-color: #d97706;
}

.btn-primary {
  background-color: var(--primary-color);
}

.btn-primary:hover {
  background-color: var(--primary-dark);
}

.btn-small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  margin: 0 0.25rem;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.stat-card {
  background: var(--card-bg);
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-md);
  text-align: center;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.stat-card h3 {
  font-size: 2.5rem;
  margin: 0;
  color: var(--primary-color);
  font-weight: 800;
}

.stat-card p {
  margin: 0.5rem 0 0 0;
  color: var(--text-secondary);
  font-weight: 600;
  font-size: 1rem;
}

/* Equipment Card */
.equipment-card {
  background: var(--card-bg);
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: var(--shadow-sm);
  margin-bottom: 1.25rem;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.equipment-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.equipment-card h3 {
  margin-top: 0;
  color: var(--primary-color);
  font-size: 1.5rem;
}

.equipment-card p {
  margin: 0.5rem 0;
  color: var(--text-secondary);
}

.equipment-card p strong {
  color: var(--text-primary);
}

/* Filters */
.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.filters input,
.filters select {
  flex: 1;
  min-width: 200px;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
}

.filters input:focus,
.filters select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

/* Table Styles */
table {
  width: 100%;
  border-collapse: collapse;
  background: var(--card-bg);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow-md);
  margin-top: 1.5rem;
}

thead {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
}

th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.875rem;
  letter-spacing: 0.05em;
}

td {
  padding: 1rem;
  border-bottom: 1px solid var(--border-color);
}

tbody tr {
  transition: background-color 0.2s;
}

tbody tr:hover {
  background-color: var(--light-bg);
}

tbody tr:last-child td {
  border-bottom: none;
}

/* Modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: var(--card-bg);
  border-radius: 1rem;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-xl);
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 2px solid var(--border-color);
}

.modal-header h2 {
  margin: 0;
  color: var(--primary-color);
  font-size: 1.75rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: var(--text-secondary);
  padding: 0;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.5rem;
  transition: all 0.2s;
}

.close-btn:hover {
  background-color: var(--light-bg);
  color: var(--danger-color);
  transform: none;
}

.modal-content form {
  padding: 1.5rem;
}

/* Badges */
.badge {
  display: inline-block;
  padding: 0.375rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 600;
}

.badge-success {
  background-color: #d1fae5;
  color: #065f46;
}

.badge-warning {
  background-color: #fef3c7;
  color: #92400e;
}

.badge-danger {
  background-color: #fee2e2;
  color: #991b1b;
}

.badge-info {
  background-color: #cffafe;
  color: #164e63;
}

/* Messages */
.error,
.success {
  padding: 1rem;
  border-radius: 0.5rem;
  margin: 1rem 0;
  font-weight: 500;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.error {
  background-color: #fee2e2;
  color: #991b1b;
  border-left: 4px solid var(--danger-color);
}

.success {
  background-color: #d1fae5;
  color: #065f46;
  border-left: 4px solid var(--secondary-color);
}

/* Loading */
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  font-size: 1.5rem;
  color: var(--primary-color);
  font-weight: 600;
}

.loading::after {
  content: '';
  width: 2rem;
  height: 2rem;
  margin-left: 1rem;
  border: 3px solid var(--border-color);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
    flex-direction: column;
    align-items: flex-start;
  }

  .navbar h2 {
    font-size: 1.25rem;
  }

  .navbar > div {
    width: 100%;
    justify-content: flex-start;
  }

  .container {
    padding: 0 1rem;
    margin: 1rem auto;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .filters {
    flex-direction: column;
  }

  .filters input,
  .filters select {
    width: 100%;
    min-width: unset;
  }

  .auth-container form {
    padding: 1.5rem;
  }

  table {
    font-size: 0.875rem;
  }

  th,
  td {
    padding: 0.75rem 0.5rem;
  }

  .modal-content {
    margin: 1rem;
  }
}

@media (max-width: 480px) {
  .navbar a,
  .navbar button {
    font-size: 0.875rem;
    padding: 0.5rem 0.75rem;
  }

  .stat-card h3 {
    font-size: 2rem;
  }

  table {
    display: block;
    overflow-x: auto;
  }
}

```

```css
.App {
  min-height: 100vh;
}

/* Navbar Styles */
.navbar {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: var(--shadow-md);
  flex-wrap: wrap;
  gap: 1rem;
}

.navbar h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
}

.navbar > div {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.navbar a {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: all 0.2s;
  font-weight: 500;
}

.navbar a:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-1px);
}

.navbar button {
  background-color: rgba(239, 68, 68, 0.9);
  color: white;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 600;
}

.navbar button:hover {
  background-color: rgba(239, 68, 68, 1);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Container */
.container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

.container h1 {
  color: var(--text-primary);
  font-size: 2rem;
  margin-bottom: 0.5rem;
  font-weight: 700;
}

.container h3 {
  color: var(--text-secondary);
  font-weight: 400;
  margin-bottom: 1.5rem;
}

/* Auth Container */
.auth-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary-color) 50%, var(--primary-dark) 100%);
  padding: 2rem;
}

.auth-container h2 {
  color: white;
  font-size: 2.5rem;
  margin-bottom: 2rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.auth-container form {
  background: var(--card-bg);
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-xl);
  width: 100%;
  max-width: 450px;
}

.auth-container p {
  color: white;
  margin-top: 1.5rem;
  font-size: 1rem;
}

.auth-container p a {
  color: white;
  font-weight: 700;
  text-decoration: underline;
}

/* Form Styles */
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--text-primary);
  font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 80px;
}

/* Button Styles */
button,
.btn {
  background-color: var(--primary-color);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.2s;
  box-shadow: var(--shadow-sm);
  font-family: inherit;
}

button:hover,
.btn:hover {
  background-color: var(--primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

button:active,
.btn:active {
  transform: translateY(0);
}

.btn-success {
  background-color: var(--secondary-color);
}

.btn-success:hover {
  background-color: #059669;
}

.btn-danger {
  background-color: var(--danger-color);
}

.btn-danger:hover {
  background-color: #dc2626;
}

.btn-warning {
  background-color: var(--warning-color);
}

.btn-warning:hover {
  background-color: #d97706;
}

.btn-primary {
  background-color: var(--primary-color);
}

.btn-primary:hover {
  background-color: var(--primary-dark);
}

.btn-small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  margin: 0 0.25rem;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.stat-card {
  background: var(--card-bg);
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-md);
  text-align: center;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.stat-card h3 {
  font-size: 2.5rem;
  margin: 0;
  color: var(--primary-color);
  font-weight: 800;
}

.stat-card p {
  margin: 0.5rem 0 0 0;
  color: var(--text-secondary);
  font-weight: 600;
  font-size: 1rem;
}

/* Equipment Card */
.equipment-card {
  background: var(--card-bg);
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: var(--shadow-sm);
  margin-bottom: 1.25rem;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.equipment-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.equipment-card h3 {
  margin-top: 0;
  color: var(--primary-color);
  font-size: 1.5rem;
}

.equipment-card p {
  margin: 0.5rem 0;
  color: var(--text-secondary);
}

.equipment-card p strong {
  color: var(--text-primary);
}

/* Filters */
.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.filters input,
.filters select {
  flex: 1;
  min-width: 200px;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
}

.filters input:focus,
.filters select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

/* Table Styles */
table {
  width: 100%;
  border-collapse: collapse;
  background: var(--card-bg);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow-md);
  margin-top: 1.5rem;
}

thead {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
}

th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.875rem;
  letter-spacing: 0.05em;
}

td {
  padding: 1rem;
  border-bottom: 1px solid var(--border-color);
}

tbody tr {
  transition: background-color 0.2s;
}

tbody tr:hover {
  background-color: var(--light-bg);
}

tbody tr:last-child td {
  border-bottom: none;
}

/* Modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: var(--card-bg);
  border-radius: 1rem;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-xl);
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 2px solid var(--border-color);
}

.modal-header h2 {
  margin: 0;
  color: var(--primary-color);
  font-size: 1.75rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: var(--text-secondary);
  padding: 0;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.5rem;
  transition: all 0.2s;
}

.close-btn:hover {
  background-color: var(--light-bg);
  color: var(--danger-color);
  transform: none;
}

.modal-content form {
  padding: 1.5rem;
}

/* Badges */
.badge {
  display: inline-block;
  padding: 0.375rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 600;
}

.badge-success {
  background-color: #d1fae5;
  color: #065f46;
}

.badge-warning {
  background-color: #fef3c7;
  color: #92400e;
}

.badge-danger {
  background-color: #fee2e2;
  color: #991b1b;
}

.badge-info {
  background-color: #cffafe;
  color: #164e63;
}

/* Messages */
.error,
.success {
  padding: 1rem;
  border-radius: 0.5rem;
  margin: 1rem 0;
  font-weight: 500;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.error {
  background-color: #fee2e2;
  color: #991b1b;
  border-left: 4px solid var(--danger-color);
}

.success {
  background-color: #d1fae5;
  color: #065f46;
  border-left: 4px solid var(--secondary-color);
}

/* Loading */
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  font-size: 1.5rem;
  color: var(--primary-color);
  font-weight: 600;
}

.loading::after {
  content: '';
  width: 2rem;
  height: 2rem;
  margin-left: 1rem;
  border: 3px solid var(--border-color);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
    flex-direction: column;
    align-items: flex-start;
  }

  .navbar h2 {
    font-size: 1.25rem;
  }

  .navbar > div {
    width: 100%;
    justify-content: flex-start;
  }

  .container {
    padding: 0 1rem;
    margin: 1rem auto;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .filters {
    flex-direction: column;
  }

  .filters input,
  .filters select {
    width: 100%;
    min-width: unset;
  }

  .auth-container form {
    padding: 1.5rem;
  }

  table {
    font-size: 0.875rem;
  }

  th,
  td {
    padding: 0.75rem 0.5rem;
  }

  .modal-content {
    margin: 1rem;
  }
}

@media (max-width: 480px) {
  .navbar a,
  .navbar button {
    font-size: 0.875rem;
    padding: 0.5rem 0.75rem;
  }

  .stat-card h3 {
    font-size: 2rem;
  }

  table {
    display: block;
    overflow-x: auto;
  }
}

```

```css
.App {
  min-height: 100vh;
}

/* Navbar Styles */
.navbar {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: var(--shadow-md);
  flex-wrap: wrap;
  gap: 1rem;
}

.navbar h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
}

.navbar > div {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.navbar a {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: all 0.2s;
  font-weight: 500;
}

.navbar a:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-1px);
}

.navbar button {
  background-color: rgba(239, 68, 68, 0.9);
  color: white;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 600;
}

.navbar button:hover {
  background-color: rgba(239, 68, 68, 1);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Container */
.container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

.container h1 {
  color: var(--text-primary);
  font-size: 2rem;
  margin-bottom: 0.5rem;
  font-weight: 700;
}

.container h3 {
  color: var(--text-secondary);
  font-weight: 400;
  margin-bottom: 1.5rem;
}

/* Auth Container */
.auth-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary-color) 50%, var(--primary-dark) 100%);
  padding: 2rem;
}

.auth-container h2 {
  color: white;
  font-size: 2.5rem;
  margin-bottom: 2rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.auth-container form {
  background: var(--card-bg);
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-xl);
  width: 100%;
  max-width: 450px;
}

.auth-container p {
  color: white;
  margin-top: 1.5rem;
  font-size: 1rem;
}

.auth-container p a {
  color: white;
  font-weight: 700;
  text-decoration: underline;
}

/* Form Styles */
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--text-primary);
  font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 80px;
}

/* Button Styles */
button,
.btn {
  background-color: var(--primary-color);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.2s;
  box-shadow: var(--shadow-sm);
  font-family: inherit;
}

button:hover,
.btn:hover {
  background-color: var(--primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

button:active,
.btn:active {
  transform: translateY(0);
}

.btn-success {
  background-color: var(--secondary-color);
}

.btn-success:hover {
  background-color: #059669;
}

.btn-danger {
  background-color: var(--danger-color);
}

.btn-danger:hover {
  background-color: #dc2626;
}

.btn-warning {
  background-color: var(--warning-color);
}

.btn-warning:hover {
  background-color: #d97706;
}

.btn-primary {
  background-color: var(--primary-color);
}

.btn-primary:hover {
  background-color: var(--primary-dark);
}

.btn-small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  margin: 0 0.25rem;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.stat-card {
  background: var(--card-bg);
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-md);
  text-align: center;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.stat-card h3 {
  font-size: 2.5rem;
  margin: 0;
  color: var(--primary-color);
  font-weight: 800;
}

.stat-card p {
  margin: 0.5rem 0 0 0;
  color: var(--text-secondary);
  font-weight: 600;
  font-size: 1rem;
}

/* Equipment Card */
.equipment-card {
  background: var(--card-bg);
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: var(--shadow-sm);
  margin-bottom: 1.25rem;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.equipment-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.equipment-card h3 {
  margin-top: 0;
  color: var(--primary-color);
  font-size: 1.5rem;
}

.equipment-card p {
  margin: 0.5rem 0;
  color: var(--text-secondary);
}

.equipment-card p strong {
  color: var(--text-primary);
}

/* Filters */
.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  align-items: center;
}

.filters input,
.filters select {
  flex: 1;
  min-width: 200px;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
  background-color: var(--card-bg);
}

.filters input:focus,
.filters select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.filters button {
  flex: 0 0 auto;
}

/* Table Styles */
table {
  width: 100%;
  border-collapse: collapse;
  background: var(--card-bg);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow-md);
  margin-top: 1.5rem;
}

thead {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
}

th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.875rem;
  letter-spacing: 0.05em;
}

td {
  padding: 1rem;
  border-bottom: 1px solid var(--border-color);
}

tbody tr {
  transition: background-color 0.2s;
}

tbody tr:hover {
  background-color: var(--light-bg);
}

tbody tr:last-child td {
  border-bottom: none;
}

/* Modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: var(--card-bg);
  border-radius: 1rem;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-xl);
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 2px solid var(--border-color);
}

.modal-header h2 {
  margin: 0;
  color: var(--primary-color);
  font-size: 1.75rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: var(--text-secondary);
  padding: 0;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.5rem;
  transition: all 0.2s;
}

.close-btn:hover {
  background-color: var(--light-bg);
  color: var(--danger-color);
  transform: none;
}

.modal-content form {
  padding: 1.5rem;
}

/* Badges */
.badge {
  display: inline-block;
  padding: 0.375rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 600;
}

.badge-success {
  background-color: #d1fae5;
  color: #065f46;
}

.badge-warning {
  background-color: #fef3c7;
  color: #92400e;
}

.badge-danger {
  background-color: #fee2e2;
  color: #991b1b;
}

.badge-info {
  background-color: #cffafe;
  color: #164e63;
}

/* Messages */
.error,
.success {
  padding: 1rem;
  border-radius: 0.5rem;
  margin: 1rem 0;
  font-weight: 500;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.error {
  background-color: #fee2e2;
  color: #991b1b;
  border-left: 4px solid var(--danger-color);
}

.success {
  background-color: #d1fae5;
  color: #065f46;
  border-left: 4px solid var(--secondary-color);
}

/* Loading */
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  font-size: 1.5rem;
  color: var(--primary-color);
  font-weight: 600;
}

.loading::after {
  content: '';
  width: 2rem;
  height: 2rem;
  margin-left: 1rem;
  border: 3px solid var(--border-color);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
    flex-direction: column;
    align-items: flex-start;
  }

  .navbar h2 {
    font-size: 1.25rem;
  }

  .navbar > div {
    width: 100%;
    justify-content: flex-start;
  }

  .container {
    padding: 0 1rem;
    margin: 1rem auto;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .filters {
    flex-direction: column;
  }

  .filters input,
  .filters select {
    width: 100%;
    min-width: unset;
  }

  .auth-container form {
    padding: 1.5rem;
  }

  table {
    font-size: 0.875rem;
  }

  th,
  td {
    padding: 0.75rem 0.5rem;
  }

  .modal-content {
    margin: 1rem;
  }
}

@media (max-width: 480px) {
  .navbar a,
  .navbar button {
    font-size: 0.875rem;
    padding: 0.5rem 0.75rem;
  }

  .stat-card h3 {
    font-size: 2rem;
  }

  table {
    display: block;
    overflow-x: auto;
  }
}

```

Excellent! Let me add one more enhancement for the form submit buttons:

```css
.App {
  min-height: 100vh;
}

/* Navbar Styles */
.navbar {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: var(--shadow-md);
  flex-wrap: wrap;
  gap: 1rem;
}

.navbar h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
}

.navbar > div {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.navbar a {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: all 0.2s;
  font-weight: 500;
}

.navbar a:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-1px);
}

.navbar button {
  background-color: rgba(239, 68, 68, 0.9);
  color: white;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 600;
}

.navbar button:hover {
  background-color: rgba(239, 68, 68, 1);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Container */
.container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

.container h1 {
  color: var(--text-primary);
  font-size: 2rem;
  margin-bottom: 0.5rem;
  font-weight: 700;
}

.container h3 {
  color: var(--text-secondary);
  font-weight: 400;
  margin-bottom: 1.5rem;
}

/* Auth Container */
.auth-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary-color) 50%, var(--primary-dark) 100%);
  padding: 2rem;
}

.auth-container h2 {
  color: white;
  font-size: 2.5rem;
  margin-bottom: 2rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.auth-container form {
  background: var(--card-bg);
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-xl);
  width: 100%;
  max-width: 450px;
}

.auth-container form button[type="submit"] {
  width: 100%;
  padding: 1rem;
  font-size: 1.1rem;
  margin-top: 0.5rem;
}

.auth-container p {
  color: white;
  margin-top: 1.5rem;
  font-size: 1rem;
}

.auth-container p a {
  color: white;
  font-weight: 700;
  text-decoration: underline;
}

/* Form Styles */
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--text-primary);
  font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 80px;
}

/* Button Styles */
button,
.btn {
  background-color: var(--primary-color);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.2s;
  box-shadow: var(--shadow-sm);
  font-family: inherit;
}

button:hover,
.btn:hover {
  background-color: var(--primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

button:active,
.btn:active {
  transform: translateY(0);
}

.btn-success {
  background-color: var(--secondary-color);
}

.btn-success:hover {
  background-color: #059669;
}

.btn-danger {
  background-color: var(--danger-color);
}

.btn-danger:hover {
  background-color: #dc2626;
}

.btn-warning {
  background-color: var(--warning-color);
}

.btn-warning:hover {
  background-color: #d97706;
}

.btn-primary {
  background-color: var(--primary-color);
}

.btn-primary:hover {
  background-color: var(--primary-dark);
}

.btn-small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  margin: 0 0.25rem;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.stat-card {
  background: var(--card-bg);
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-md);
  text-align: center;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.stat-card h3 {
  font-size: 2.5rem;
  margin: 0;
  color: var(--primary-color);
  font-weight: 800;
}

.stat-card p {
  margin: 0.5rem 0 0 0;
  color: var(--text-secondary);
  font-weight: 600;
  font-size: 1rem;
}

/* Equipment Card */
.equipment-card {
  background: var(--card-bg);
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: var(--shadow-sm);
  margin-bottom: 1.25rem;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.equipment-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.equipment-card h3 {
  margin-top: 0;
  color: var(--primary-color);
  font-size: 1.5rem;
}

.equipment-card p {
  margin: 0.5rem 0;
  color: var(--text-secondary);
}

.equipment-card p strong {
  color: var(--text-primary);
}

/* Filters */
.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  align-items: center;
}

.filters input,
.filters select {
  flex: 1;
  min-width: 200px;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
  background-color: var(--card-bg);
}

.filters input:focus,
.filters select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.filters button {
  flex: 0 0 auto;
}

/* Table Styles */
table {
  width: 100%;
  border-collapse: collapse;
  background: var(--card-bg);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow-md);
  margin-top: 1.5rem;
}

thead {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
}

th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.875rem;
  letter-spacing: 0.05em;
}

td {
  padding: 1rem;
  border-bottom: 1px solid var(--border-color);
}

tbody tr {
  transition: background-color 0.2s;
}

tbody tr:hover {
  background-color: var(--light-bg);
}

tbody tr:last-child td {
  border-bottom: none;
}

/* Modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: var(--card-bg);
  border-radius: 1rem;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-xl);
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 2px solid var(--border-color);
}

.modal-header h2 {
  margin: 0;
  color: var(--primary-color);
  font-size: 1.75rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: var(--text-secondary);
  padding: 0;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.5rem;
  transition: all 0.2s;
}

.close-btn:hover {
  background-color: var(--light-bg);
  color: var(--danger-color);
  transform: none;
}

.modal-content form {
  padding: 1.5rem;
}

/* Badges */
.badge {
  display: inline-block;
  padding: 0.375rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 600;
}

.badge-success {
  background-color: #d1fae5;
  color: #065f46;
}

.badge-warning {
  background-color: #fef3c7;
  color: #92400e;
}

.badge-danger {
  background-color: #fee2e2;
  color: #991b1b;
}

.badge-info {
  background-color: #cffafe;
  color: #164e63;
}

/* Messages */
.error,
.success {
  padding: 1rem;
  border-radius: 0.5rem;
  margin: 1rem 0;
  font-weight: 500;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.error {
  background-color: #fee2e2;
  color: #991b1b;
  border-left: 4px solid var(--danger-color);
}

.success {
  background-color: #d1fae5;
  color: #065f46;
  border-left: 4px solid var(--secondary-color);
}

/* Loading */
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  font-size: 1.5rem;
  color: var(--primary-color);
  font-weight: 600;
}

.loading::after {
  content: '';
  width: 2rem;
  height: 2rem;
  margin-left: 1rem;
  border: 3px solid var(--border-color);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
    flex-direction: column;
    align-items: flex-start;
  }

  .navbar h2 {
    font-size: 1.25rem;
  }

  .navbar > div {
    width: 100%;
    justify-content: flex-start;
  }

  .container {
    padding: 0 1rem;
    margin: 1rem auto;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .filters {
    flex-direction: column;
  }

  .filters input,
  .filters select {
    width: 100%;
    min-width: unset;
  }

  .auth-container form {
    padding: 1.5rem;
  }

  table {
    font-size: 0.875rem;
  }

  th,
  td {
    padding: 0.75rem 0.5rem;
  }

  .modal-content {
    margin: 1rem;
  }
}

@media (max-width: 480px) {
  .navbar a,
  .navbar button {
    font-size: 0.875rem;
    padding: 0.5rem 0.75rem;
  }

  .stat-card h3 {
    font-size: 2rem;
  }

  table {
    display: block;
    overflow-x: auto;
  }
}

```

Let me add a few more polished elements to enhance the overall experience:

```css
.App {
  min-height: 100vh;
}

/* Navbar Styles */
.navbar {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: var(--shadow-md);
  flex-wrap: wrap;
  gap: 1rem;
}

.navbar h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
}

.navbar > div {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.navbar a {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: all 0.2s;
  font-weight: 500;
}

.navbar a:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-1px);
}

.navbar button {
  background-color: rgba(239, 68, 68, 0.9);
  color: white;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 600;
}

.navbar button:hover {
  background-color: rgba(239, 68, 68, 1);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Container */
.container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

.container h1 {
  color: var(--text-primary);
  font-size: 2rem;
  margin-bottom: 0.5rem;
  font-weight: 700;
}

.container h3 {
  color: var(--text-secondary);
  font-weight: 400;
  margin-bottom: 1.5rem;
}

/* Auth Container */
.auth-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary-color) 50%, var(--primary-dark) 100%);
  padding: 2rem;
}

.auth-container h2 {
  color: white;
  font-size: 2.5rem;
  margin-bottom: 2rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.auth-container form {
  background: var(--card-bg);
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-xl);
  width: 100%;
  max-width: 450px;
}

.auth-container form button[type="submit"] {
  width: 100%;
  padding: 1rem;
  font-size: 1.1rem;
  margin-top: 0.5rem;
}

.auth-container p {
  color: white;
  margin-top: 1.5rem;
  font-size: 1rem;
}

.auth-container p a {
  color: white;
  font-weight: 700;
  text-decoration: underline;
}

/* Form Styles */
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--text-primary);
  font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 80px;
}

/* Button Styles */
button,
.btn {
  background-color: var(--primary-color);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.2s;
  box-shadow: var(--shadow-sm);
  font-family: inherit;
}

button:hover,
.btn:hover {
  background-color: var(--primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

button:active,
.btn:active {
  transform: translateY(0);
}

.btn-success {
  background-color: var(--secondary-color);
}

.btn-success:hover {
  background-color: #059669;
}

.btn-danger {
  background-color: var(--danger-color);
}

.btn-danger:hover {
  background-color: #dc2626;
}

.btn-warning {
  background-color: var(--warning-color);
}

.btn-warning:hover {
  background-color: #d97706;
}

.btn-primary {
  background-color: var(--primary-color);
}

.btn-primary:hover {
  background-color: var(--primary-dark);
}

.btn-small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  margin: 0 0.25rem;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.stat-card {
  background: var(--card-bg);
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-md);
  text-align: center;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.stat-card h3 {
  font-size: 2.5rem;
  margin: 0;
  color: var(--primary-color);
  font-weight: 800;
}

.stat-card p {
  margin: 0.5rem 0 0 0;
  color: var(--text-secondary);
  font-weight: 600;
  font-size: 1rem;
}

/* Equipment Card */
.equipment-card {
  background: var(--card-bg);
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: var(--shadow-sm);
  margin-bottom: 1.25rem;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.equipment-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.equipment-card h3 {
  margin-top: 0;
  color: var(--primary-color);
  font-size: 1.5rem;
}

.equipment-card p {
  margin: 0.5rem 0;
  color: var(--text-secondary);
}

.equipment-card p strong {
  color: var(--text-primary);
}

/* Filters */
.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  align-items: center;
}

.filters input,
.filters select {
  flex: 1;
  min-width: 200px;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
  background-color: var(--card-bg);
}

.filters input:focus,
.filters select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.filters button {
  flex: 0 0 auto;
}

/* Table Styles */
table {
  width: 100%;
  border-collapse: collapse;
  background: var(--card-bg);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow-md);
  margin-top: 1.5rem;
}

thead {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
}

th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.875rem;
  letter-spacing: 0.05em;
}

td {
  padding: 1rem;
  border-bottom: 1px solid var(--border-color);
}

tbody tr {
  transition: background-color 0.2s;
}

tbody tr:hover {
  background-color: var(--light-bg);
}

tbody tr:last-child td {
  border-bottom: none;
}

/* Empty state in tables */
tbody td[colspan] {
  text-align: center;
  padding: 2rem;
  color: var(--text-secondary);
  font-style: italic;
}

/* Modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: var(--card-bg);
  border-radius: 1rem;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-xl);
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 2px solid var(--border-color);
}

.modal-header h2 {
  margin: 0;
  color: var(--primary-color);
  font-size: 1.75rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: var(--text-secondary);
  padding: 0;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.5rem;
  transition: all 0.2s;
}

.close-btn:hover {
  background-color: var(--light-bg);
  color: var(--danger-color);
  transform: none;
}

.modal-content form {
  padding: 1.5rem;
}

/* Badges */
.badge {
  display: inline-block;
  padding: 0.375rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 600;
}

.badge-success {
  background-color: #d1fae5;
  color: #065f46;
}

.badge-warning {
  background-color: #fef3c7;
  color: #92400e;
}

.badge-danger {
  background-color: #fee2e2;
  color: #991b1b;
}

.badge-info {
  background-color: #cffafe;
  color: #164e63;
}

/* Messages */
.error,
.success {
  padding: 1rem;
  border-radius: 0.5rem;
  margin: 1rem 0;
  font-weight: 500;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.error {
  background-color: #fee2e2;
  color: #991b1b;
  border-left: 4px solid var(--danger-color);
}

.success {
  background-color: #d1fae5;
  color: #065f46;
  border-left: 4px solid var(--secondary-color);
}

/* Loading */
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  font-size: 1.5rem;
  color: var(--primary-color);
  font-weight: 600;
}

.loading::after {
  content: '';
  width: 2rem;
  height: 2rem;
  margin-left: 1rem;
  border: 3px solid var(--border-color);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
    flex-direction: column;
    align-items: flex-start;
  }

  .navbar h2 {
    font-size: 1.25rem;
  }

  .navbar > div {
    width: 100%;
    justify-content: flex-start;
  }

  .container {
    padding: 0 1rem;
    margin: 1rem auto;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .filters {
    flex-direction: column;
  }

  .filters input,
  .filters select {
    width: 100%;
    min-width: unset;
  }

  .auth-container form {
    padding: 1.5rem;
  }

  table {
    font-size: 0.875rem;
  }

  th,
  td {
    padding: 0.75rem 0.5rem;
  }

  .modal-content {
    margin: 1rem;
  }
}

@media (max-width: 480px) {
  .navbar a,
  .navbar button {
    font-size: 0.875rem;
    padding: 0.5rem 0.75rem;
  }

  .stat-card h3 {
    font-size: 2rem;
  }

  table {
    display: block;
    overflow-x: auto;
  }
}

```

```css
.App {
  min-height: 100vh;
}

/* Navbar Styles */
.navbar {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: var(--shadow-md);
  flex-wrap: wrap;
  gap: 1rem;
}

.navbar h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
}

.navbar > div {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.navbar a {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: all 0.2s;
  font-weight: 500;
}

.navbar a:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-1px);
}

.navbar button {
  background-color: rgba(239, 68, 68, 0.9);
  color: white;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 600;
}

.navbar button:hover {
  background-color: rgba(239, 68, 68, 1);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Container */
.container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

.container h1 {
  color: var(--text-primary);
  font-size: 2rem;
  margin-bottom: 0.5rem;
  font-weight: 700;
}

.container h3 {
  color: var(--text-secondary);
  font-weight: 400;
  margin-bottom: 1.5rem;
}

/* Auth Container */
.auth-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary-color) 50%, var(--primary-dark) 100%);
  padding: 2rem;
}

.auth-container h2 {
  color: white;
  font-size: 2.5rem;
  margin-bottom: 2rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.auth-container form {
  background: var(--card-bg);
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-xl);
  width: 100%;
  max-width: 450px;
}

.auth-container form button[type="submit"] {
  width: 100%;
  padding: 1rem;
  font-size: 1.1rem;
  margin-top: 0.5rem;
}

.auth-container p {
  color: white;
  margin-top: 1.5rem;
  font-size: 1rem;
}

.auth-container p a {
  color: white;
  font-weight: 700;
  text-decoration: underline;
}

/* Form Styles */
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--text-primary);
  font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 80px;
}

/* Button Styles */
button,
.btn {
  background-color: var(--primary-color);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.2s;
  box-shadow: var(--shadow-sm);
  font-family: inherit;
}

button:hover,
.btn:hover {
  background-color: var(--primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

button:active,
.btn:active {
  transform: translateY(0);
}

.btn-success {
  background-color: var(--secondary-color);
}

.btn-success:hover {
  background-color: #059669;
}

.btn-danger {
  background-color: var(--danger-color);
}

.btn-danger:hover {
  background-color: #dc2626;
}

.btn-warning {
  background-color: var(--warning-color);
}

.btn-warning:hover {
  background-color: #d97706;
}

.btn-primary {
  background-color: var(--primary-color);
}

.btn-primary:hover {
  background-color: var(--primary-dark);
}

.btn-small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  margin: 0 0.25rem;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.stat-card {
  background: var(--card-bg);
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-md);
  text-align: center;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.stat-card h3 {
  font-size: 2.5rem;
  margin: 0;
  color: var(--primary-color);
  font-weight: 800;
}

.stat-card p {
  margin: 0.5rem 0 0 0;
  color: var(--text-secondary);
  font-weight: 600;
  font-size: 1rem;
}

/* Equipment Card */
.equipment-card {
  background: var(--card-bg);
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: var(--shadow-sm);
  margin-bottom: 1.25rem;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.equipment-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.equipment-card h3 {
  margin-top: 0;
  color: var(--primary-color);
  font-size: 1.5rem;
}

.equipment-card p {
  margin: 0.5rem 0;
  color: var(--text-secondary);
}

.equipment-card p strong {
  color: var(--text-primary);
}

/* Filters */
.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  align-items: center;
}

.filters input,
.filters select {
  flex: 1;
  min-width: 200px;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
  background-color: var(--card-bg);
}

.filters input:focus,
.filters select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.filters button {
  flex: 0 0 auto;
}

/* Table Styles */
table {
  width: 100%;
  border-collapse: collapse;
  background: var(--card-bg);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow-md);
  margin-top: 1.5rem;
}

thead {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
}

th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.875rem;
  letter-spacing: 0.05em;
}

td {
  padding: 1rem;
  border-bottom: 1px solid var(--border-color);
}

tbody tr {
  transition: background-color 0.2s;
}

tbody tr:hover {
  background-color: var(--light-bg);
}

tbody tr:last-child td {
  border-bottom: none;
}

/* Empty state in tables */
tbody td[colspan] {
  text-align: center;
  padding: 2rem;
  color: var(--text-secondary);
  font-style: italic;
}

/* Modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: var(--card-bg);
  border-radius: 1rem;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-xl);
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 2px solid var(--border-color);
}

.modal-header h2 {
  margin: 0;
  color: var(--primary-color);
  font-size: 1.75rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: var(--text-secondary);
  padding: 0;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.5rem;
  transition: all 0.2s;
}

.close-btn:hover {
  background-color: var(--light-bg);
  color: var(--danger-color);
  transform: none;
}

.modal-content form {
  padding: 1.5rem;
}

/* Badges */
.badge {
  display: inline-block;
  padding: 0.375rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 600;
}

.badge-success {
  background-color: #d1fae5;
  color: #065f46;
}

.badge-warning {
  background-color: #fef3c7;
  color: #92400e;
}

.badge-danger {
  background-color: #fee2e2;
  color: #991b1b;
}

.badge-info {
  background-color: #cffafe;
  color: #164e63;
}

/* Messages */
.error,
.success {
  padding: 1rem;
  border-radius: 0.5rem;
  margin: 1rem 0;
  font-weight: 500;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.error {
  background-color: #fee2e2;
  color: #991b1b;
  border-left: 4px solid var(--danger-color);
}

.success {
  background-color: #d1fae5;
  color: #065f46;
  border-left: 4px solid var(--secondary-color);
}

/* Loading */
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  font-size: 1.5rem;
  color: var(--primary-color);
  font-weight: 600;
}

.loading::after {
  content: '';
  width: 2rem;
  height: 2rem;
  margin-left: 1rem;
  border: 3px solid var(--border-color);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Page Header */
.page-header {
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid var(--border-color);
}

.page-header h1 {
  margin-bottom: 0.25rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
    flex-direction: column;
    align-items: flex-start;
  }

  .navbar h2 {
    font-size: 1.25rem;
  }

  .navbar > div {
    width: 100%;
    justify-content: flex-start;
  }

  .container {
    padding: 0 1rem;
    margin: 1rem auto;
  }

  .container h1 {
    font-size: 1.5rem;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .filters {
    flex-direction: column;
  }

  .filters input,
  .filters select,
  .filters button {
    width: 100%;
    min-width: unset;
  }

  .auth-container form {
    padding: 1.5rem;
  }

  .auth-container h2 {
    font-size: 2rem;
  }

  table {
    font-size: 0.875rem;
  }

  th,
  td {
    padding: 0.75rem 0.5rem;
  }

  .modal-content {
    margin: 1rem;
  }

  .equipment-card {
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .navbar a,
  .navbar button {
    font-size: 0.875rem;
    padding: 0.5rem 0.75rem;
  }

  .stat-card h3 {
    font-size: 2rem;
  }

  table {
    display: block;
    overflow-x: auto;
  }
}

```

```css
.App {
  min-height: 100vh;
}

/* Navbar Styles */
.navbar {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: var(--shadow-md);
  flex-wrap: wrap;
  gap: 1rem;
}

.navbar h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
}

.navbar > div {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.navbar a {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: all 0.2s;
  font-weight: 500;
}

.navbar a:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-1px);
}

.navbar button {
  background-color: rgba(239, 68, 68, 0.9);
  color: white;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 600;
}

.navbar button:hover {
  background-color: rgba(239, 68, 68, 1);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Container */
.container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

.container h1 {
  color: var(--text-primary);
  font-size: 2rem;
  margin-bottom: 0.5rem;
  font-weight: 700;
}

.container h3 {
  color: var(--text-secondary);
  font-weight: 400;
  margin-bottom: 1.5rem;
}

/* Auth Container */
.auth-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary-color) 50%, var(--primary-dark) 100%);
  padding: 2rem;
}

.auth-container h2 {
  color: white;
  font-size: 2.5rem;
  margin-bottom: 2rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.auth-container form {
  background: var(--card-bg);
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-xl);
  width: 100%;
  max-width: 450px;
}

.auth-container form button[type="submit"] {
  width: 100%;
  padding: 1rem;
  font-size: 1.1rem;
  margin-top: 0.5rem;
}

.auth-container p {
  color: white;
  margin-top: 1.5rem;
  font-size: 1rem;
}

.auth-container p a {
  color: white;
  font-weight: 700;
  text-decoration: underline;
}

/* Form Styles */
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--text-primary);
  font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 80px;
}

/* Button Styles */
button,
.btn {
  background-color: var(--primary-color);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.2s;
  box-shadow: var(--shadow-sm);
  font-family: inherit;
}

button:hover,
.btn:hover {
  background-color: var(--primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

button:active,
.btn:active {
  transform: translateY(0);
}

.btn-success {
  background-color: var(--secondary-color);
}

.btn-success:hover {
  background-color: #059669;
}

.btn-danger {
  background-color: var(--danger-color);
}

.btn-danger:hover {
  background-color: #dc2626;
}

.btn-warning {
  background-color: var(--warning-color);
}

.btn-warning:hover {
  background-color: #d97706;
}

.btn-primary {
  background-color: var(--primary-color);
}

.btn-primary:hover {
  background-color: var(--primary-dark);
}

.btn-small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  margin: 0 0.25rem;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.stat-card {
  background: var(--card-bg);
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-md);
  text-align: center;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.stat-card h3 {
  font-size: 2.5rem;
  margin: 0;
  color: var(--primary-color);
  font-weight: 800;
}

.stat-card p {
  margin: 0.5rem 0 0 0;
  color: var(--text-secondary);
  font-weight: 600;
  font-size: 1rem;
}

/* Equipment Card */
.equipment-card {
  background: var(--card-bg);
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: var(--shadow-sm);
  margin-bottom: 1.25rem;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.equipment-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.equipment-card h3 {
  margin-top: 0;
  color: var(--primary-color);
  font-size: 1.5rem;
}

.equipment-card p {
  margin: 0.5rem 0;
  color: var(--text-secondary);
}

.equipment-card p strong {
  color: var(--text-primary);
}

/* Filters */
.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  align-items: center;
}

.filters input,
.filters select {
  flex: 1;
  min-width: 200px;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
  background-color: var(--card-bg);
}

.filters input:focus,
.filters select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.filters button {
  flex: 0 0 auto;
}

/* Table Styles */
table {
  width: 100%;
  border-collapse: collapse;
  background: var(--card-bg);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow-md);
  margin-top: 1.5rem;
}

thead {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
}

th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.875rem;
  letter-spacing: 0.05em;
}

td {
  padding: 1rem;
  border-bottom: 1px solid var(--border-color);
}

tbody tr {
  transition: background-color 0.2s;
}

tbody tr:hover {
  background-color: var(--light-bg);
}

tbody tr:last-child td {
  border-bottom: none;
}

/* Empty state in tables */
tbody td[colspan] {
  text-align: center;
  padding: 2rem;
  color: var(--text-secondary);
  font-style: italic;
}

/* Modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: var(--card-bg);
  border-radius: 1rem;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-xl);
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 2px solid var(--border-color);
}

.modal-header h2 {
  margin: 0;
  color: var(--primary-color);
  font-size: 1.75rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: var(--text-secondary);
  padding: 0;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.5rem;
  transition: all 0.2s;
}

.close-btn:hover {
  background-color: var(--light-bg);
  color: var(--danger-color);
  transform: none;
}

.modal-content form {
  padding: 1.5rem;
}

/* Badges */
.badge {
  display: inline-block;
  padding: 0.375rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 600;
}

.badge-success {
  background-color: #d1fae5;
  color: #065f46;
}

.badge-warning {
  background-color: #fef3c7;
  color: #92400e;
}

.badge-danger {
  background-color: #fee2e2;
  color: #991b1b;
}

.badge-info {
  background-color: #cffafe;
  color: #164e63;
}

/* Messages */
.error,
.success {
  padding: 1rem;
  border-radius: 0.5rem;
  margin: 1rem 0;
  font-weight: 500;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.error {
  background-color: #fee2e2;
  color: #991b1b;
  border-left: 4px solid var(--danger-color);
}

.success {
  background-color: #d1fae5;
  color: #065f46;
  border-left: 4px solid var(--secondary-color);
}

/* Loading */
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  font-size: 1.5rem;
  color: var(--primary-color);
  font-weight: 600;
}

.loading::after {
  content: '';
  width: 2rem;
  height: 2rem;
  margin-left: 1rem;
  border: 3px solid var(--border-color);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Page Header */
.page-header {
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid var(--border-color);
}

.page-header h1 {
  margin-bottom: 0.25rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
    flex-direction: column;
    align-items: flex-start;
  }

  .navbar h2 {
    font-size: 1.25rem;
  }

  .navbar > div {
    width: 100%;
    justify-content: flex-start;
  }

  .container {
    padding: 0 1rem;
    margin: 1rem auto;
  }

  .container h1 {
    font-size: 1.5rem;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .filters {
    flex-direction: column;
  }

  .filters input,
  .filters select,
  .filters button {
    width: 100%;
    min-width: unset;
  }

  .auth-container form {
    padding: 1.5rem;
  }

  .auth-container h2 {
    font-size: 2rem;
  }

  table {
    font-size: 0.875rem;
  }

  th,
  td {
    padding: 0.75rem 0.5rem;
  }

  .modal-content {
    margin: 1rem;
  }

  .equipment-card {
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .navbar a,
  .navbar button {
    font-size: 0.875rem;
    padding: 0.5rem 0.75rem;
  }

  .stat-card {
    padding: 1.5rem;
  }

  .stat-card h3 {
    font-size: 2rem;
  }

  .equipment-card h3 {
    font-size: 1.25rem;
  }

  table {
    display: block;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }

  .btn-small {
    padding: 0.4rem 0.75rem;
    font-size: 0.8rem;
  }
}

/* Smooth scrolling */
html {
  scroll-behavior: smooth;
}

/* Focus visible for accessibility */
*:focus-visible {
  outline: 2px solid var(--primary-color);
  outline-offset: 2px;
}

```

Perfect! Let me check for any linting errors in the updated files:

Excellent! The UI revamp is complete! Here's a comprehensive summary of what I've improved:

## 🎨 Frontend UI Revamp Summary

### ✅ What I've Enhanced:

#### **1. Global Styling & Design System** (`index.css` & `App.css`)
- ✨ Added CSS variables for consistent colors, shadows, and spacing throughout the app
- 🎨 Modern color palette with primary blue (`#2563eb`), secondary green (`#10b981`), and semantic colors
- 📱 Comprehensive responsive design for mobile, tablet, and desktop
- 🌟 Smooth animations and transitions for a polished feel

#### **2. Navigation Bar**
- 🎭 Beautiful gradient background with hover effects
- 📱 Fully responsive with mobile-friendly layout
- ✨ Smooth hover transitions and better spacing

#### **3. Authentication Pages** (Login & Register)
- 🌈 Full-screen gradient background for visual impact
- 💎 Elevated card design with shadows
- 🎯 Improved form styling with focus states
- 📏 Full-width submit buttons for better UX
- ✨ Better error message displays

#### **4. Dashboard**
- 📊 Grid layout for statistics cards with hover effects
- 🎨 Large, prominent numbers with better typography
- ✨ Cards that lift on hover for interactivity
- 📱 Responsive grid that stacks on mobile

#### **5. Equipment Pages**
- 🗂️ Clean card layouts with subtle shadows
- 🔍 Enhanced filter section with better input styling
- 🎯 Improved table design with gradient headers
- ✨ Smooth hover effects on cards and table rows

#### **6. Tables**
- 🎨 Modern gradient headers
- ✏️ Hover effects on rows
- 📱 Horizontal scrolling on mobile devices
- 🎭 Better empty state styling

#### **7. Modals**
- 💫 Smooth slide-in animation
- 🌫️ Backdrop blur effect
- ✨ Modern close button with hover effects
- 📱 Fully responsive

#### **8. Buttons**
- 🎨 Color-coded button variants (success, danger, warning, primary)
- ✨ Lift effect on hover
- 📱 Responsive sizing for mobile
- 🎯 Better spacing and visual hierarchy

#### **9. Form Elements**
- 🎨 Consistent styling across all inputs
- ✨ Focus states with blue glow effect
- 📱 Touch-friendly sizes on mobile
- 🎯 Better label typography

#### **10. Badges & Status Indicators**
- 🏷️ Color-coded status badges (pending, approved, issued, etc.)
- ✨ Pill-shaped design with appropriate colors
- 📱 Readable on all screen sizes

#### **11. Messages & Alerts**
- ✨ Slide-in animation for notifications
- 🎨 Color-coded for success/error states
- 🎯 Better visual hierarchy with left border accent

#### **12. Loading States**
- 🔄 Animated spinner with smooth rotation
- 🎨 Consistent branding colors
- ✨ Centered and prominent

#### **13. Accessibility**
- ♿ Focus-visible outlines for keyboard navigation
- 📱 Touch-friendly tap targets on mobile
- 🎯 Proper color contrast ratios
- ⚡ Smooth scrolling behavior

### 🎯 Key Features:

✅ **Minimal Code Changes** - Only CSS updates, no JavaScript changes  
✅ **Fully Responsive** - Works perfectly on mobile, tablet, and desktop  
✅ **Modern Design** - Clean, professional look with gradients and shadows  
✅ **Better UX** - Hover effects, animations, and visual feedback  
✅ **Consistent** - Unified design system across all pages  
✅ **Professional** - School-appropriate, modern interface  
✅ **Accessible** - Keyboard navigation and proper focus states  

### 📱 Responsive Breakpoints:

- **Desktop**: > 768px (full layout)
- **Tablet**: 481px - 768px (adjusted spacing)
- **Mobile**: ≤ 480px (stacked layout, optimized buttons)

The UI is now modern, user-friendly, and responsive across all devices while maintaining all the existing functionality! 🚀

---

**User**

Background can be improved. Can you also give it a dual tone color. Maybe something like one color being faded into another from left top corner to right bottom corner.

---

**Cursor**

Perfect! Let me add a beautiful dual-tone gradient background that fades from top-left to bottom-right:

```css
:root {
  --primary-color: #2563eb;
  --primary-dark: #1e40af;
  --primary-light: #3b82f6;
  --secondary-color: #10b981;
  --danger-color: #ef4444;
  --warning-color: #f59e0b;
  --info-color: #06b6d4;
  --dark-bg: #1f2937;
  --light-bg: #f9fafb;
  --card-bg: #ffffff;
  --border-color: #e5e7eb;
  --text-primary: #111827;
  --text-secondary: #6b7280;
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background: linear-gradient(135deg, #f0f9ff 0%, #e0e7ff 50%, #fce7f3 100%);
  background-attachment: fixed;
  color: var(--text-primary);
  line-height: 1.6;
  min-height: 100vh;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}

```

```css
.App {
  min-height: 100vh;
  background: transparent;
}

/* Navbar Styles */
.navbar {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: var(--shadow-md);
  flex-wrap: wrap;
  gap: 1rem;
}

.navbar h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
}

.navbar > div {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.navbar a {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: all 0.2s;
  font-weight: 500;
}

.navbar a:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-1px);
}

.navbar button {
  background-color: rgba(239, 68, 68, 0.9);
  color: white;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 600;
}

.navbar button:hover {
  background-color: rgba(239, 68, 68, 1);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Container */
.container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

.container h1 {
  color: var(--text-primary);
  font-size: 2rem;
  margin-bottom: 0.5rem;
  font-weight: 700;
}

.container h3 {
  color: var(--text-secondary);
  font-weight: 400;
  margin-bottom: 1.5rem;
}

/* Auth Container */
.auth-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary-color) 50%, var(--primary-dark) 100%);
  padding: 2rem;
}

.auth-container h2 {
  color: white;
  font-size: 2.5rem;
  margin-bottom: 2rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.auth-container form {
  background: var(--card-bg);
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-xl);
  width: 100%;
  max-width: 450px;
}

.auth-container form button[type="submit"] {
  width: 100%;
  padding: 1rem;
  font-size: 1.1rem;
  margin-top: 0.5rem;
}

.auth-container p {
  color: white;
  margin-top: 1.5rem;
  font-size: 1rem;
}

.auth-container p a {
  color: white;
  font-weight: 700;
  text-decoration: underline;
}

/* Form Styles */
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--text-primary);
  font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 80px;
}

/* Button Styles */
button,
.btn {
  background-color: var(--primary-color);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.2s;
  box-shadow: var(--shadow-sm);
  font-family: inherit;
}

button:hover,
.btn:hover {
  background-color: var(--primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

button:active,
.btn:active {
  transform: translateY(0);
}

.btn-success {
  background-color: var(--secondary-color);
}

.btn-success:hover {
  background-color: #059669;
}

.btn-danger {
  background-color: var(--danger-color);
}

.btn-danger:hover {
  background-color: #dc2626;
}

.btn-warning {
  background-color: var(--warning-color);
}

.btn-warning:hover {
  background-color: #d97706;
}

.btn-primary {
  background-color: var(--primary-color);
}

.btn-primary:hover {
  background-color: var(--primary-dark);
}

.btn-small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  margin: 0 0.25rem;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.stat-card {
  background: var(--card-bg);
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-md);
  text-align: center;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.stat-card h3 {
  font-size: 2.5rem;
  margin: 0;
  color: var(--primary-color);
  font-weight: 800;
}

.stat-card p {
  margin: 0.5rem 0 0 0;
  color: var(--text-secondary);
  font-weight: 600;
  font-size: 1rem;
}

/* Equipment Card */
.equipment-card {
  background: var(--card-bg);
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: var(--shadow-sm);
  margin-bottom: 1.25rem;
  transition: all 0.3s;
  border: 1px solid var(--border-color);
}

.equipment-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.equipment-card h3 {
  margin-top: 0;
  color: var(--primary-color);
  font-size: 1.5rem;
}

.equipment-card p {
  margin: 0.5rem 0;
  color: var(--text-secondary);
}

.equipment-card p strong {
  color: var(--text-primary);
}

/* Filters */
.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  align-items: center;
}

.filters input,
.filters select {
  flex: 1;
  min-width: 200px;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  font-family: inherit;
  background-color: var(--card-bg);
}

.filters input:focus,
.filters select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.filters button {
  flex: 0 0 auto;
}

/* Table Styles */
table {
  width: 100%;
  border-collapse: collapse;
  background: var(--card-bg);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow-md);
  margin-top: 1.5rem;
}

thead {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
}

th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.875rem;
  letter-spacing: 0.05em;
}

td {
  padding: 1rem;
  border-bottom: 1px solid var(--border-color);
}

tbody tr {
  transition: background-color 0.2s;
}

tbody tr:hover {
  background-color: var(--light-bg);
}

tbody tr:last-child td {
  border-bottom: none;
}

/* Empty state in tables */
tbody td[colspan] {
  text-align: center;
  padding: 2rem;
  color: var(--text-secondary);
  font-style: italic;
}

/* Modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: var(--card-bg);
  border-radius: 1rem;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-xl);
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 2px solid var(--border-color);
}

.modal-header h2 {
  margin: 0;
  color: var(--primary-color);
  font-size: 1.75rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: var(--text-secondary);
  padding: 0;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.5rem;
  transition: all 0.2s;
}

.close-btn:hover {
  background-color: var(--light-bg);
  color: var(--danger-color);
  transform: none;
}

.modal-content form {
  padding: 1.5rem;
}

/* Badges */
.badge {
  display: inline-block;
  padding: 0.375rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 600;
}

.badge-success {
  background-color: #d1fae5;
  color: #065f46;
}

.badge-warning {
  background-color: #fef3c7;
  color: #92400e;
}

.badge-danger {
  background-color: #fee2e2;
  color: #991b1b;
}

.badge-info {
  background-color: #cffafe;
  color: #164e63;
}

/* Messages */
.error,
.success {
  padding: 1rem;
  border-radius: 0.5rem;
  margin: 1rem 0;
  font-weight: 500;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.error {
  background-color: #fee2e2;
  color: #991b1b;
  border-left: 4px solid var(--danger-color);
}

.success {
  background-color: #d1fae5;
  color: #065f46;
  border-left: 4px solid var(--secondary-color);
}

/* Loading */
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  font-size: 1.5rem;
  color: var(--primary-color);
  font-weight: 600;
}

.loading::after {
  content: '';
  width: 2rem;
  height: 2rem;
  margin-left: 1rem;
  border: 3px solid var(--border-color);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Page Header */
.page-header {
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid var(--border-color);
}

.page-header h1 {
  margin-bottom: 0.25rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
    flex-direction: column;
    align-items: flex-start;
  }

  .navbar h2 {
    font-size: 1.25rem;
  }

  .navbar > div {
    width: 100%;
    justify-content: flex-start;
  }

  .container {
    padding: 0 1rem;
    margin: 1rem auto;
  }

  .container h1 {
    font-size: 1.5rem;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .filters {
    flex-direction: column;
  }

  .filters input,
  .filters select,
  .filters button {
    width: 100%;
    min-width: unset;
  }

  .auth-container form {
    padding: 1.5rem;
  }

  .auth-container h2 {
    font-size: 2rem;
  }

  table {
    font-size: 0.875rem;
  }

  th,
  td {
    padding: 0.75rem 0.5rem;
  }

  .modal-content {
    margin: 1rem;
  }

  .equipment-card {
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .navbar a,
  .navbar button {
    font-size: 0.875rem;
    padding: 0.5rem 0.75rem;
  }

  .stat-card {
    padding: 1.5rem;
  }

  .stat-card h3 {
    font-size: 2rem;
  }

  .equipment-card h3 {
    font-size: 1.25rem;
  }

  table {
    display: block;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }

  .btn-small {
    padding: 0.4rem 0.75rem;
    font-size: 0.8rem;
  }
}

/* Smooth scrolling */
html {
  scroll-behavior: smooth;
}

/* Focus visible for accessibility */
*:focus-visible {
  outline: 2px solid var(--primary-color);
  outline-offset: 2px;
}

```

Perfect! I've added a beautiful dual-tone gradient background that smoothly transitions from **light blue** → **light purple** → **light pink** at a 135° angle (top-left to bottom-right). 

### 🎨 What I've Added:

**Gradient Colors:**
- 🔵 **Top-left**: Light Sky Blue (`#f0f9ff`)
- 💜 **Middle**: Light Lavender (`#e0e7ff`)
- 💗 **Bottom-right**: Light Rose Pink (`#fce7f3`)

**Key Features:**
- ✨ Smooth 3-color transition for depth
- 📌 `background-attachment: fixed` - keeps the gradient fixed while scrolling
- 🎯 135° angle for perfect diagonal flow from top-left to bottom-right
- 🌈 Subtle, professional colors that complement the blue primary theme
- 💎 Works beautifully with the white cards and components

The gradient is subtle enough to maintain professionalism for a school system while adding a modern, visually appealing touch! The white cards and content will pop nicely against this soft, colorful background. 🚀

