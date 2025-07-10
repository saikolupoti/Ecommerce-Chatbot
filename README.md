# 🛍️ E-commerce Chatbot

A fully functional AI-powered chatbot interface that assists users in browsing products from a mock e-commerce platform. Built with a React frontend and a Flask backend, this chatbot supports product search, real-time filtering, session management, and interactive UI.

## 🔗 Live Demo

- 🔹 **Frontend:** [https://ecommerce-chatbot-gilt.vercel.app/login](https://ecommerce-chatbot-gilt.vercel.app/login)
- 🔹 **Backend API:** [https://ecommerce-chatbot-backend-jn1d.onrender.com](https://ecommerce-chatbot-backend-jn1d.onrender.com)

---

## ✨ Features

- 💬 Conversational UI for product search and exploration  
- 🧠 Intelligent backend processing with Flask  
- 📦 Mock inventory with 20 product entries  
- ♻️ Reset and clear conversation options  
- 🌐 Responsive UI (desktop, tablet, and mobile)

---

## 📁 Project Structure

```
chatbot-backend/
├── app.py                 # Main Flask application
├── db_setup.py           # Script to populate mock product data
├── products.db           # SQLite database
├── requirements.txt      # Python dependencies
├── chatbot-frontend/
│   └── frontend/         # React app (contains all frontend source code)
│       ├── public/
│       ├── src/
│       ├── package.json
│       └── ...
└── README.md
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Node.js (v18 or higher)
- Python (3.8+)
- Git

---

### 🧪 Backend Setup (Flask)

1. **Clone the repository**  
   ```bash
   git clone https://github.com/saikolupoti/ecomnerce-chatbot-backend.git
   cd ecomnerce-chatbot-backend
   ```

2. **Create a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate    # For Linux/macOS
   venv\Scripts\activate       # For Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend server**  
   ```bash
   python app.py
   ```

---

### 💻 Frontend Setup (React)

1. **Navigate to frontend**  
   ```bash
   cd chatbot-frontend/frontend
   ```

2. **Install dependencies**  
   ```bash
   npm install
   ```

3. **Run development server**  
   ```bash
   npm start
   ```

---

## 🧠 Technologies Used

### Frontend:
- React.js
- HTML5, CSS3
- Vercel for deployment

### Backend:
- Flask (Python)
- SQLite3
- REST API
- Render for deployment

---

## 🗃️ Sample Use Cases

- **"Show me phones"**  
- **"Find me some headphones"**  
- **"Display watches"**

---

## 📌 Future Enhancements

- 🧾 Integration with real-time product APIs  
- 🔐 OAuth or Firebase authentication

---

## 📄 License

This project is licensed under the MIT License - feel free to use and customize it for personal or academic use.

---

## 🙋‍♂️ Author

**Kolupoti Sai Prakash**  
📫 [GitHub Profile](https://github.com/saikolupoti)  
📍 India

---

> Thank you for visiting! If you liked the project, consider giving it a ⭐️ on GitHub.
