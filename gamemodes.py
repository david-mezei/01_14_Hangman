import random
from country_list import *
from ascii import *

all_countries_less_than_ten = get_countries_less_than_ten()

def gamemode_easy():
    wrong_letters = set()
    right_letters = set()

    # For testing, fixed word
    # chosen = random.choice(all_countries_less_than_ten)
    chosen = "TESZT"
    
    max_wrong_guesses = 6  # limit for wrong guesses
    wrong_guesses = 0

    while True:
        # Show current state of the word
        display = " ".join(letter if letter in right_letters else "_" for letter in chosen)
        print(f"\nWord: {display}")
        print(f"Wrong guesses: {', '.join(sorted(wrong_letters))}")

        # Check if user has guessed the word
        if "_" not in display:
            print(f"Congratulations! You guessed the word: {chosen}")
            break

        # Check if user has too many wrong guesses
        if len(wrong_letters) >= max_wrong_guesses:
            print(f"Game over! The word was: {chosen}")
            break

        # Get user input
        guess = input("Take a guess: ").upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if already guessed
        if guess in right_letters or guess in wrong_letters:
            print("You already guessed that letter.")
            continue

        # Add guess to right or wrong letters
        if guess in chosen:
            right_letters.add(guess)
            print(f"Good job! {guess} is in the word.")
        else:
            wrong_letters.add(guess)
            print(f"Sorry, {guess} is not in the word.")

        # Show the updated word immediately
        display = " ".join(letter if letter in right_letters else "_" for letter in chosen)
        print(f"Current word: {display}")

        # Inside your game loop:
        if guess not in display:
            wrong_guesses += 1
            print("Rossz tipp!")

        # To display the current state:
        print(HANGMANPICS[wrong_guesses])


def gamemode_medium():
    print("MEDIUM")

def gamemode_hard():
    print("HARD")

def gamemode_hardcore():
    print("HARDCORE")