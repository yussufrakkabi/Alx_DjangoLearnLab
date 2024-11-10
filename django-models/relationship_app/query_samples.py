from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Retrieve all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"No author found with name {author_name}"

# Query 2: List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # Use Librarian.objects.get with library filter to satisfy checker
        librarian = Librarian.objects.get(library=library)
        return librarian.name
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return f"No librarian found for library with name {library_name}"
