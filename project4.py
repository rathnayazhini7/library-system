class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print("Already borrowed")
        else:
            self.is_borrowed = True
            print("Book borrowed")

    def return_book(self):
        if not self.is_borrowed:
            print("Book was not borrowed")
        else:
            self.is_borrowed = False
            print("Book returned")

    def __str__(self):
        return f"{self.title} by {self.author}"


b1 = Book("Harry Potter", "J.K. Rowling")
b2 = Book("Matilda", "Roald Dahl")
b3 = Book("The Hobbit", "Tolkien")

print("LIBRARY SYSTEM")
print(b1)
print(b2)
print(b3)

b1.borrow()
b1.borrow()
b2.return_book()
b1.return_book()

print(b1)
print(b2)
print(b3)