**ii. Retrieve:**

Retrieve and display all attributes of the created book:

```python
all_books = Book.objects.all()
for book in all_books:
    print(book)
