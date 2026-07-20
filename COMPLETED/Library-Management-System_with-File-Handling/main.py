books = []
def readBooks():
    try:
        file=open("books.txt","r")
        for line in file:
            line = line.strip()
            book = line.split(",")
            book[4] = int(book[4])
            book[5] = int(book[5])
            books.append(book)
        file.close()
    except FileNotFoundError:
        print("")

def showbook(a):
    print("Book Id:",a[0])
    print("Book Name:",a[1])
    print("Author:",a[2])
    print("Category:",a[3])
    print("Total Copies:",a[4])
    print("Available Copies:",a[5])
    print("________________________")

def saveBooks():
    file = open("books.txt","w")
    for book in books:
        file.write(str(book[0])+","+str(book[1])+","+str(book[2])+","+str(book[3])+","+str(book[4])+","+str(book[5])+"\n")
    file.close()

def home_():
    print("\n====== LIBRARY MANAGEMENT SYSTEM ======\n\n")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Books")
    print("5. Return Books")
    print("6. Update Book")
    print("7. Delete Book")
    print("8. View Available Books:")
    print("9. View Issues Books")
    print("0. Exit\n")

def isavail(b):
    found = False
    for book in books:
        if b == book[0]:
            return True
    if not found:
        return False        

def _issueBook():
    bid = input("Enter Book ID: ")
    found = False
    for book in books:
        if book[0] == bid:
            if book[5] > 0:
                book[5] -= 1
                print("Book Issued Successfully!")
            else:
                print("No Book Lef!............")
            found = True
            break
    if not found:
        print("No Book Found!.................")


def _returnBook():
    bid = input("Enter Book ID: ")
    found = False
    for book in books:
        if book[0] == bid:
            if book[5] < book[4]:
                book[5] += 1
                print("Book Returned Successfully!............")
            else:
                print("No Book Issue!.........")
            found = True
            break
    if not found:
        print("No Book Found!...............")

def _updateBook():
    bid = input("Enter Book Id: ")
    found = False
    for book in books:
        if book[0] == bid:
            showbook(book)
            book[1] = input("Enter New Book Name: ")
            book[2] = input("Enter New Author Name: ")
            book[3] = input("Enter New Category: ")
            book[4] = int(input("Enter New Total Copy: "))
            book[5] = int(input("Enter New Available Copy: "))
            print("Book Updated Successfully!..............")
            found = True
            break
    if not found:
        print("No Book Availabe!....................")

def _searchBook():
    bid = input("Book ID: ").lower()
    found = False
    for book in books:
        if book[0] == bid:
            showbook(book)
            found = True
            break
    if not found:
        print("No Book Found!..............")

def _deleteBook():
    bid = input("Book ID: ").lower()
    found = False
    for book in books:
        if book[0] == bid:
            showbook(book)
            print("...... Deleted Successfully! ......")
            books.remove(book)
            found = True
            break
    if not found:
        print("No Book Found!..............")

def _issuedBook():
    print("------ All Issued Books ------")
    for book in books:
        if book[5]<book[4]:
            print(book[1],"Available:",book[5],"Issued:",book[4]-book[5])

def _availBook():
    print("------ All Available Books ------")
    for book in books:
        if book[5]>0:
            print(book[1],"Available:",book[5],"Issued:",book[4]-book[5])

def _addBook():
    bid = input("Enter Book ID: ").lower()
    if not isavail(bid):
        name = input("Book Name: ")
        auth = input("Book Author: ")
        cate = input("Book Category: ")
        tcpy = int(input("Total Copy: "))
        acpy = tcpy
        book =[bid,name,auth,cate,tcpy,acpy]
        books.append(book)
        print("Book Added Successfully!................")
    else:
        print("Book Already Available!......")


def _viewBooks():
    if len(books)==0:
        print("No Books Available!...............")
    else:
        print("====== All Books ======\n")
        for book in books:
            showbook(book)
            



readBooks()
while True:
    home_()
    temp = input("Choose an Option: ")

    if temp == '1':
        _addBook()
        saveBooks()
    elif temp == '2':
        _viewBooks()
    elif temp == '3':
        _searchBook()
    elif temp == '4':
        _issueBook()
        saveBooks()
    elif temp == '5':
        _returnBook()
        saveBooks()
    elif temp == '6':
        _updateBook()
        saveBooks()
    elif temp == '7':
        _deleteBook()
        saveBooks()
    elif temp == '8':
        _availBook()
    elif temp == '9':
        _issuedBook()
    elif temp == '0':
        saveBooks()
        print("Good Bye!")
        print(" _________________________________________________")
        print("|                                                 |")
        print("|------ Designed By Sardar Nirmaljeet Singh ------|")
        print("|_________________________________________________|")
        break
    else:
        print("Invalid Input.......................!")