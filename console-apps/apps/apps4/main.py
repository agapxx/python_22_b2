class Library:
    def __init__(self, booklist):
        self.books = booklist

    def displayAvailableBooks(self):
        print(f"There are {len(self.books)} books available")
        for book in self.books:
            print(f"==> {book}\n")

    def checkOutBooks(self,name,bookName):
        pass

    def checkInBooks(self,bookName):
        pass

    def populateBookList(self,bookName):
        self.books.append(bookName)
        print(f"book \"{bookName}\" added successfully")
        return self.book


class Person():
    def issueBook(self):
        print("You wanna issue out a book")
        self.book = input("Please enter the book name")
        return self.book

    def returnBook(self):
        pass

    def addBook(self):
        print("A donated new book")
        self.books = input("Please enter book name")
        return self.books

if  __name__ == '__main__':
    wuseLibrary = Library(['General Maths','Programming Fundamentals','Ikemefuna'])
    individual = Person()

    print("<============= Wuse Digital Library ==============>")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print("\nWelcome user, What would you like to accomplish today?")
    print("\n1. View Book List \n2. Check out a book \n3. Add new book \n4. Check in a book \n5. Track book(s) \n6. Quit")

    while True:
        try:
            action = int(input("Kindly select an option\t"))
            if action == 1:
                wuseLibrary.displayAvailableBooks()
            elif action == 2:
                pass
            elif action == 3:
                wuseLibrary.populateBookList(individual.addBook())
            elif action == 4:
                pass
            elif action == 5:
                pass
            elif action == 6:
                print("Thanks for showing boys love")
                exit()

        except Exception as anomaly:
            print(anomaly)