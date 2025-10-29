import './Home.css';

function Home() {
  return (
    <div className="home">
      <div className="home-container">
        <h1>Welcome to Equipment Lending System</h1>
        <p className="home-description">
          A comprehensive system for managing equipment lending in educational institutions.
        </p>
        
        <div className="feature-grid">
          <div className="feature-card">
            <h3>📦 Equipment Management</h3>
            <p>Track and manage all your equipment inventory in one place.</p>
          </div>
          
          <div className="feature-card">
            <h3>📝 Lending Records</h3>
            <p>Keep track of all lending transactions and their status.</p>
          </div>
          
          <div className="feature-card">
            <h3>👥 User Management</h3>
            <p>Manage users and their borrowing privileges efficiently.</p>
          </div>
          
          <div className="feature-card">
            <h3>📊 Reports</h3>
            <p>Generate reports and insights on equipment usage.</p>
          </div>
        </div>
        
        <div className="getting-started">
          <h2>Getting Started</h2>
          <ol>
            <li>Browse available equipment in the Equipment section</li>
            <li>View lending records and their current status</li>
            <li>Use the admin panel to manage the system</li>
          </ol>
        </div>
      </div>
    </div>
  );
}

export default Home;
