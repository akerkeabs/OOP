# Encapsulation is a programming approach that ties the class’s
# variables and methods together and makes it impossible for other
# classes to access them. Security is possible through Encapsulation
# Encapsulation is mostly used for Data Hiding.
class Library:
    def __init__(self, id, name):
        self.bookId = id
        self.bookName = name

    def setBookName(self, newBookName):
        self.bookName = newBookName

    def getBookName(self):
        print(f"The name of the book is {self.bookName}")

book = Library(101, 'Prepare for the Interview')
book.getBookName()
book.setBookName('Learn OOPS and practice')
book.getBookName()