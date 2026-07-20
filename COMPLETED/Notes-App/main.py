note = input("Enter a note: ")

with open("my_notes.txt", "w") as file:
    file.write(note)

with open("my_notes.txt", "r") as file:
    print("\nSaved Note:")
    print(file.read())