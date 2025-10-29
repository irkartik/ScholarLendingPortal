import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Home from './pages/Home';
import EquipmentList from './pages/EquipmentList';
import LendingRecords from './pages/LendingRecords';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app">
        <Header />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/equipment" element={<EquipmentList />} />
            <Route path="/lending" element={<LendingRecords />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
