
# 🏦 Bank Management System

A console-based Bank Management System built using **Python** and **Object-Oriented Programming (OOP)**. This project simulates basic banking operations, handles invalid user input, and stores account information permanently using CSV file handling.

---

## 📌 Features

- Create a new bank account
- Deposit money
- Withdraw money (with PIN verification)
- Check account balance
- Display account details
- Change account PIN
- Add interest to savings accounts
- Track the last transaction
- Persistent data storage using CSV
- Prevent duplicate account numbers
- Input validation using reusable helper functions
- Handle missing data files gracefully
- Properly handle commas inside CSV fields

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- File Handling
- CSV (`csv.reader` and `csv.writer`)
- Exception Handling
- Git & GitHub

---

## 📂 Project Structure

```text
Bank-Management-System/
│
├── Bank_Management_System.py
├── accounts.csv
├── README.md
└── .gitignore

## 💾 Data Persistence

Account data is stored in `accounts.txt`.

Whenever an account is created or modified, the program automatically updates the file so that all data is preserved even after the program is closed.

Example:

```
Akhil,101,5000,SAVINGS,1234,Deposited Rs.500
Rahul,102,8000,CURRENT,5678,Account Created
```

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/akhiljobbi-ai/bank-management-system.git
```

2. Navigate to the project folder.

```bash
cd Bank-Management-System
```

3. Run the program.

```bash
python Bank_Management_System.py
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

## 📖 Concepts Practiced

- Classes and Objects
- Constructors (`__init__`)
- Instance Variables
- Class Variables
- Methods
- Helper Functions
- Lists of Objects
- Searching Objects
- File Reading
- File Writing
- Data Parsing
- Data Persistence
- Input Validation

---

## 🚀 Future Improvements

- JSON support
- Database (SQL) integration
- Graphical User Interface (GUI)
- Transaction history
- Account deletion
- Better input validation

---

## 👨‍💻 Author

**Akhil Jobbi**

This project was built as part of my journey to become an AI/ML Engineer through hands-on software engineering projects.
