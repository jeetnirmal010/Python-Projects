class Book:
    def __init__(self,bid,title,author,category,publisher,price,quantity,available_copy):
        self.bid = bid
        self.title = title
        self.author = author
        self.category = category
        self.publisher = publisher
        self.price = price
        self.quantity = quantity
        self.available_copy = available_copy
    def display(self):
        print("Book ID       :",self.bid)
        print("Title         :",self.title)
        print("Author        :",self.author)
        print("Category      :",self.category)
        print("Publisher     :",self.publisher)
        print("Quantity      :",self.quantity)
        print("Price         :",self.price)
        print("Available Copy:",self.available_copy)
    def book_issue(self):
        if self.available_copy > 0:
            self.available_copy = self.available_copy - 1
            print("Book Issued Successfuly!")
            return True
        else:
            print("This Book is Currently Not Available!......")
            return  False
    def book_return(self):
        if self.available_copy < self.quantity:
            self.available_copy = self.available_copy + 1
        else:
            print("Book is Not issue to Any One!..........")