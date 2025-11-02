import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function EquipmentManage() {
  const [equipment, setEquipment] = useState([]);
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [editMode, setEditMode] = useState(false);
  const [currentItem, setCurrentItem] = useState(null);
  const [formData, setFormData] = useState({
    name: '',
    category: 'sports',
    description: '',
    condition: 'good',
    quantity: 1,
    available_quantity: 1,
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

    if (userData.role !== 'admin') {
      navigate('/dashboard');
      return;
    }

    fetchEquipment(token);
  }, [navigate]);

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
    } finally {
      setLoading(false);
    }
  };

  const openAddModal = () => {
    setFormData({
      name: '',
      category: 'sports',
      description: '',
      condition: 'good',
      quantity: 1,
      available_quantity: 1,
    });
    setEditMode(false);
    setCurrentItem(null);
    setShowModal(true);
    setMessage('');
  };

  const openEditModal = (item) => {
    setFormData({
      name: item.name,
      category: item.category,
      description: item.description,
      condition: item.condition,
      quantity: item.quantity,
      available_quantity: item.available_quantity,
    });
    setEditMode(true);
    setCurrentItem(item);
    setShowModal(true);
    setMessage('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem('token');

    try {
      const url = editMode ? `/api/equipment/${currentItem.id}/` : '/api/equipment/';
      const method = editMode ? 'PUT' : 'POST';

      const response = await fetch(url, {
        method: method,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setMessage(editMode ? 'Equipment updated!' : 'Equipment added!');
        setShowModal(false);
        fetchEquipment(token);
      } else {
        const data = await response.json();
        setMessage('Error: ' + JSON.stringify(data));
      }
    } catch (err) {
      setMessage('Error saving equipment');
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Are you sure you want to delete this equipment?')) {
      return;
    }

    const token = localStorage.getItem('token');

    try {
      const response = await fetch(`/api/equipment/${id}/`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      if (response.ok) {
        setMessage('Equipment deleted!');
        fetchEquipment(token);
      } else {
        setMessage('Error deleting equipment');
      }
    } catch (err) {
      setMessage('Error deleting equipment');
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
        <h1>Manage Equipment</h1>
        <button onClick={openAddModal}>Add New Equipment</button>

        {message && <div className="success">{message}</div>}

        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Category</th>
              <th>Condition</th>
              <th>Quantity</th>
              <th>Available</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {equipment.map((item) => (
              <tr key={item.id}>
                <td>{item.name}</td>
                <td>{item.category}</td>
                <td>{item.condition}</td>
                <td>{item.quantity}</td>
                <td>{item.available_quantity}</td>
                <td>
                  <button className="btn-warning btn-small" onClick={() => openEditModal(item)}>
                    Edit
                  </button>
                  <button className="btn-danger btn-small" onClick={() => handleDelete(item.id)}>
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {showModal && (
          <div className="modal">
            <div className="modal-content">
              <div className="modal-header">
                <h2>{editMode ? 'Edit Equipment' : 'Add Equipment'}</h2>
                <button className="close-btn" onClick={() => setShowModal(false)}>×</button>
              </div>
              <form onSubmit={handleSubmit}>
                <div className="form-group">
                  <label>Name:</label>
                  <input
                    type="text"
                    value={formData.name}
                    onChange={(e) => setFormData({...formData, name: e.target.value})}
                    required
                  />
                </div>
                <div className="form-group">
                  <label>Category:</label>
                  <select
                    value={formData.category}
                    onChange={(e) => setFormData({...formData, category: e.target.value})}
                  >
                    <option value="sports">Sports Equipment</option>
                    <option value="lab">Lab Equipment</option>
                    <option value="camera">Camera & Photography</option>
                    <option value="musical">Musical Instruments</option>
                    <option value="project">Project Materials</option>
                    <option value="other">Other</option>
                  </select>
                </div>
                <div className="form-group">
                  <label>Description:</label>
                  <textarea
                    value={formData.description}
                    onChange={(e) => setFormData({...formData, description: e.target.value})}
                    rows="3"
                  ></textarea>
                </div>
                <div className="form-group">
                  <label>Condition:</label>
                  <select
                    value={formData.condition}
                    onChange={(e) => setFormData({...formData, condition: e.target.value})}
                  >
                    <option value="excellent">Excellent</option>
                    <option value="good">Good</option>
                    <option value="fair">Fair</option>
                    <option value="poor">Poor</option>
                  </select>
                </div>
                <div className="form-group">
                  <label>Total Quantity:</label>
                  <input
                    type="number"
                    min="1"
                    value={formData.quantity}
                    onChange={(e) => setFormData({...formData, quantity: e.target.value})}
                    required
                  />
                </div>
                <div className="form-group">
                  <label>Available Quantity:</label>
                  <input
                    type="number"
                    min="0"
                    value={formData.available_quantity}
                    onChange={(e) => setFormData({...formData, available_quantity: e.target.value})}
                    required
                  />
                </div>
                {message && <div className="error">{message}</div>}
                <button type="submit">{editMode ? 'Update' : 'Add'}</button>
              </form>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default EquipmentManage;

