# Lab 5 Part I -- Jose Ricardo Cuadra
class Book:
    # init constructor method to initialize attributes
    def __init__(self, title, author, pages, read = False):
        self._title = title
        self._author = author
        self._pages = pages
        self._read = read

    # returning book instance's description
    def description(self):
        return f"Title: {self._title}, Author: {self._author}, Pages: {self._pages}"
    
    # setting read to True and displaying confirmation message
    def mark_as_read(self):
        self._read = True
        print(f"{self._title} has been marked as read.")
        return self._read
    
def main():
    # creating two Book objects
    book1 = Book("Snow Crash", "Neil Stephenson", "559")
    book2 = Book("The Idiot", "Fyodor Dostoevsky", "559")

    # printing each book's description
    print(book1.description())
    print(book2.description())

    # showing the change in read attribute
    print(book1._read)
    book1.mark_as_read()
    print(book1._read)

if __name__ == "__main__":
    main()