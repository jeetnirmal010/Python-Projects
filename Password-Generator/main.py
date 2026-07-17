import random
import string


while True:
    print("\n====== PASSWORD GENERATOR ======")

    length = int(input("Enter password length: "))
    use_letters = input("Include letters? (y/n): ").lower()
    use_numbers = input("Include numbers? (y/n): ").lower()
    use_symbols = input("Include symbols? (y/n): ").lower()
    password = ""
    characters = ""

    if use_letters == "y":
        characters += string.ascii_letters

    if use_numbers == "y":
       characters += string.digits

    if use_symbols == "y":
      characters += string.punctuation
    if characters == "":
        print("Please select at least one character type!")
        continue
    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)

    again = input("\nGenerate another password? (y/n): ").lower()

    if again != "y":
        print("Goodbye!")
        break