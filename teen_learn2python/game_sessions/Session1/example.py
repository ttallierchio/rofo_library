#!/usr/bin/python3
import random


if __name__ == "__main__":
    random_number = random.randint(1, 10)
    start = 1
    end = 10
    guess = input(f"What number am i thinking of between {start} and {end}? ")

    try:
        guess = int(guess)
    except:
        print("please enter a valid whole number")

    if random_number == guess:
        print("You have chosen correctly!")
    else:
        print("You have chosen incorrectly!")
