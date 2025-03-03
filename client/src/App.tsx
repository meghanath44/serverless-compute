import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css'
import Welcome from "./Welcome";
import Login from "./login";
import Signup from "./Signup";

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
