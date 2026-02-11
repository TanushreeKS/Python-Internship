class Library:
    def __init__(self, books):
        self.books = books

    def __contains__(self, item):
        return item in self.books


lib = Library(["Python", "Java", "C++"])

print("Python" in lib)
print("Go" in lib)
