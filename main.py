from abc import ABC, abstractmethod

class Book:
    def __init__(self, book_id, title, author, category, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.__available_copies = available_copies

    @property
    def available_copies(self):
        return self.__available_copies

    def display_info(self):
        print(f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Category: {self.category} | Available: {self.__available_copies}")

    def borrow_book(self):
        if self.__available_copies <= 0:
            raise ValueError("This book is currently unavailable.")
        self.__available_copies -= 1

    def return_book(self):
        self.__available_copies += 1

class User(ABC):
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.name = name
        self.borrowed_books = []

    @property
    def user_id(self):
        return self.__user_id

    @abstractmethod
    def show_menu(self):
        pass

    @abstractmethod
    def borrow(self, book):
        pass

    def return_book(self, book):
        if book not in self.borrowed_books:
            raise ValueError("You cannot return a book you have never borrowed.")
        book.return_book()
        self.borrowed_books.remove(book)

class Student(User):
    def borrow(self, book):
        if len(self.borrowed_books) >= 3:
            raise ValueError("Student borrow limit reached (Maximum 3 books).")
        book.borrow_book()
        self.borrowed_books.append(book)

    def show_menu(self):
        print("\n1. Display all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Display available books only")
        print("5. Display borrowed books")
        print("6. Exit")

class Teacher(User):
    def borrow(self, book):
        if len(self.borrowed_books) >= 5:
            raise ValueError("Teacher borrow limit reached (Maximum 5 books).")
        book.borrow_book()
        self.borrowed_books.append(book)

    def show_menu(self):
        print("\n1. Display all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Display available books only")
        print("5. Display borrowed books")
        print("6. Exit")

class Librarian(User):
    def borrow(self, book):
        book.borrow_book()
        self.borrowed_books.append(book)

    def add_book(self, library_books, book):
        library_books.append(book)

    def remove_book(self, library_books, book):
        if book in library_books:
            library_books.remove(book)

    def search_books(self, library_books, keyword):
        return [b for b in library_books if keyword.lower() in b.title.lower()]

    def view_all_books(self, library_books):
        if not library_books:
            print("The library is currently empty.")
        for book in library_books:
            book.display_info()

    def show_menu(self):
        print("\n1. Add a new book")
        print("2. Display all books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Display available books only")
        print("6. Display borrowed books")
        print("7. Exit")

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.current_user = None

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def display_all_books(self):
        if not self.books:
            print("No books available in the library.")
        for book in self.books:
            book.display_info()

    def display_available_books(self):
        available = [book for book in self.books if book.available_copies > 0]
        if not available:
            print("No books are currently available.")
        for book in available:
            book.display_info()

    def display_borrowed_books(self):
        if not self.current_user.borrowed_books:
            print("You have not borrowed any books.")
        for book in self.current_user.borrowed_books:
            book.display_info()

    def handle_librarian_choice(self, choice):
        if choice == 1:
            try:
                book_id = input("Enter Book ID: ")
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                category = input("Enter Category: ")
                copies = int(input("Enter Available Copies: "))
                new_book = Book(book_id, title, author, category, copies)
                self.current_user.add_book(self.books, new_book)
                print("Book added successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid number for copies.")
        elif choice == 2:
            self.current_user.view_all_books(self.books)
        elif choice == 3:
            book_id = input("Enter Book ID to borrow: ")
            book = self.find_book_by_id(book_id)
            if book:
                self.current_user.borrow(book)
                print("Book borrowed successfully.")
            else:
                print("Book not found.")
        elif choice == 4:
            book_id = input("Enter Book ID to return: ")
            book = self.find_book_by_id(book_id)
            if book:
                self.current_user.return_book(book)
                print("Book returned successfully.")
            else:
                print("Book not found.")
        elif choice == 5:
            self.display_available_books()
        elif choice == 6:
            self.display_borrowed_books()
        elif choice == 7:
            return False
        else:
            print("Invalid menu choice.")
        return True

    def handle_member_choice(self, choice):
        if choice == 1:
            self.display_all_books()
        elif choice == 2:
            book_id = input("Enter Book ID to borrow: ")
            book = self.find_book_by_id(book_id)
            if book:
                self.current_user.borrow(book)
                print("Book borrowed successfully.")
            else:
                print("Book not found.")
        elif choice == 3:
            book_id = input("Enter Book ID to return: ")
            book = self.find_book_by_id(book_id)
            if book:
                self.current_user.return_book(book)
                print("Book returned successfully.")
            else:
                print("Book not found.")
        elif choice == 4:
            self.display_available_books()
        elif choice == 5:
            self.display_borrowed_books()
        elif choice == 6:
            return False
        else:
            print("Invalid menu choice.")
        return True

    def run(self):
        print("Welcome to the Smart Library Management System")
        print("1. Login as Student")
        print("2. Login as Teacher")
        print("3. Login as Librarian")
        
        try:
            role_choice = int(input("Select your role (1-3): "))
            if role_choice == 1:
                self.current_user = Student("S1", "Student User")
            elif role_choice == 2:
                self.current_user = Teacher("T1", "Teacher User")
            elif role_choice == 3:
                self.current_user = Librarian("L1", "Librarian User")
            else:
                print("Invalid role selected. Exiting.")
                return
        except ValueError:
            print("Invalid numeric input. Exiting.")
            return

        running = True
        while running:
            self.current_user.show_menu()
            try:
                choice = int(input("Enter your choice: "))
                if isinstance(self.current_user, Librarian):
                    running = self.handle_librarian_choice(choice)
                else:
                    running = self.handle_member_choice(choice)
            except ValueError as e:
                if "invalid literal for int()" in str(e):
                    print("Invalid numeric input. Please enter a number.")
                else:
                    print(f"Error: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.run()