class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print("title:", self.title)
        print("author:", self.author)

class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        super().__init__(title, author)  
        self.issued_to = issued_to
        self.issued_date = issued_date

    def display_issued_book_details(self):
        super().display_book_details()   
        print("Issued To:",self.issued_to)
        print("Issued Date:",self.issued_date)

obj = IssuedBook("Java Programming","James Gosling","efg","7 jan 22")
    
obj.display_book_details()
obj.display_issued_book_details()