import React, { useState, useEffect } from "react";
import "./Chatbot.css";

function Chatbot() {
  const greetingMessage = {
    from: "bot",
    text: "🤖 Hello! I'm your shopping assistant. What are you looking for today?",
    timestamp: new Date().toLocaleTimeString()
  };

  const [messages, setMessages] = useState(() => {
    const stored = localStorage.getItem("chat_history");
    return stored ? JSON.parse(stored) : [greetingMessage];
  });

  const [input, setInput] = useState("");
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [filters, setFilters] = useState({
    minPrice: "",
    maxPrice: "",
    minRating: ""
  });

  useEffect(() => {
    localStorage.setItem("chat_history", JSON.stringify(messages));
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = {
      from: "user",
      text: input,
      timestamp: new Date().toLocaleTimeString()
    };

    try {
      const response = await fetch("https://ecommerce-chatbot-backend-jn1d.onrender.com/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input })
      });

      const data = await response.json();
      let newMessages = [...messages, userMessage];

      if (Array.isArray(data) && data.length > 0) {
        const productMessages = data.map(product => ({
          from: "bot",
          product,
          timestamp: new Date().toLocaleTimeString()
        }));
        newMessages = [...newMessages, ...productMessages];
        setFilteredProducts([]);
      } else {
        newMessages.push({
          from: "bot",
          text: "❌ Sorry, no matching products found.",
          timestamp: new Date().toLocaleTimeString()
        });
      }

      setMessages(newMessages);
      setInput("");
    } catch (error) {
      setMessages(prev => [
        ...prev,
        userMessage,
        {
          from: "bot",
          text: "⚠️ Something went wrong. Try again later.",
          timestamp: new Date().toLocaleTimeString()
        }
      ]);
    }
  };

  const handleFilterChange = (e) => {
    setFilters({
      ...filters,
      [e.target.name]: e.target.value
    });
  };

  const applyFilters = async () => {
    try {
      const response = await fetch("https://ecommerce-chatbot-backend-jn1d.onrender.com/filter", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          minPrice: parseFloat(filters.minPrice) || 0,
          maxPrice: parseFloat(filters.maxPrice) || Infinity,
          minRating: parseFloat(filters.minRating) || 0
        })
      });

      const data = await response.json();
      setFilteredProducts(data);
    } catch (error) {
      console.error("Filter fetch failed:", error);
    }
  };

  const handleReset = () => {
    const resetMessages = [greetingMessage];
    setMessages(resetMessages);
    localStorage.removeItem("chat_history");
    setFilteredProducts([]);
    setFilters({
      minPrice: "",
      maxPrice: "",
      minRating: ""
    });
  };

  return (
    <div className="chat-container">
      {/* Chat UI */}
      <div className="chat-box">
        {(filteredProducts.length > 0 ? filteredProducts : messages).map((msg, index) =>
          msg.product ? (
            <div className="product-card message bot fade-in" key={index}>
              <img
                src={msg.product.image_url}
                alt={msg.product.name}
                style={{ width: "100%", borderRadius: "10px", marginBottom: "0.5rem" }}
              />
              <strong>{msg.product.name}</strong>
              <p>₹{msg.product.price} | ⭐ {msg.product.rating}</p>
              <small>{msg.product.availability}</small>
              <div className="timestamp">{msg.timestamp}</div>
            </div>
          ) : (
            <div className={`message ${msg.from} fade-in`} key={index}>
              {msg.from === "bot" ? `🤖 ${msg.text}` : msg.text}
              <div className="timestamp">{msg.timestamp}</div>
            </div>
          )
        )}
      </div>

      {/* Filter UI aligned in one line at bottom */}
      <div
        className="filter-container"
        style={{
          position: "absolute",
          bottom: "60px",
          left: "50%",
          transform: "translateX(-50%)",
          display: "grid",
          gridAutoFlow: "column",
          alignItems: "center",
          gap: "10px",
          padding: "10px 20px",
          borderRadius: "15px",
          fontSize: "1rem",
          background: "rgba(255, 255, 255, 0.1)",
          backdropFilter: "blur(10px)",
          boxShadow: "0 4px 20px rgba(0,0,0,0.2)"
        }}
      >
        <strong style={{ color: "#fff" }}>Filter:</strong>
        <input
          type="text"
          name="minPrice"
          placeholder="Min ₹"
          value={filters.minPrice}
          onChange={handleFilterChange}
          style={{ fontSize: "0.85rem", padding: "5px", width: "65px" }}
        />
        <input
          type="text"
          name="maxPrice"
          placeholder="Max ₹"
          value={filters.maxPrice}
          onChange={handleFilterChange}
          style={{ fontSize: "0.85rem", padding: "5px", width: "65px" }}
        />
        <input
          type="text"
          name="minRating"
          placeholder="Min ★"
          value={filters.minRating}
          onChange={handleFilterChange}
          style={{ fontSize: "0.85rem", padding: "5px", width: "65px" }}
        />
        <button onClick={applyFilters} style={{ fontSize: "0.85rem", padding: "5px 8px" }}>
          Apply
        </button>
        <button
          onClick={handleReset}
          style={{ fontSize: "0.85rem", padding: "5px 8px", backgroundColor: "#777", color: "#fff" }}
        >
          Reset
        </button>
      </div>

      <div className="chat-input">
        <input
          type="text"
          placeholder="Type message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          style={{ fontSize: "0.9rem", padding: "8px" }}
        />
        <button onClick={sendMessage} style={{ fontSize: "0.9rem", padding: "8px 12px" }}>Send</button>
      </div>
    </div>
  );
}

export default Chatbot;
