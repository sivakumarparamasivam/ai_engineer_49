import datetime

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.publication_year


if __name__ == "__main__":
    book1 = Book("Quantum Pysics", "John Rohn", 1980)
    print("Book Age:", book1.get_age(), "years")
