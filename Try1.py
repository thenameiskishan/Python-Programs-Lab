class Book:
    type = "Friction"

    def __init__(self, title):
        
        self.title = title

    
print("Book Type: ", Book.type)

book1 = Book("Java")
print("Book Name: ", book1.title)

        
        