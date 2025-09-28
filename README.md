# 💰 Expense Tracker Web (Flask)

A simple **Flask web app** to track daily expenses.  
Expenses are stored in a CSV file, and the app allows you to **add new expenses** and **view total expenses**.

---

## 🚀 Features
- Add expense details (Date, Product, Amount, Payer)
- View all expenses in a table
- Automatically calculate total amount
- Stores data in `expense.csv` (auto-created if missing)

---

## 📂 Project Structure
expense_tracker_web/
│── app.py # Main Flask application
│── requirements.txt # Python dependencies
│── .gitignore # Ignored files (like venv, CSV data)
│── README.md # Project documentation
│
└── templates/ # HTML templates
│── index.html
│── add.html
│── view.html
