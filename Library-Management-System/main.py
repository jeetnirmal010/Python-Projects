books =[]

while True:
    print("\n====== LIBRARY MANAGEMENT SYSTEM ======\n")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Show Library Summary")
    print("7. Exit")
    choose = input("\nchoose an option : ")
    if choose =='1':
        title = input("Enter Book Title: ")
        author=input("Enter the Author of Book : ")
        genre = input("Enter the Genre of Book : ")
        copy=int(input("Enter Number of Copies : "))
        price=float(input("Enter the Book Price : "))
        book={
        "title" : title,
        "author": author,
        "genre" : genre,
        "copy" : copy,
        "price": price
        }
        books.append(book)
        print("Book Added Sucessfully")
    elif choose == '2':
        if len(books) == 0:
            print("No Books Available! ")
        else:
            print("====== BOOK LIST ======\n")
            for book in books:
                print("\nTitle :",book["title"])
                print("Author:",book["author"])
                print("Genre :",book["genre"])
                print("Copies:",book["copy"])
                print("Price :",book["price"])
                print("-----------------------")
    elif choose == '3':
        title = input("Enter Book Title: ").lower()
        found = False
        for book in books:
            if title == book["title"].lower():
                print("\nTitle :",book["title"])
                print("Author:",book["author"])
                print("Genre :",book["genre"])
                print("Copies:",book["copy"])
                print("Price :",book["price"])
                print("-----------------------")
                found = True
                break
        if not found:
            print("Book Not Found!")
    elif choose == '4':
        title = input("Enter Book Title: ").lower()
        found = False
        for book in books:
            if title == book["title"].lower():
                author=input("Enter the Author of Book : ")
                genre = input("Enter the Genre of Book : ")
                copy=int(input("Enter Number of Copies : "))
                price=float(input("Enter the Book Price : "))
                book["author"] = author
                book["genre"] = genre
                book["copy"] = copy
                book["price"] = price
                found = True
                print("Book Updated Successfully!")
                break
        if not found:
            print("No Book Found!")
    elif choose =='5':
        title = input("Enter Book Title: ").lower()
        found = False
        for book in books:
            if title == book["title"].lower():
                books.remove(book)
                found = True
                print("Book Deleted Successfully!")
                break
        if not found:
            print("Book Not Found!")
    elif choose == '6':
        print("====== LIBRARY SUMMARY ======\n")
        print("Available Books:")
        diffbook=0
        tcopy = 0
        tvalue = 0
        for book in books:
            print(book["title"])
            diffbook += 1
            tcopy = tcopy + book["copy"]
            tvalue = tvalue + (book["price"] * book["copy"])
        print("Total Different Books:",diffbook)
        print("Total Copies Available:",tcopy)
        print("Total Library Value:",tvalue)
    elif choose == '7':
        print("Good Bye!")
        break
    else:
        print("Invalid Input\n")
 