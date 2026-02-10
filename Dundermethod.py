class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def __str__(self):
        return f"{self.title} by {self.author} - ₹{self.price}"
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"
b1 = Book("Python Basics", "Guido", 500)
b2 = Book("OOP Concepts", "James", 650)
print(b1)
print([b1, b2])

