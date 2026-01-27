# Banking Project – Flask, MySQL & React

A full-stack banking application built using **Python (Flask)** for the backend, **MySQL** for data persistence, and **React (Vite)** for the frontend.  
This project demonstrates object-oriented backend design, RESTful APIs, and a simple React-based user interface for common banking operations.

## Features

### Backend (Flask + MySQL)
- Object-oriented data models using SQLAlchemy
- Service-layer architecture for business logic
- REST APIs for:
  - Creating customers and accounts
  - Deposits and withdrawals
  - Account-to-account transfers
  - Transaction history retrieval
- Automatic database table creation
- Optional raw SQL schema provided

### Frontend (React + Vite)
- Simple and clean React UI
- Screens for:
  - Login (mock/demo)
  - Dashboard
  - Transfers
  - Transaction history
- React Router for navigation
- Axios for API communication

---

## Tech Stack

**Backend**
- Python
- Flask
- Flask-SQLAlchemy
- MySQL

**Frontend**
- React 18
- Vite
- Axios
- React Router

---

## Backend Design Overview

- **Models (`models.py`)**  
  Defines `Customer`, `Account`, and `Transaction` using SQLAlchemy.  
  Core operations like deposit and withdrawal are implemented as methods on the `Account` model.

- **Service Layer (`services.py`)**  
  All business logic is handled through a `BankService` class, keeping route handlers clean and maintainable.

- **Routes (`routes.py`)**  
  RESTful API endpoints under `/api/*` expose backend functionality to the frontend.

---

## Database Schema

The application supports:
- SQLAlchemy-managed tables (auto-created at runtime)
- Raw SQL schema via `schema.sql`

Tables:
- `customers`
- `accounts`
- `transactions`

---

## Running the Project Locally

### Prerequisites
- Python 3.9+
- Node.js 18+
- MySQL server running locally

---

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
```
Create a .env file inside backend/:
```bash
python3 -m venv .venv
```

Run the backend server:
```bash
python3 app.py
```
Backend runs on http://localhost:5000.

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Frontend runs on http://localhost:5173.

***Ensure Axios or Vite proxy is configured to forward requests to http://localhost:5000/api.***

## License

This project is open-source and intended for learning and portfolio use.