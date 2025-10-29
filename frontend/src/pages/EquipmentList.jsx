import { useState, useEffect } from 'react';
import { equipmentAPI } from '../services/api';
import './EquipmentList.css';

function EquipmentList() {
  const [equipment, setEquipment] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchEquipment();
  }, []);

  const fetchEquipment = async () => {
    try {
      setLoading(true);
      const response = await equipmentAPI.getAll();
      setEquipment(response.data.results || response.data);
      setError(null);
    } catch (err) {
      setError('Failed to fetch equipment. Please make sure the backend is running.');
      console.error('Error fetching equipment:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Loading equipment...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="equipment-list">
      <div className="equipment-container">
        <h1>Equipment Inventory</h1>
        
        {equipment.length === 0 ? (
          <div className="no-data">
            <p>No equipment found. Please add equipment through the admin panel.</p>
          </div>
        ) : (
          <div className="equipment-grid">
            {equipment.map((item) => (
              <div key={item.id} className="equipment-card">
                <h3>{item.name}</h3>
                <p className="equipment-category">Category: {item.category}</p>
                <p className="equipment-description">{item.description}</p>
                <div className="equipment-quantity">
                  <span>Available: {item.quantity_available}</span>
                  <span>Total: {item.quantity_total}</span>
                </div>
                <div className={`equipment-status ${item.is_available ? 'available' : 'unavailable'}`}>
                  {item.is_available ? '✓ Available' : '✗ Unavailable'}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default EquipmentList;
