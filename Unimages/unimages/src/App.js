import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from 'react-router-dom'

import { About } from './pages/about/About';
import { Home } from './pages/home/Home';
import { Profile } from './pages/profile/Profile';
import { Contact } from './pages/contact/Contact';
import { Navigation } from './components/navigation/Navigation'
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
  return (
    <Router>
      <Navigation />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/allusers" element={<Navigate to="/profile" />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </Router>
  )
}

export default App
