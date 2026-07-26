from book import Book
def read():
    book_list=[]
    try:
        file = open("books.txt","r")
        for line in file:
            line = line.strip()
            if line =="":
                continue
            data = line.split(",")
            data[5] = float(data[5])
            data[6] = int(data[6])
            data[7] = int(data[7])
            book = Book(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
            book_list.append(book)
        file.close()
    except FileNotFoundError:
        pass
    return book_list
def save(book_list):
    file = open("books.txt","w")
    for book in book_list:
        file.write(book.bid +","+ book.title +","+ book.author+","+book.category+","+book.publisher+","+str(book.price)+","+str(book.quantity)+","+str(book.available_copy)+"\n")
    file.close()
def search(book_list,bid):
    for book in book_list:
        if book.bid == bid:
            return book
    return None
def view(book_list):
    if len(book_list) == 0:
        print("No Books Available!..........")
    else:
        for book in book_list:
            book.display()
            print("**********")
def update(book_list,bid):
    book = search(book_list,bid)
    if book:
        book.title = input("New Title: ")
        book.author = input("New Author: ")
        book.category = input("New Category: ")
        book.publisher = input("New Publisher: ")
        book.price = float(input("New Price: "))
        book.quantity = int(input("New Quantity: "))
        book.available_copy = int(input("New Available Copy: "))
        return True
    else:
        return False
def add(book_list,book):
    book_list.append(book)
def delete(book_list,bid):
    book = search(book_list,bid)
    if book:
        book.display()
        print("Book Deleted Successfully!..........")
        book_list.remove(book)
    else:
        print("Book Not Available!..........")