# Random Number Guessing Game
import random

num = random.randint(1, 100)   # random number between 1 and 100
guess = 0

print("I have chosen a number between 1 and 100")

while guess != num:
    guess = int(input("Guess the number: "))

    if guess > num:
        print("Too high! Try again.")
    elif guess < num:
        print("Too low! Try again.")
    else:
        print(" Correct! You guessed the number.")
