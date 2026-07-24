from book import Book
from member import Member
from issue import Issue
import member_database
import book_database
import issue_database
book_list = book_database.read()
member_list = member_database.read()
issue_list = issue_database.read()
def mainmenu():
    print("\n====== Library Management System ======\n\n")
    print("1. Book Management")
    print("2. Member Management")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Reports")
    print("6. Save")
    print("7. Exit\n")
def bookmenu():
    while True:
        print("\n====== Book Management ======\n\n")
        print("1. Add Book")
        print("2. View Book")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Back\n")
        btemp = input("Choose an Option: ")
        if btemp =='1':
            while True:
                bid = input("Book ID: ")
                if book_database.search(book_list,bid):
                    print("Book ID Already Available!......")
                else:
                    break
            title = input("Title: ")
            author = input("Author: ")
            category = input("Category: ")
            publisher = input("Publisher: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            available_copy = quantity
            book = Book(bid,title,author,category,publisher,price,quantity,available_copy)
            book_database.add(book_list,book)
            print("Book Added Successfully!.....")
            book_database.save(book_list)
        elif btemp == '2':
            book_database.view(book_list)
        elif btemp == '3':
            bid = input("Book ID: ")
            book = book_database.search(book_list,bid)
            if book:
                book.display()
            else:
                print("No Such Book Found!..........")
        elif btemp == '4':
            bid = input("Book ID: ")
            if book_database.update(book_list,bid):
                print("Book Updated Successfully!......")
                book_database.save(book_list)
            else:
                print("No Book Found to Update")
        elif btemp == '5':
            bid  = input("Book ID: ")
            book_database.delete(book_list,bid)
            book_database.save(book_list)
        elif btemp =='6':
            book_database.save(book_list)
            break
        else:
            print("Invalid Input\n")

def membermenu():
    while True:
        print("\n====== Member Management ======\n\n")
        print("1. Add Member")
        print("2. View Members")
        print("3. Search Member")
        print("4. Update Member")
        print("5. Delete Member")
        print("6. Back\n")
        mtemp = input("Choose an Option:")
        if mtemp == '1':
            while True:
                mid = input("Member ID: ")
                if member_database.search(member_list,mid):
                    print("Member ID Already Available!...")
                else:
                    break
            name = input("Name: ")
            age = input("Age: ")
            gender = input("Gender: ")
            phone = input("Phone: ")
            email = input("Email ID: ")
            member = Member(mid,name,age,gender,phone,email)
            member_database.add(member_list,member)
            member_database.save(member_list)
            print("Member Added Successfully!......")
        elif mtemp =='2':
            member_database.view(member_list)
        elif mtemp == '3':
            mid = input("Member ID: ")
            member = member_database.search(member_list,mid)
            if member:
                member.display()
            else:
                print("No Member found!......")
        elif mtemp == '4':
            mid = input("Member ID: ")
            if member_database.update(member_list,mid):
                print("Updated Successfully!...")
                member_database.save(member_list)
            else:
                print("No Member Found!...")
        elif mtemp == '5':
            mid = input("Member ID: ")
            member_database.delete(member_list,mid)
            member_database.save(member_list)
        elif mtemp == '6':
            member_database.save(member_list)
            break
        else:
            print("Invalid Input!..........")
def _isavail(book_list):
    for book in book_list:
        if book.available_copy > 0:
            book.display()
def _isissue(issue_list):
    for issue in issue_list:
        if issue.status.lower() == "Issued".lower():
            issue.display()
def reportmenu():
    while True:
        print("\n====== Reports ======\n\n")
        print("1. Available Books")
        print("2. Issued Books")
        print("3. Members")
        print("4. Back\n")
        rtemp = input("Choose an Option: ")
        if rtemp =='1':
            _isavail(book_list)
        elif rtemp == '2':
            _isissue(issue_list)
        elif rtemp == '3':
            member_database.view(member_list)
        elif rtemp =='4':
            break
        else:
            print("Invalid Input!......")
def _save(book_list,member_list,issue_list):
    book_database.save(book_list)
    member_database.save(member_list)
    issue_database.save(issue_list)

while True:
    mainmenu()
    temp = input("Choose an Option: ")
    if temp == '1':
        bookmenu()
    elif temp == '2':
        membermenu()
        _save(book_list,member_list,issue_list)
    elif temp == '3':
        while True:
            bid = input("Book ID: ")
            book = book_database.search(book_list,bid)
            if book:
                while True:
                    mid = input("Member ID: ")
                    member = member_database.search(member_list,mid)
                    if member:
                        while True:
                            iid = input("Issue ID: ")
                            if issue_database.search(issue_list,iid):
                                print("Issue ID Available: ")
                            else:
                                break
                        issdate = input("Issue Date: ")
                        retdate = input("Return Date: ")
                        if book.book_issue():
                            issue= Issue(iid,member.mid,book.bid,issdate,retdate,"ISSUED")
                            issue_database.add(issue_list,issue)
                            _save(book_list,member_list,issue_list)
                        break
                    else:
                        print("Invalid Member!...")
                break
            else:
                print("Invalid Book Selected!......")
    elif temp == '4':
        iid = input("Issue ID: ")
        issue = issue_database.search(issue_list,iid)
        print(issue)
        
        if issue:
            bid = issue.bid
            book = book_database.search(book_list,bid)
            if book.available_copy < book.quantity:
                book.book_return()
                mid = issue.mid
                member = member_database.search(member_list,mid)
                retdate = input("Return Date: ")
                issue.status = "Returned"
                iid = "R"+issue.iid
                new_issue = Issue(iid,member.mid,book.bid,issue.issdate,retdate,"Returned")
                issue_database.add(issue_list,new_issue)
                _save(book_list,member_list,issue_list)

            else:
                print("Book Alredy Returned!......")
        else:
            print("Invalid Issue ID!...........")
    elif temp == '5':
        reportmenu()
    elif temp =='6':
        _save(book_list,member_list,issue_list)
    elif temp == '7':
        _save(book_list,member_list,issue_list)
        print("Good Bye!..........")
        break