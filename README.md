# 📚 Smart Library Management System

A Python-based console application for managing a public library, built to demonstrate core Object-Oriented Programming (OOP) principles. The system handles book borrowing and returning while enforcing distinct permissions based on user roles.

## 🚀 Features

- **Role-Based Permissions:**
  - **Student:** Can borrow a maximum of 3 books[cite: 1].
  - **Teacher:** Can borrow a maximum of 5 books[cite: 1].
  - **Librarian:** Has administrative privileges to add, remove, search, and view all books[cite: 1].
- **Library Operations:** Users can view all books, filter available books, view their borrowed books, borrow new books, and return them[cite: 1].
- **Robust Exception Handling:** The program handles invalid menu choices, unavailable book borrowing, returning unborrowed books, and invalid numeric inputs without crashing[cite: 1].
- **Interactive CLI:** The application displays a continuous menu loop until the user chooses to exit[cite: 1].

## 🧠 OOP Concepts Demonstrated

- **Abstraction:** The `User` class is an Abstract Base Class (ABC) with abstract methods like `show_menu()` and `borrow()`, enforcing a template for all users[cite: 1].
- **Inheritance:** `Student`, `Teacher`, and `Librarian` are child classes that inherit attributes and common behaviors from the `User` parent class[cite: 1].
- **Polymorphism:** Child classes override the `borrow()` and `show_menu()` methods to apply logic specific to their roles[cite: 1].
- **Encapsulation:** Sensitive data, such as available book copies, is hidden using private attributes (`__available_copies`) and accessed safely via properties and methods[cite: 1].

## 🛠️ Prerequisites

- Python 3.x installed on your local machine.

## ⚙️ How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Mo7ammed-Ja3far/iti-tasks/tree/library_management_system](https://github.com/Mo7ammed-Ja3far/iti-tasks/tree/library_management_system)
   cd Smart-Library-Management-System
   ```
