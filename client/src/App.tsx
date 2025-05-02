import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css'
import Welcome from "./welcome";
import Login from "./Login";
import Signup from "./Signup";
import Home from "./home"

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/home" element={<Home />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
