#! /usr/bin/env python
# Guess a number
import random, sys

def guess_game():
    import random
    print("Hello what is your name?")
    player_name = input()
    right_number = random.randint(1, 20)
    print("Well, " + player_name + ", just take a guess between 1 and 20 number. You have 6 guesses")

    # Ask player to guess 6 time
    for guessesTaken in range(1, 7):
        print("Take a guess")
        guess = int(input())
        if guess < right_number:
            print("Your guess is too low")
        elif guess > right_number:
             print("Your guess is too high")
        else:
            break # If guess correct

    if guess == right_number:
        print("Good job, " + player_name + "!, you guessed number in " + str(guessesTaken) + " guesses")
    else:
        print("You lost the game, you didn't guess a number")
        print("Want play one more time? 'yes' or 'no' ")
        answer = input()
        if answer == "yes":
            return guess_game()
        else:
            sys.exit()

if __name__ == "__main__":
# Run as a script
    guess_game() 
