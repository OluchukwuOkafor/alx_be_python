class Book:
    """A class representing a book using Python magic methods."""

    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Readable string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation that can recreate the instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Print when the Book object is deleted."""
        print(f"Deleting {self.title}")
