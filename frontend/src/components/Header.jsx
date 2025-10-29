import { Link } from 'react-router-dom';
import './Header.css';

function Header() {
  return (
    <header className="header">
      <div className="header-container">
        <h1 className="header-title">
          <Link to="/">Equipment Lending System</Link>
        </h1>
        <nav className="header-nav">
          <Link to="/" className="nav-link">Home</Link>
          <Link to="/equipment" className="nav-link">Equipment</Link>
          <Link to="/lending" className="nav-link">Lending Records</Link>
        </nav>
      </div>
    </header>
  );
}

export default Header;
