import random
from country_list import *
from ascii import *

all_countries_less_than_ten = get_countries_less_than_ten()

def gamemode_easy():
    wrong_letters = set()
    right_letters = set()

    chosen = random.choice(all_countries_less_than_ten).upper()
    max_wrong_guesses = 6
    wrong_guesses = 0

    while True:
        # show the current state
        display = " ".join(letter if letter in right_letters else "_" for letter in chosen)
        print("\nWord: " + display)
        print("Wrong guesses: " + ", ".join(sorted(wrong_letters)))

        # win check
        if "_" not in display:
            print(f"\nCongratulations! You guessed the word: {chosen}")
            break

        # lose check
        if wrong_guesses >= max_wrong_guesses:
            print(f"\nGame over! The word was: {chosen}")
            break

        guess = input("Take a guess: ").upper()

        # input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # already guessed
        if guess in right_letters or guess in wrong_letters:
            print("You already guessed that letter.")
            continue

        # handle guess
        if guess in chosen:
            right_letters.add(guess)
            print(f"\nGood job! {guess} is in the word.")
        else:
            wrong_letters.add(guess)
            wrong_guesses += 1
            print(f"\nSorry, {guess} is not in the word.")

        print(HANGMANPICS[wrong_guesses])



def gamemode_medium():
    print("MEDIUM")

def gamemode_hard():
    print("HARD")

def gamemode_hardcore():
    print("HARDCORE")