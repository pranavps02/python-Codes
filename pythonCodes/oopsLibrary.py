# Tasks:
# Create A library Class
# diaplay books
# lend book
# add book
# return book


class Library:
    def __init__(self,list,name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBook(self):
        print("We Have Following Books In the Library")
        for book in self.bookList:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been Updated.You can take the Book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self,book):
        self.bookList.append(book)
        print("Book has been Added to the Book Shelf")

    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    colLib = Library(['Python','Rich Dad Poor Dad','Harry Potter','C++ Bsics','Algorithm By CLRS'],"College Library")
    print(f"--------------- Welcome To {colLib.name} ------------------- ")

    while (True):
        print(f"Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            colLib.displayBook()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            colLib.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            colLib.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            colLib.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue

