import { useState, useEffect } from 'react';
import { lendingAPI } from '../services/api';
import './LendingRecords.css';

function LendingRecords() {
  const [records, setRecords] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {
    try {
      setLoading(true);
      const response = await lendingAPI.getAll();
      setRecords(response.data.results || response.data);
      setError(null);
    } catch (err) {
      setError('Failed to fetch lending records. Please make sure the backend is running.');
      console.error('Error fetching records:', err);
    } finally {
      setLoading(false);
    }
  };

  const getStatusClass = (status) => {
    const statusClasses = {
      pending: 'status-pending',
      approved: 'status-approved',
      borrowed: 'status-borrowed',
      returned: 'status-returned',
      cancelled: 'status-cancelled',
    };
    return statusClasses[status] || '';
  };

  if (loading) {
    return <div className="loading">Loading lending records...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="lending-records">
      <div className="records-container">
        <h1>Lending Records</h1>
        
        {records.length === 0 ? (
          <div className="no-data">
            <p>No lending records found. Records will appear here once equipment is borrowed.</p>
          </div>
        ) : (
          <div className="records-list">
            {records.map((record) => (
              <div key={record.id} className="record-card">
                <div className="record-header">
                  <h3>{record.equipment_name}</h3>
                  <span className={`status-badge ${getStatusClass(record.status)}`}>
                    {record.status.toUpperCase()}
                  </span>
                </div>
                <div className="record-details">
                  <p><strong>User:</strong> {record.user_name}</p>
                  <p><strong>Quantity:</strong> {record.quantity}</p>
                  {record.borrow_date && (
                    <p><strong>Borrowed:</strong> {new Date(record.borrow_date).toLocaleDateString()}</p>
                  )}
                  {record.due_date && (
                    <p><strong>Due:</strong> {new Date(record.due_date).toLocaleDateString()}</p>
                  )}
                  {record.return_date && (
                    <p><strong>Returned:</strong> {new Date(record.return_date).toLocaleDateString()}</p>
                  )}
                  {record.notes && (
                    <p className="record-notes"><strong>Notes:</strong> {record.notes}</p>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default LendingRecords;
