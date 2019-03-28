#!/usr/bin/env python3

import random

def display_title():
    print("Guess the number!")
    print()

def play_game(): # rem pos arg limit
    limit = int(input("Enter the upper limit for the range of numbers: ")) # added limit inside
    number = random.randint(1, limit)
    print("I'm thinking of a number from 1 to " + str(limit) + "\n")
    while True:
        count = 0 # define 'count'
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number: # changed '>=' -> '>'
            print("Too high.")
            count += 1
        elif guess == number:
            print("You guessed it in " + str(count) + " tries.\n")
            return

def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        play_game()
        again = input("Play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

