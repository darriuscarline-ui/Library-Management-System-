from book import Book


def add_book(library):
    """Prompt the user for book information and add a new Book object.

    Args:
        library (list): The list containing the library's Book objects.

    Returns:
        None
    """
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    isbn = input("Enter the ISBN: ")

    new_book = Book(title, author, isbn)
    library.append(new_book)

    print("Book added successfully!")


def list_books(library):
    """Display all books currently stored in the library.

    Args:
        library (list): The list containing the library's Book objects.

    Returns:
        None
    """
    if not library:
        print("The library is empty.")
    else:
        print("\nBooks in the library:")
        for book in library:
            print(book)


def find_book(library, query):
    """Search for a book by title or author.

    Args:
        library (list): The list containing the library's Book objects.
        query (str): The title or author to search for.

    Returns:
        Book or None: The matching Book object, or None if no match is found.
    """
    for book in library:
        if query.lower() in book.title.lower() or query.lower() in book.author.lower():
            return book

    return None


# Main program
my_library = []

while True:
    print("\nLibrary Menu")
    print("1. Add a new book")
    print("2. List all books")
    print("3. Find a book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book(my_library)

    elif choice == "2":
        list_books(my_library)

    elif choice == "3":
        query = input("Enter the title or author to search for: ")
        found_book = find_book(my_library, query)

        if found_book:
            print("Book found:")
            print(found_book)
        else:
            print("Book not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")