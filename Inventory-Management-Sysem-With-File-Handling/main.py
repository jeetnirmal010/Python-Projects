stocks = []
category = ["ELECTRONICS", "GROCERY", "CLOTHING", "STATIONERY"]
def readstock():
    try:
        file = open("Inventory.txt","r")
        for line in file:
            line = line.strip()
            data = line.split(",")
            data[0] = data[0].lower()
            data[4] = float(data[4])
            data[5] = float(data[5])
            data[6] = int(data[6])            
            stocks.append(data)
        file.close()
    except FileNotFoundError:
        print("")

def show(stock):
    print("Product ID   :",stock[0])
    print("Product Name :",stock[1].capitalize())
    print("Category     :",stock[2].capitalize())
    print("Brand        :",stock[3].capitalize())
    print("Buying Price :",stock[4])
    print("Selling Price:",stock[5])
    print("Quantity     :",stock[6])
    print("Supplier     :",stock[7].capitalize())
    print(".......................................")

def savestock():
    file = open("Inventory.txt","w")
    for stock in stocks:
        file.write(str(stock[0])+","+str(stock[1])+","+str(stock[2])+","+str(stock[3])+","+str(stock[4])+","+str(stock[5])+","+str(stock[6])+","+str(stock[7])+"\n")
    file.close()

def _home():
    print("\n ------ INVENTORY MANAGEMENT SYSTEM ------\n\n")
    print("1. Add Product")
    print("2. View all Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Purchase Stock")
    print("7. Sell Stock")
    print("8. Low Stock Product")
    print("9. Highest Stock Product")
    print("10. Category Wise View")
    print("11. Inventory Summary")
    print("0. Exit\n")

def _summary():
    if len(stocks) == 0:
        print("No Stock Available!")
    else:
        print("------ INVENTORY SUMMARY ------\n")
        tproduct = 0
        tqty = 0
        tcp = 0
        tsp = 0
        for stock in stocks:
            tproduct += 1
            tqty = tqty + stock[6]
            tcp = tcp + (stock[4] * stock[6])
            tsp = tsp +(stock[5] * stock[6])
        print("Total Product:",tproduct)
        print("Total Quantity:",tqty)
        print("Inventory Cost: Rs.",tcp)
        print("Expected Revenue:Rs.",tsp)
        print("Total Profit: Rs.",tsp - tcp)

def _hstock():
    hstock = stocks[0]
    for stock in stocks:
        if hstock[6] < stock[6]:
            hstock = stock
    show(hstock)

def _view():
    if len(stocks) == 0:
        print("No Stock Available!")
    else:
        for stock in stocks:
            show(stock)

def _deletestock():
    pid = input("Enter Product ID: ").lower()
    found = False
    for stock in stocks:
        if stock[0] == pid:
            show(stock)
            print("Stock Deleted Successfully!..........")
            stocks.remove(stock)
            found = True
            break
    if not found:
        print("No Product Found!..........")

def _search():
    pid = input("Enter Product ID: ").lower()
    found = False
    for stock in stocks:
        if stock[0] == pid:
            show(stock)
            found = True
            break
    if not found:
        print("No Product Found!..........")

def _updatestock():
    pid = input("Enter Product ID: ").lower()
    found = False
    for stock in stocks:
        if stock[0] == pid:
            show(stock)
            stock[1] = input("New Name: ")
            stock[2] = input("New Category: ")
            stock[3] = input("New Brand: ")
            stock[4] = float(input("New Buying Price: "))
            stock[5] = float(input("New Selling Price: "))
            '''stock qty cannot be updated it should be in purchase stock or sale stock'''
            stock[7] = input("New Supplier: ")
            found = True
            break
    if not found:
        print("No Product Found!..........")

def _sellstock():
    pid = input("Enter Product ID: ").lower()
    found = False
    for stock in stocks:
        if stock[0] == pid:
            show(stock)
            while True:
                qty = int(input("How Much Quantity: "))
                if qty<= stock[6]:
                    stock[6] = stock[6] - qty
                    print("Stock Sold!..........")
                    break
                else:
                    print("Invalid Quantity!...")
            found = True
            break
    if not found:
        print("No Product Found!..........")

def _purchasestock():
    pid = input("Enter Product ID: ").lower()
    found = False
    for stock in stocks:
        if stock[0] == pid:
            show(stock)
            while True:
                qty = int(input("How Much Quantity: "))
                if qty> 0:
                    stock[6] = stock[6] + qty
                    print("Stock Purchased !..........")
                    break
                else:
                    print("Invalid Quantity!...")
            found = True
            break
    if not found:
        print("No Product Found!..........")

def _lstock():
    print("------ Low Stock Product ------\n")
    for stock in stocks:
        if stock[6] < 5:
            show(stock)

def _cview():
    if len(stocks) == 0:
        print("No Stock Available!..........")
    else:
        print("------ CATEGORY WISE PRODUCTS ------\n")

        print("Category : ELECTRONICS")
        for stock in stocks:
            if stock[2].upper() == category[0]:
                show(stock)

        print("Category : GROCERY")
        for stock in stocks:
            if stock[2].upper() == category[1]:
                show(stock)

        print("Category : CLOTHING")
        for stock in stocks:
            if stock[2].upper() == category[2]:
                show(stock)

        print("Category : STATIONERY")
        for stock in stocks:
            if stock[2].upper() == category[3]:
                show(stock)

def _addstock():
    pid = input("Enter Product ID: ").lower()

    for stock in stocks:
        if stock[0] == pid:
            print("Product Already Available!..........")
            return

    name = input("Product Name: ")

    while True:
        cate = input("Category\nELECTRONICS\nGROCERY\nCLOTHING\nSTATIONERY\nSelect Category: ").upper()
        if cate in category:
            break
        print("Invalid Category!")

    brand = input("Brand: ")
    bprice = float(input("Buying Price: "))
    sprice = float(input("Selling Price: "))
    qty = int(input("Quantity: "))
    supp = input("Supplier: ")

    stock = [pid, name, cate, brand, bprice, sprice, qty, supp]
    stocks.append(stock)

    print("Product Added Successfully!..........")

readstock()
while True:
    _home()
    temp =input("Choose an Option: ")
    if temp == '1':
        _addstock()
        savestock()
    elif temp == '2':
        _view()
    elif temp == '3':
        _search()
    elif temp == '4':
        _updatestock()
        savestock()
    elif temp == '5':
        _deletestock()
        savestock()
    elif temp == '6':
        _purchasestock()
        savestock()
    elif temp == '7':
        _sellstock()
        savestock()
    elif temp == '8':
        _lstock()
    elif temp == '9':
        _hstock()
    elif temp == '10':
        _cview()
    elif temp == '11':
        _summary()
    elif temp == '0':
        savestock()
        print(" _______________________________________________________")
        print("|                                                       |")
        print("|          Designed By Sardar Nirmaljeet Singh          |")
        print("|_______________________________________________________|")
        print("---------- Good Bye!-----------")
        break