# 📚 Library Management System

A Django-based Library Management System designed for librarians to manage book issuance and returns efficiently. The system provides functionality to add new users, issue and return books, and send email notifications to users after each transaction.

🔗 **Project Repository:** [GitHub - KetanHegde/library_management_system](https://github.com/KetanHegde/library_management_system)

---

## ✨ Features

- 👤 **User Management**  
  Add, view, and manage library users.

- 📘 **Book Issuance and Returns**  
  Easily issue and return books, with transaction tracking.

- 📧 **Email Notifications**  
  Automated email alerts are sent to users for each transaction (issuance/return).

- 🗂️ **Transaction History**  
  Keep a record of all transactions for auditing and reference.

---

## 🚀 Technologies Used

- **Framework**: Django 5.0.6
- **Database**: Configurable via environment variables (e.g., PostgreSQL, MySQL, SQLite)
- **Email Integration**: SMTP (TLS-enabled, configurable via environment variables)
- **Environment Management**: `python-dotenv`

---

## 🔧 Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/KetanHegde/library_management_system.git
   cd library_management_system
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Configure Environment Variables**

   Create a `.env` file in the root directory and add:

   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True

   DATABASE_ENGINE=django.db.backends.postgresql  # or other backend
   DATABASE_NAME=your_db_name
   USER=your_db_user
   PASSWORD=your_db_password

   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST=smtp.example.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_PASSWORD=your_email_password
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Start the development server**

   ```bash
   python manage.py runserver
   ```

6. **Access the app**

   Visit `http://127.0.0.1:8000` in your browser.

---

## 📬 Email Notifications

The system sends confirmation emails to users after:

- A book is issued
- A book is returned

Make sure to configure valid email credentials in your `.env` file for SMTP functionality.

---

## 🛠 Developer Notes

- This project uses Django’s built-in admin interface for administrative tasks.
- Default time zone is set to `Asia/Kolkata`.
- All settings are securely managed via environment variables using `python-dotenv`.

---

## 📃 License

This project is licensed under the MIT License.
