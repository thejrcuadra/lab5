# Lab 5 -- Jose Ricardo Cuadra
# Part I

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
    def markAsRead(self):
        self._read = True
        print(f"{self._title} has been marked as read!")
        return self._read
    
def main():
    # creating two Book objects
    book1 = Book("Snow Crash", "Neil Stephenson", "559")
    book2 = Book("The Idiot", "Fyodor Dostoevsky", "559") # coincidently, both books have same number of pages

    # printing each book's description
    print(book1.description())
    print(book2.description())

    # showing the change in read attribute
    print(book1._read) # False = book not read
    book1.markAsRead()
    print(book1._read) # True = book has been changed to read

# Part II

class eBookReader:
    # init contructor method to initialize lists (data)
    def __init__(self):
        self._availableBooks = []
        self._purchasedBooks = []

    # add a book to available books (already populated data)
    def addBook(self, book):
        if book not in self._availableBooks:
            self._availableBooks.append(book)
            print(f"{book._title} has been added to system.")
        else:
            print(f"{book._title} is already in the system.")

    # buying a book if not purchased, available, and exists
    def buyBook(self, bookName):
        for book in self._purchasedBooks:
            if book._title == bookName:
                print(f"{book._title} has already been purchased.")
                return
        for book in self._availableBooks:
            if book._title == bookName:
                self._purchasedBooks.append(book)
                self._availableBooks.remove(book)
                print(f"{book._title} has been successfully purchased!")
                return
        print(f"{bookName} is not available.")

    # displaying the description of books inside purchased books list
    def viewPurchasedBooks(self):
        if not self._purchasedBooks:
            print(f"There are no purchased books ... yet!")
        else:
            print(f"These are the purchased books: ")
            for book in self._purchasedBooks:
                print('\t'+book.description())

    # marking a book as read if there book is already purchased and not yet read
    def readPurchasedBook(self, bookName):
        if not self._purchasedBooks:
            print(f"There are no purchased books ... yet!")
        else:
            for book in self._purchasedBooks:
                if book._title == bookName:
                    if book._read == False:
                        book.markAsRead()
                    else:
                        print(f"{book._title} has already been read.")
                    return
            print(f"{bookName} is not purchased.")


def main2():
    print() # differentiate betweeen two mains

    # singular instance of eBookReader class
    userOne = eBookReader()

    # adding Book instances (books) to userOne's simulation
    userOne.addBook(Book("Mansfield Park", "Jane Austen", "488"))
    userOne.addBook(Book("The Jungle Book", "Rudyard Kipling", "277"))
    userOne.addBook(Book("Little Women", "Louisa May Alcott", "449"))
    userOne.addBook(Book("The Phantom of the Opera", "Gaston Leroux", "360"))

    # simulating user actions
    userOne.buyBook("The Jungle Book")
    userOne.buyBook("Little Women")
    userOne.viewPurchasedBooks()
    userOne.readPurchasedBook("The Jungle Book")
    userOne.buyBook("Meditations")

if __name__ == "__main__":
    main()
    main2()