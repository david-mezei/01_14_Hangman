from rich import print as rprint
from gamemodes import *
def main_menu():
    print("""
          

 .d8888b.  d8b 888              .d8888b.                                             
d88P  Y88b Y8P 888             d88P  Y88b                                            
888    888     888             888    888                                            
888        888 888888 888  888 888        888  888  .d88b.  .d8888b  .d8888b  888d888
888        888 888    888  888 888  88888 888  888 d8P  Y8b 88K      88K      888P"  
888    888 888 888    888  888 888    888 888  888 88888888 "Y8888b. "Y8888b. 888    
Y88b  d88P 888 Y88b.  Y88b 888 Y88b  d88P Y88b 888 Y8b.          X88      X88 888    
 "Y8888P"  888  "Y888  "Y88888  "Y8888P88  "Y88888  "Y8888   88888P'  88888P' 888    
                           888                                                       
                      Y8b d88P                                                       
                       "Y88P"                                                        

""")
    

    print("Welcome to our game!")
    print("You can choose from 4 difficulties:")
    rprint("[#00C8FF] - 1. Easy (Only Countries) [/#00C8FF]")
    rprint("[#CF34EB] - 2. Medium (Countries; 10+ characters) [/#CF34EB]")
    rprint("[#00FF51] - 3. Hard (Countries and capitals; <10 characters) [/#00FF51]")
    rprint("[#E30E0E] - 4. Hardcore (Countries and capitals; 10+ characters) [/#E30E0E]")

    print("-----------------------------------")

    # folyamatos input ellenőrzés
    while True:
        try:
            jatekmod = int(input("Which one do you want to try? (1, 2, 3, 4) "))
            if 1 <= jatekmod <= 4:
                break
            print("Please enter a correct number! (1-4)")
        except ValueError:
            print("Please enter a number!")

    if jatekmod == 1:
        gamemode_easy()
    elif jatekmod == 2:
        gamemode_medium()
    elif jatekmod == 3:
        gamemode_hard()
    else:
        gamemode_hardcore()