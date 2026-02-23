# Mart Ecommerce API 🛒

A professional, secure, and clean Single-Vendor Ecommerce API built with **FastAPI** and **SQLAlchemy**.

## 🚀 Features

- **User Management**: Secure user registration with **Bcrypt** password hashing.
- **Product Management**: Create and list products with detailed attributes.
- **Order System**: 
  - Automated stock management (stock decreases on order).
  - Backend-calculated total prices for security.
  - Order status tracking (default: `pending`).
- **Database**: SQLite integration with SQLAlchemy ORM.
- **Validation**: Strict data validation using Pydantic schemas.

## 🛠️ Technology Stack

- **Framework**: FastAPI
- **Database**: SQLite (via SQLAlchemy)
- **Security**: Passlib (Bcrypt) for hashing.
- **Validation**: Pydantic v2

## 📂 Project Structure

```text
├── app/
│   ├── routers/       # API Routes (Products, Orders, Users)
│   ├── models.py      # Database Tables
│   ├── schemas.py     # Pydantic Validation Models
│   ├── crud.py        # Database Operations
│   ├── database.py    # DB Connection Setup
│   ├── utils.py       # Security & Helper Functions
│   └── main.py        # Application Entry Point
├── mart.db            # SQLite Database
├── requirements.txt   # Dependencies
└── README.md          # Project Documentation
```

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/altaf59/single-vendor-ecommerce-api.git
   cd single-vendor-ecommerce-api
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

5. **API Documentation**:
   Once the server is running, visit:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## 📝 License

This project is open-source. Feel free to use and modify it!
