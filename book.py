class Book:
    """Represents a book with a title, author, and ISBN."""

    def __init__(self, title, author, isbn):
        """Initialize a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        """Return a formatted string containing the book's details."""
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    def get_details(self):
        """Return the book's details as a dictionary.

        Returns:
            dict: A dictionary containing the title, author, and ISBN.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }