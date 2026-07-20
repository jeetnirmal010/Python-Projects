contacts = []

while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)

        print("Contact Added Successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found!")
        else:
            print("\n===== CONTACT LIST =====")
            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("----------------------")
        
    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print("\n===== CONTACT FOUND =====")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                found = True
                break

        if not found:
            print("Contact not found!")
    elif choice == "4":
        update_name = input("Enter contact name to update: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == update_name.lower():
                new_phone = input("Enter new phone number: ")
                contact["phone"] = new_phone
                print("Contact Updated Successfully!")
                found = True
                break

        if not found:
            print("Contact not found!")
    elif choice == "5":
        delete_name = input("Enter contact name to delete: ")
        found = False
        for contact in contacts:
            if contact["name"].lower() == delete_name.lower():
                contacts.remove(contact)
                print("Contact Deleted Successfully!")
                found = True
                break
        if not found:
            print("Contact not found!")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")