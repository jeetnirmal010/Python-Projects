import random

secret = random.randint(1, 10)
count = 0

print("🎮 Welcome to Guess the Number Game!")
print("I'm thinking of a number between 1 and 10.")

while True:
    guess = int(input("Guess the number: "))
    count += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("🎉 Correct! You won in", count, "attempt(s).")
        break