from LibraryManagerQ4 import LibraryManager, sample_books

# Initialize the library manager
library = LibraryManager()

# Add sample books to the library
for book in sample_books:
    library.add_book(**book)

# Add a new book
print("Adding a new book:")
library.add_book("9780132350884", "Clean Code", "Robert C. Martin", "Prentice Hall", "1", 2021)
print(library.retrieve_book("9780132350884"))

# Remove a book from the library by its ISBN
print("\nRemoving a book:")
library.remove_book("9780132350884")
print(library.retrieve_book("9780132350884"))

# Retrieve and display the details of a book using its ISBN
print("\nRetrieving book details:")
print(library.retrieve_book("9780134685991"))

# Search for books by title or author
print("\nSearching for books by title 'Python':")
search_results = library.search_books("Python", by='title')
for result in search_results:
    print(result)

print("\nSearching for books by author 'Joshua Bloch':")
search_results = library.search_books("Joshua Bloch", by='author')
for result in search_results:
    print(result)

# List all books currently in the library
print("\nListing all books:")
all_books = library.list_books()
for book in all_books:
    print(book)

# Update the details of an existing book
print("\nUpdating a book's details:")
library.update_book("9780134685991", title="Effective Java, 3rd Edition")
print(library.retrieve_book("9780134685991"))

# Check if a book is available in the library by its ISBN
print("\nChecking book availability:")
print(library.check_availability("9780134685991"))
print(library.check_availability("9780132350884"))
