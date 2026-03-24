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

#