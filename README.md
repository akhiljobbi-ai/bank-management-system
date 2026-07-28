# 🏦 Bank Management System

A console-based Bank Management System developed in Python using Object-Oriented Programming principles.

This project simulates basic banking operations such as creating accounts, depositing and withdrawing money, checking balances, changing PINs, and calculating interest. It was built to strengthen OOP concepts, program design, and Git/GitHub workflow.

---

## ✨ Features

- ✅ Create a new bank account
- 💰 Deposit money
- 💸 Withdraw money (PIN protected)
- 📊 Check account balance
- 👤 Display account details
- 🔐 Change account PIN
- 📈 Calculate interest for Savings Accounts
- 🔍 Search accounts using account number
- 🚫 Prevent duplicate account numbers

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Git
- GitHub

---

## 📚 OOP Concepts Practiced

- Classes and Objects
- Constructors (`__init__`)
- Instance Variables
- Class Variables
- Methods
- Encapsulation
- Helper Methods
- Code Reusability

---

## 📂 Project Structure

```
Bank Management System
│
├── BankAccount Class
│   ├── deposit()
│   ├── withdraw()
│   ├── check_balance()
│   ├── change_pin()
│   ├── display_account()
│   ├── add_interest()
│   └── verify_pin()
│
├── find_account()
│
└── Menu-Driven Application
```

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/akhiljobbi-ai/student-management-system.git
```

2. Navigate to the project folder

```bash
cd student-management-system
```

3. Run the program

```bash
python bank_management.py
```

---

## 📋 Menu

```
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Display Account
6. Change PIN
7. Add Interest
8. Exit
```

---

## ⚠️ Current Limitations

- Account data is stored only in memory.
- All accounts are lost when the program exits.
- User input validation for non-numeric values is limited.

These limitations will be addressed in future versions.

---

## 🚀 Planned Improvements

- 💾 File Handling (Save and Load Accounts)
- 🗄️ SQLite/MySQL Database Integration
- 🌐 GUI or Web Interface
- 🔄 Transaction History
- 🧪 Improved Input Validation
- 🔒 Better Authentication and Security

---

## 👨‍💻 Author

**Akhil Jobbi**

Second-Year AI & Data Science Student

GitHub: https://github.com/akhiljobbi-ai

---

## 🎯 Learning Outcome

This project was built to practice software engineering fundamentals, including:

- Designing classes and objects
- Writing reusable methods
- Applying business logic
- Input validation
- Menu-driven programming
- Git and GitHub workflow
- Code organization and refactoring

It serves as a foundation for future projects involving file handling, databases, backend development, and machine learning.