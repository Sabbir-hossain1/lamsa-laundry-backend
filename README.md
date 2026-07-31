# 🧺 Lamsa Laundry Backend

A scalable and RESTful backend API for a modern **Laundry Service Management System**, built with **Django**, **Django REST Framework**, and **PostgreSQL**. This project provides APIs to manage customers, laundry orders, services, pricing, pickups, deliveries, payments, and administrative operations.

> Built with clean architecture, scalability, and maintainability in mind.

---

# 📖 About

The **Lamsa Laundry Backend** powers a laundry management platform where customers can place laundry orders, schedule pickups and deliveries, track order progress, and make payments. Administrators and staff can efficiently manage services, pricing, customers, orders, and operational workflows.

This project follows RESTful API best practices and is designed to serve web and mobile applications.

---

# ✨ Features

## 👤 Authentication & Authorization

* Custom User Model
* JWT Authentication
* Role-Based Access Control (RBAC)
* User Groups & Permissions
* Profile Management
* Password Change & Reset

---

## 👥 Customer Management

* Customer Registration
* Customer Profiles
* Address Management
* Order History
* Account Management

---

## 🧺 Laundry Services

* Service Categories
* Laundry Service Types
* Pricing Management
* Special Instructions
* Service Availability

---

## 📦 Order Management

* Create Laundry Orders
* Pickup Scheduling
* Delivery Scheduling
* Order Status Tracking
* Order Timeline
* Order History
* Cancel Orders

---

## 🚚 Pickup & Delivery

* Pickup Address
* Delivery Address
* Assigned Delivery Staff
* Pickup & Delivery Status
* Delivery Tracking

---

## 💳 Payments

* Payment Management
* Multiple Payment Methods
* Payment Status
* Transaction Records
* Invoice Support

---

## 🔔 Notifications

* Order Confirmation
* Pickup Notifications
* Delivery Notifications
* Payment Notifications
* Push Notifications (FCM)
* Email Notifications

---

## 📊 Admin Dashboard

* Customer Management
* Staff Management
* Laundry Order Management
* Service Management
* Pricing Management
* Reports & Analytics

---

# 🛠 Tech Stack

* Python 3
* Django
* Django REST Framework
* PostgreSQL
* JWT Authentication
* Pillow
* Swagger / OpenAPI
* Docker (Optional)
* Redis (Optional)
* Celery (Optional)

---

# 📁 Project Structure

```text
lamsa-laundry-backend/
│
├── apps/
│   ├── accounts/
│   ├── customers/
│   ├── laundry/
│   ├── orders/
│   ├── payments/
│   ├── notifications/
│   ├── common/
│   └── ...
│
├── config/
├── media/
├── static/
├── requirements.txt
├── manage.py
└── README.md
```

> The project structure may evolve as new modules and features are added.

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/Sabbir-hossain1/lamsa-laundry-backend.git
```

```bash
cd lamsa-laundry-backend
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

### macOS / Linux

```bash
python3 -m venv venv
```

---

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=laundry_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

ALLOWED_HOSTS=127.0.0.1,localhost
```

---

## Apply Database Migrations

```bash
python manage.py migrate
```

---

## Create a Superuser

```bash
python manage.py createsuperuser
```

---

## Run the Development Server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

# 📚 API Documentation

If API documentation is enabled:

```text
/swagger/
/redoc/
/api/docs/
```

---

# 🔐 Authentication

The API uses **JWT Authentication**.

Typical authentication flow:

1. Register
2. Login
3. Receive Access Token
4. Include the token in API requests

```http
Authorization: Bearer <access_token>
```

---

# 📌 Core Modules

* Authentication
* Users
* Customers
* Laundry Services
* Orders
* Pickups
* Deliveries
* Payments
* Notifications
* Reports
* Dashboard

---

# 🧪 Running Tests

Run the test suite with:

```bash
python manage.py test
```

---

# 🚀 Future Improvements

* Real-time Order Tracking
* SMS Notifications
* Online Payment Gateway Integration
* QR Code Order Tracking
* Loyalty & Rewards Program
* Discount & Coupon System
* Multi-Branch Support
* Multi-Language Support
* Docker Deployment
* CI/CD Pipeline

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Sabbir Hossain**

Backend Developer | Python • Django • Django REST Framework

GitHub: https://github.com/Sabbir-hossain1

---

# ⭐ Support

If you find this project helpful, consider giving it a **⭐ Star** on GitHub. It helps others discover the project and encourages continued development.

---

## 🚀 Clean Code. Reliable APIs. Better Laundry Management.

*"Building scalable backend systems, one API at a time."*
