from country_list import *
from contry_and_capital_list import *
from rich import print as rprint
import sys
from playsound3 import playsound

all_countries_less_than_ten = get_countries_less_than_ten()
all_countries_more_than_ten = get_countries_more_than_ten()
all_countries_cities_less_than_ten = get_cc_less_than_ten()
all_countries_cities_more_than_ten = get_cc_more_than_ten()

# szó megjelenítése, titkosítása
def get_display_word(chosen_word, right_letters):
    return " ".join(
        letter if letter in right_letters or letter in {" ", "|"} else "_" # kihagyja a titkosításból a szóköz és | karaktert
        for letter in chosen_word)

# bemenet ellenőrzése
def get_valid_guess(used_letters):
    guess = input("Take a guess: ").strip().upper()

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
        rprint(f"\n[green]Good job! {guess} is in the word.[/green]")
        return False  # nem volt rossz tipp
    else:
        wrong_letters.add(guess)
        rprint(f"\n[red]Sorry, {guess} is not in the word.[/red]")
        return True  # rossz tipp

# játék újraindítása
def handle_restart():
    from main_menu import main_menu
    restart = input("Do you want to go back to main menu? (yes/no) ")
    if restart in ["y", "yes"]:
        main_menu()
    else:
        print("Thanks for playing!")
        sys.exit()

# játék motor
def play_game(words, max_wrong_guesses):
    import random
    from ascii import HANGMANPICS

    chosen_word = random.choice(words).upper()

    right_letters = set()
    wrong_letters = set()
    wrong_guesses = 0


    while True:
        lives_left = max_wrong_guesses - wrong_guesses
        print(f"\nLives left: {lives_left}/{max_wrong_guesses}")

        display = get_display_word(chosen_word, right_letters)
        print("\nWord:", display)
        print("Wrong guesses:", ", ".join(sorted(wrong_letters)))
        print(HANGMANPICS[wrong_guesses])

        # win
        if "_" not in display:
            print(f"\nYou won! The word was: {chosen_word} 🎉")
            playsound("sounds/win.mp3")
            handle_restart()
            break

        # lose
        if wrong_guesses >= max_wrong_guesses:
            print(f"\nGame over! The word was: {chosen_word} 🙄")
            playsound("sounds/lose.mp3")
            handle_restart()
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
    play_game(all_countries_more_than_ten, max_wrong_guesses=6)

def gamemode_hard():
    play_game(all_countries_cities_less_than_ten, max_wrong_guesses=6)

def gamemode_hardcore():
    play_game(all_countries_cities_more_than_ten, max_wrong_guesses=6)
