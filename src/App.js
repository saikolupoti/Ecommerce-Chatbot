// src/App.js
import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes, Navigate } from "react-router-dom";
import Chatbot from "./components/Chatbot";
import Login from "./components/Login";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const savedUser = localStorage.getItem("username");
    if (savedUser) setUser(savedUser);
  }, []);

  return (
    <Router>
      <Routes>
        <Route
          path="/login"
          element={<Login onLogin={(username) => setUser(username)} />}
        />
        <Route
          path="/chatbot"
          element={
            user ? <Chatbot username={user} /> : <Navigate to="/login" replace />
          }
        />
        {/* Redirect root to login */}
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    </Router>
  );
}

export default App;
