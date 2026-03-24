from book import *#import the book class
from library import *#import the library class

if __name__ == "__main__":
    library1 = Library("NAIT")

    book1 = Book("Lord of the rings", "JRR Tolken", 50000)
    #Add a book to the library
    library1.add_book(book1)
    library1.list_books()

#In the library class create a get_book_by_name(self,title)
#If it exists return the book object
#If it does not exist return None

#test in the main line

