# Library-Management-System-

Project Overview

This project is a simple library management system created with python. It shows object-oriented programming, modular programming, user-defined functions, and basic data managment.
This program allows users to add books to a library, view the books, and search for books by title or author.

Files

book.py

The book.py module contains the book class. The class represents a book and stores three pieces of information which are Title, Author, and ISBN. 
The book class also includes methods for displaying book information and returning the book's details as a dictionary. 

Library_manager.py

This file is the main program. It imports the book class from book.py and provides a menu that allows the user to 

1. Add a new book
2. List all books
3. Find a book
4. Exit the program

The program uses functions, a list of book objects, a while loop, and conditional statements to manage the library. 

How to Run the Program

Make sure python is installed on your computer
Place book.py and Library_manager.py in the same folder
Open the project folder in VS Code and open the terminal.
Run the program using python with file Library_manager.py
Follow the menu prompts to add, list, or search for books.

Object-Oriented Programmiing

The Book class acts as a blueprint for creating book objects. Each book object contains its own title, author, and ISBN. 
The __init__ method uses the information for each book, while the __str__ method provides a readable representation when a book object is printed.
The get_details method returns the book's information as a dictionary

Modular Design

The project is separated into two python modules. The book class is stored in book.py while the main library management functionality is stored in Library_manager.py
Separating the program into modules makes the code easier to organize, maintain, and reuse.

Functions 

The Library_manager.py file has 3 main functions 
1. add_book(library) which adds a new book object to the library
2. list_books(library) displays all the books in the library
3. find_books(library, query) searches for a book by title or author

Example Output

Library Menu
1. Add a new book
2. List all books
3. Find a book
4. Exit

Enter your choice: 1
Enter the book title: A Song of Ice and Fire
Enter the author: George R.R. Martin
Enter the ISBN: 9780553386790
Book added successfully!

Video Demonstration: https://www.loom.com/share/83fd94ba1a7949a5bf914a994ec35cc9 
](https://www.loom.com/share/83fd94ba1a7949a5bf914a994ec35cc9)
