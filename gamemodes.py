import random
from country_list import *
from ascii import *

all_countries_less_than_ten = get_countries_less_than_ten()

# szó megjelenítése, titkosítása
def get_display_word(chosen_word, right_letters):
    return " ".join(
        letter if letter in right_letters else "_"
        for letter in chosen_word)

# bemenet ellenőrzése
def get_valid_guess(used_letters):
    guess = input("Take a guess: ").upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        return None

    if guess in used_letters:
        print("You already guessed that letter.")
        return None

    return guess

# tipp feldolgozása
def handle_guess(guess, chosen_word, right_letters, wrong_letters):
    if guess in chosen_word:
        right_letters.add(guess)
        print(f"\nGood job! {guess} is in the word.")
        return False  # nem volt rossz tipp
    else:
        wrong_letters.add(guess)
        print(f"\nSorry, {guess} is not in the word.")
        return True  # rossz tipp

# játék motor
def play_game(words, max_wrong_guesses):
    import random
    from ascii import HANGMANPICS

    chosen_word = random.choice(words).upper()

    right_letters = set()
    wrong_letters = set()
    wrong_guesses = 0

    while True:
        display = get_display_word(chosen_word, right_letters)
        print("\nWord:", display)
        print("Wrong guesses:", ", ".join(sorted(wrong_letters)))
        print(HANGMANPICS[wrong_guesses])

        # win
        if "_" not in display:
            print(f"\nYou won! The word was: {chosen_word}")
            break

        # lose
        if wrong_guesses >= max_wrong_guesses:
            print(f"\nGame over! The word was: {chosen_word}")
            break

        guess = get_valid_guess(right_letters | wrong_letters) # |: két set uniója
        if guess is None:
            continue

        is_wrong = handle_guess(
            guess,
            chosen_word,
            right_letters,
            wrong_letters
        )

        if is_wrong:
            wrong_guesses += 1

def gamemode_easy():
    play_game(all_countries_less_than_ten, max_wrong_guesses=6)
def gamemode_medium():
    print("MEDIUM")

def gamemode_hard():
    print("HARD")

def gamemode_hardcore():
    print("HARDCORE")