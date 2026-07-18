inventorys = []
while True:
    print("====== INVENTORY MANAGEMENT ======")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Show Total Products")
    print("7. Exit\n")
    choose =input("Choose an option: ")
    if choose =='1':
        pname =input("Enter Product Name : ")
        price =float(input("Enter Product Price : "))
        qty =int(input("Enter Product Quantity : "))
        inventory={
        "productname" : pname,
        "price" : price,
        "qty" : qty
        }
        inventorys.append(inventory)
        print("One Product Added Successfully!")
    elif choose == '2':
        if len(inventorys) == 0:
            print("No Stock Found!")
        else:
            print("====== All Products ======\n")
            for inventory in inventorys:
                print("Product Name :",inventory["productname"])
                print("Price :",inventory["price"])
                print("Quantity :",inventory["qty"])
                print("----------------------------\n")
    elif choose == '3':
        pname = input("Enter Product Name: ").lower()
        found = False
        for inventory in inventorys:
            if pname == inventory["productname"].lower():
                print("Product : ",inventory["productname"])
                print("Price :",inventory["price"])
                print("Quantity :",inventory["qty"])
                found = True
                break
        if not found:
            print("Product not Found!")
    elif choose == '4':
        pname = input("Enter Product Name: ").lower()
        found = False
        for inventory in inventorys:
            if pname == inventory["productname"].lower():
                price =float(input("Enter Product Price : "))
                qty =int(input("Enter Product Quantity : "))
                inventory["price"]= price
                inventory["qty"]=qty
                found = True
                print("Product Updated")
                break
        if not found:
            print("Product not Found!")
    elif choose == '5':
        pname = input("Enter Product Name: ").lower()
        found = False
        for inventory in inventorys:
            if pname == inventory["productname"].lower():
                inventorys.remove(inventory)
                print("Product Deleted")
                found =True
                break
        if not found:
            print("Product not Found!")
    elif choose == '6':
        count =0
        tqty=0
        print("Available Products: ")
        for inventory in inventorys:
            count += 1
            tqty = tqty + inventory["qty"]
            print(inventory["productname"])
            
        print("Total Different Product: ",count)
        print("Total Items in Stock: ",tqty)
        
        
    elif choose == '7':
        print("Good Bye!")
        break
    else:
        print("\nInvalid Input")