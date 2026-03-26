#We will make library_utilities a package by adding a __init__.py
#a package is a folder that contains files we want to import to use in our code

from library_utilities.book import *#import the book class
from library_utilities.library import *#import the library class
from pathlib import Path

base_dir = Path(__file__).parent
file_path = base_dir/"books.csv"

if __name__ == "__main__":
    library1 = Library("NAIT")

    book1 = Book("Lord of the rings", "JRR Tolken", 50000)
    #Add a book to the library
    library1.add_book(book1)
    #shortcut
    library1.add_book(Book("Good Stuff","Shane Bell",2))
    library1.add_book(Book("Gooder Stuff","Shane Bell",4))
    library1.list_books()

#In the library class create a get_book_by_name(self,title)
#If it exists return the book object
#If it does not exist return None

#test in the main line
search_book = input("Enter a book title to search for: ")

found_book = library1.get_book_by_name(search_book)

if found_book is None:
    print(f"Sorry{search_book} is not in the library")
else:
    print(found_book)

library1.write_books_to_csv(file_path)

new_list = library1.import_books(file_path)

#Loop through the new_list and display the books
print("Books from file(new_list):")
for book in new_list:
    print(book)

