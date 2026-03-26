from csv import DictReader,DictWriter
#When importing from within a package we must use .(this package)
#the path will be relative to this package
from .book import *

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []#list of book objects
        
#Add book Method
    def add_book(self, book):
        self.books.append(book)

    #List books Method
    def list_books(self):
        print("Current books in our library:")
        if len(self.books) == 0:#empty list
            print("No books in the library")
        else:
            for book in self.books:#each book object in the books
                print(f"- {book}")

    def get_book_by_name(self, title):
        return_value = None
        for book in self.books:
            if book.title.lower() == title.lower():
                return_value = book
        return return_value
    
    def write_books_to_csv(self, file_path):
        with open(file_path,"w",newline="") as f:
            writer = DictWriter(f,fieldnames = ["title","author","pages"])
            writer.writeheader()
            #write each object in the list to the file in csv format
            #for each book(object) in this objects(library1) books list
            for book in self.books:
                #Create a dictionary from each book object
                writer.writerow({"title":book.title,"author":book.author,"pages": book.pages})
    #Read the file into a list of objects
    def import_books(self,file_path):
        with open(file_path,"r",newline="")as f:
            reader = DictReader(f)
            for row in reader:
                self.books.append(Book(row["title"],row["author"],row["pages"]))
        return self.books



    

    
            

