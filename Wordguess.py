
import random
import sys
import os

class GameOrdGame:
    def __init__(self):
        pass


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# ORIGINAL KOD.
#def avsluta_spel():
#    print("Spelet Avslutat")
#    sys.exit()

# *******
# LA TILL FUNKTION FÖR EXIT. ******
# EFTERSOM DET ÄR ETT SKRIFTKÄNSLIGT SPEL LA JAG TILL EN EXTRA FRÅGA JA/NEJ. *******
def exit_game():
    return True
# ******************************************
# FUNKTION FÖR ATT HÄMTA ANVÄNDARNAMN ******
def get_username():
    if os.path.exists('username.txt'):
        with open('username.txt', 'r') as f:
            return f.read()
# *******************************************
def WordGuessingGame():

    while True:
        # Skapa en dictionary med teman och deras motsvarande ordlistor.
        themes = {
            1: ["volvo", "ford", "kia", "honda", "toyota", "volkswagen", "mercedes", "audi", "bmw", "porsche"],
            2: ["hund", "katt", "lejon", "elefant", "krokodil", "häst", "orm", "björn", "varg" "älg" "noshörning"],
            3: ["äpple", "banan", "päron", "melon", "kiwi", "persika", "mandarin", "apelsin" "vindruvor"],
            4: ["paris", "london", "tokyo", "rom", "sydney", "istanbul", "dubai", "stockholm", "oslo", "köpenhamn"],
            5: ["fotboll", "basket", "tennis", "golf", "volleyboll", "baseboll", "mma", "hockey", "paddel", "klättring"]
        }

        # Skriv ut menyn.
        print("╔" + "═" * 22 + "╗")
        print("║____ Ord Gissaren ____║")
        print("║──────────────────────║")
        print("║      Välj Tema       ║")
        print("║                      ║")
        print("║1 Bilmärken           ║")
        print("║2 Djur                ║")
        print("║3 Frukter             ║")
        print("║4 Städer              ║")
        print("║5 Sporter             ║")
        print("║──────────────────────║")
        print("║e Avsluta Spel        ║")
        print("╚" + "═" * 22 + "╝")


        # Be spelaren att välja ett menyalternativ.
        selected_theme = input("Välj tema > ")


        # Kontrollera om valt tema är giltigt.
        try:
            selected_theme = int(selected_theme)
            if selected_theme not in themes:
                print("Välj ett giltigt tema (1, 2, eller 3).")
                continue

        except ValueError:
            # Om användaren trycker på "e", avsluta spelet.
            # BYTT UT: *************************************************************
            if selected_theme == "e" or 'E':
                # Original:
                #    print("Spelet Avslutat")
                #    sys.exit()
                break
            # ***********************************************************************

            print("Välj ett giltigt tema (1, 2, eller 3).")
            continue

        # Välj den aktuella listan med ord från dictionaryn.
        word_list = themes[selected_theme]

        # Välj ett ord att gissa.
        word = random.choice(word_list)

        # Skapa en lista med bokstäver som spelaren har gissat.
        guessed_letters = []

        # Sätt max antal gissningar
        max_guesses = len(word)

        # Spela spelet.
        while True:
            # Räkna antalet gissningar som spelaren har kvar
            guesses_left = max_guesses - len(guessed_letters)

            # Skriv ut antalet gissningar som en hint
            print("Du har", guesses_left, "chanser kvar.")

            # Be spelaren att gissa ett ord.
            guessed_letter = input("Gissa ett ord eller bokstav: ")

            # Kontrollera om spelaren gissade rätt.
            if guessed_letter == word:
                # Spelaren vann!
                clear_terminal()
                print("\U0001f603", "Grattis, du gissade rätt!", "\U0001f603")
                break

            # Om spelaren inte gissade rätt, lägg till den gissade bokstaven till listan med gissade bokstäver.
            guessed_letters.append(guessed_letter)

            # Visa spelaren hur många bokstäver de har gissat rätt.
            print("Hint! Du har gissat rätt på följande bokstäver:")
            for letter in word:
                if letter in guessed_letters:
                    print(letter, end=" ")
                else:
                    print("*", end=" ")
            print()

            # Om spelaren har förbrukat alla sina gissningar, avsluta spelet.
            if len(guessed_letters) == max_guesses:
                clear_terminal()
                print("\U0001f627", "Du förlorade!","\U0001f627" "\nDet rätta ordet var", word)
                break

        # Fråga användaren om de vill spela igen eller avsluta.
        print("════════════════════════════════")
        play_again = input("Vill du spela igen? (ja/nej): ")
        if play_again == "ja":
            # RENSAR TERMINALEN IFALL SPELAREN VILL SPELA OM. *************************************
            clear_terminal()
            # **************************************************************************************
            continue


        elif play_again == "nej":
            # avsluta spel ************************************************
            exit_game()
            # **************************************************************
            #avsluta_spel()
            break


if __name__ == "__main__":
    # Skapa ett objekt av GameGo-klassen och anropa metoden för att spela spelet.
    game = WordGuessingGame()
