# 📚 Library Management System

A console-based **Library Management System** developed in **Python** using **Object-Oriented Programming (OOP)** and **File Handling**.

The project allows librarians to manage books, members, book issues, returns, and reports through a simple menu-driven interface. All data is stored in text files, so records remain available even after the program is closed.

---

## 🚀 Features

### 📖 Book Management
- Add Book
- View Books
- Search Book
- Update Book
- Delete Book

### 👤 Member Management
- Add Member
- View Members
- Search Member
- Update Member
- Delete Member

### 📚 Book Issue
- Issue books to members
- Checks book availability
- Prevents issuing unavailable books
- Stores issue records

### 🔄 Book Return
- Return issued books
- Updates available copies
- Preserves complete issue history by creating a return record

### 📊 Reports
- View Available Books
- View Issued Books
- View All Members

### 💾 Data Persistence
All records are automatically stored using text files:
- books.txt
- members.txt
- issue.txt

---

# 🛠 Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- File Handling
- Modular Programming

No external libraries are required.

---

# 📂 Project Structure

```
Library-Management-System/
│
├── main.py
├── book.py
├── book_database.py
├── member.py
├── member_database.py
├── issue.py
├── issue_database.py
│
├── books.txt
├── members.txt
├── issue.txt
│
└── README.md
```

---

# ▶️ How to Run

1. Clone the repository

```
git clone <repository-url>
```

2. Open the project folder

3. Run

```
python main.py
```

---

# 🖥 Main Menu

```
====== Library Management System ======

1. Book Management
2. Member Management
3. Issue Book
4. Return Book
5. Reports
6. Save
7. Exit
```

---

# 📖 Book Management

- Add Book
- View Book
- Search Book
- Update Book
- Delete Book

---

# 👤 Member Management

- Add Member
- View Members
- Search Member
- Update Member
- Delete Member

---

# 📑 Reports

- Available Books
- Issued Books
- Members List

---

# 📁 Data Storage

The project stores all information in text files.

### Books

```
books.txt
```

### Members

```
members.txt
```

### Issues

```
issue.txt
```

This ensures data is preserved after the application is closed.

---

# ⭐ Project Highlights

- Object-Oriented Design
- Modular Code Structure
- CRUD Operations
- File Handling
- Menu Driven Interface
- Search Functionality
- Data Persistence
- Issue & Return Management
- Report Generation

---

# 🔮 Future Improvements

- User Login System
- Fine Calculation
- Due Date Reminder
- SQLite/MySQL Database Support
- Graphical User Interface (GUI)
- Barcode Scanner Support
- Search by Title/Author
- Export Reports to PDF/Excel

---

# 👨‍💻 Author

**Sardar Nirmaljeet Singh**

Python Developer (Learning Journey)

GitHub:
https://github.com/jeetnirmal010

---

# 📄 License

This project is created for learning and educational purposes.