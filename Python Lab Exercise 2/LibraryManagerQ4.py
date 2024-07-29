class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year):
        if isbn not in self.books:
            self.books[isbn] = {
                'title': title,
                'author': author,
                'publisher': publisher,
                'volume': volume,
                'year': year
            }

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]

    def retrieve_book(self, isbn):
        return self.books.get(isbn, "Book not found.")

    def search_books(self, query, by='title'):
        return [book for book in self.books.values() if query.lower() in book[by].lower()]

    def list_books(self):
        return list(self.books.values())

    def update_book(self, isbn, **kwargs):
        if isbn in self.books:
            self.books[isbn].update(kwargs)

    def check_availability(self, isbn):
        return isbn in self.books

# Sample data
sample_books = [
    {"isbn": "9780134685991", "title": "Effective Java", "author": "Joshua Bloch", "publisher": "Addison-Wesley", "volume": "3", "year": 2020},
    {"isbn": "9781449355739", "title": "Python for Data Analysis", "author": "Wes McKinney", "publisher": "O'Reilly Media", "volume": "2", "year": 2022},
    {"isbn": "9780131103627", "title": "The C Programming Language", "author": "Brian W. Kernighan", "publisher": "Prentice Hall", "volume": "2", "year": 2022}
]
