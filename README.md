# 🛒 Mart Ecommerce API (Single Vendor)

A professional, secure, and clean FastAPI-based Ecommerce API designed for a Single Vendor store.

## 🚀 Features

- **Personalized Admin Dashboard**: Separate section for the Shop Owner.
- **Secure Admin Registration**: Register using a secret code to prevent unauthorized access.
- **Product Management**: Full CRUD (Create, Read, Update, Delete) functionality for products.
- **Customer Shopping**: Customers can browse products, search by name, and place orders.
- **Order Tracking**: Automated total price calculation and real-time stock management.
- **Password Security**: Modern Bcrypt hashing for all users.

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Database**: SQLite (SQLAlchemy ORM)
- **Security**: Bcrypt Hashing
- **Validation**: Pydantic v2

## 📂 Project Structure

```text
app/
├── main.py          # Main Entry Point
├── models.py        # Database Models
├── schemas.py       # Pydantic Schemas
├── crud.py          # Database Operations
├── database.py      # DB Connection
├── utils.py         # Security Helpers (Hasing)
├── config.py        # Settings & Secret Keys
└── routers/
    ├── admin.py     # Admin/Vendor Endpoints
    ├── products.py  # Public Product Catalog
    ├── user.py      # Customer Accounts
    └── orders.py    # Shopping & Orders
```

## 🔐 Admin Configuration

To register as an admin, use the following details in the `/admin/register` endpoint:
- **Secret Code**: `ALTAF_ADMIN_786` (Configurable in `app/config.py`)

## 🚥 Main Endpoints

### 👤 User / Customer
- `POST /users/` - Register as a new customer.
- `POST /users/login` - Login to your account.

### 🍱 Products (Public)
- `GET /products/` - View all products.
- `GET /products/?search=name` - Search products by name.

### 🛡️ Admin (Vendor)
- `POST /admin/register` - Create an admin account (requires Secret Code).
- `POST /admin/login` - Admin login.
- `POST /admin/products` - Add new stock.
- `PUT /admin/products/{id}` - Update product details.
- `DELETE /admin/products/{id}` - Remove a product.
- `GET /admin/orders` - View all customer orders.

### 📦 Orders
- `POST /orders/` - Place a new order (Autocalculates total & updates stock).
- `GET /orders/{id}` - View specific order details.

## 🏃 How to Run

1. **Install Dependencies**:
   ```bash
   pip install fastapi uvicorn sqlalchemy bcrypt
   ```

2. **Run Server**:
   ```bash
   uvicorn app.main:app --reload
   ```

3. **Explore Documentation**:
   Open `http://127.0.0.1:8000/docs` in your browser.

---
Built by **Altaf** with ❤️ using FastAPI.
