from Wordguess import WordGuessingGame, clear_terminal
from Sten import RockPaperScissor
import GoFish
import Hang
import os


username = None
def get_username():
    global username
    if username is None:
        username = input("Skriv in ditt namn: ")
        with open('username.txt', 'w') as f:
            f.write(username)
        return username
    # LÄSER IN NAMNET IGEN OM MAN VÄLJER ATT AVSLUTA SPEL OCH KOMMA TILLBAKA TILL MENYN
    else:
        if os.path.exists('username.txt'):
            with open('username.txt', 'r') as f:
                return f.read()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    username = get_username()
    clear_terminal()
    menu_width = 60

    print("*" * menu_width)
    print("*{:^58}*".format(f"Välkommen {username} till Spelsamlingen"))
    print("*" * menu_width)
    print("*{:^58}*".format("Välj något av spelen 1 - 4, eller '5' för att avsluta"))
    print("*" * menu_width)
    print("*{:^58}*".format("Tillgängliga spel:"))
    print("*{:^58}*".format("1. Ordgissaren"))
    print("*{:^58}*".format("2. Sten, Sax, Påse"))
    print("*{:^58}*".format("3. Finns i Sjön"))
    print("*{:^58}*".format("4. Hängagubbe"))
    print("*{:^58}*".format("5. Avsluta"))
    print("*" * menu_width)


# test av inmatning av namn:
def main():
    while True:
        #clear_terminal()
        print_menu()
        game_choice = input("Val: ")

        # Avsluta = 'e'.
        if game_choice == "1":
            clear_terminal()
            WordGuessingGame()
        # Avsluta = "Vill du fortsätta spela? - Nej"
        elif game_choice == "2":
            clear_terminal()
            game = RockPaperScissor()
            game.play()
        # Avsluta - 'exit'
        elif game_choice == "3":
            clear_terminal()
            GoFish.main_game()
        # Avsluta - 'exit' -> 'yes'
        elif game_choice == "4":
            clear_terminal()
            Hang.main()
        elif game_choice == "5":
            print("")
            print("Tack för du ville spela. <3")
            break


if __name__ == "__main__":
    main()