# Random modul för blandning av kortleken samt datorns gissningar.
import random
# os modul för att hantera terminalrensningen för flera operativsystem.
import os


# Klass som används för att representera kortleken
# Även metoder för att bland annat skapa, blanda, dra, blanda och dela ut kort samt återställa kortleken.
class Deck:
    def __init__(self):
        # En tom lista för att lagra korten i kortleken.
        self.cards = []
        # Lista med alla möjliga värden på korten.
        values = ['ace', "2", "3", "4", "5", "6", "7", "8", "9", "10", "jacks", "queen", "king"]
        # Skapar fyra exemplar av varje kort.
        for _ in range(4):
            for value in values:
                card = value
                self.cards.append(card)

    # funktion för att blanda.
    def card_shuffle(self):
        random.shuffle(self.cards)

    # Funktion för att dra kort från kortleken samt skriva ut när kortleken är tom.
    def draw(self):
        if not self.cards:
            print("The deck is now empty.")
            print("")
            return None
        return self.cards.pop()

    # Funktion för att dela ut kort spelaren och datorns kort till en tom lista.
    def deal_cards(self):
        player = []
        computer = []
        for _ in range(5):
            card = self.draw()
            player.append(card)
        for _ in range(5):
            card = self.draw()
            computer.append(card)
        return player, computer

    # funktion för att kolla hur många kort som finns kvar i kortleken.
    def remaining_cards(self):
        return len(self.cards)

    # Funktion för att återställa kortleken.
    def reset(self):
        self.__init__()


# Funktion för UI.
def draw_border(text):
    border = '*' * 100
    return f"{border}\n{text.center(100)}\n{border}"


# Funktion för att skriva ut välkomstmeddelande och regler.
def print_welcome_message(player_name):
    welcome_message = f"♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ Welcome {player_name} to the game of Go Fish! ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥"
    rules = (
        "- You can only guess cards that you have in your hand.",
        "- If you guess a card that's not on your hand, you get to skip a round.",
        "- When you collect four of the same card, you earn a point.",
        "- The first player to reach 3 points wins.",
        "- You can always exit by typing 'exit'."
    )
    return draw_border(welcome_message) + "\n" + "\n".join(rules)


# Funktion som tar en lista med spelarens kort som argument och kontrollerar om det finns fyra kort av samma i handen.
def check_four_cards(player_cards):
    card_counts = {}
    for card in player_cards:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1

    for card, count in card_counts.items():
        if count == 4:
            player_cards = [c for c in player_cards if c != card]
            return True, player_cards
    return False, player_cards


# Funktion som rensar terminalen.
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Funktion för att hämta det valda användarnamnet som spelar fyller i innan huvudmenyn.
def get_username():
    if os.path.exists('username.txt'):
        with open('username.txt', 'r') as f:
            return f.read()


# Huvudspel
def main_game():
    # player = namnet som skrivs in i huvudprogrammet
    player = get_username()
    # Datorns namn :)
    nemesis = "Computer"
    player_cards = []
    player_score = 0
    computer_cards = []
    computer_score = 0
    computer_guesses = (['ace', "2", "3", "4", "5", "6", "7", "8", "9", "10", "jacks", "queen", "king"] * 4)
    # Anropar klassen till spelet och sätter igång motoriken.
    deck = Deck()
    # Blandar kortleken
    deck.card_shuffle()
    # Symboler för UI
    symbol_list = [' ♥ ', ' ♦ ', ' ♣ ', ' ♠ ']
    symbols = ' '.join(symbol_list * 6)
    symbol_string = random.choice(symbols)
    # Delar ut kort till spelare och datorn.
    player_cards, computer_cards = deck.deal_cards()

    # Skriv ut välkomstmeddelande och regler en gång i början av spelet.
    clear_terminal()
    print(print_welcome_message(player))
    # Score-board.
    print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
    # Spelarens kort.
    print("Player cards: ")
    # UI som separerar spelarens kort från övriga spelet.
    print(*player_cards, sep=', ')
    print(symbols + symbol_list[0])
    print("")

    while True:
        # Spelarens gör här sitt val, därefter rensas terminalen för att skriva ut svaren.
        player_choice = input("Which card would you like to steal from your opponent? >:) ")
        clear_terminal()

        # Tar tillbaka användaren till huvudmenyn som den skriver in exit istället för val av kort.
        if player_choice.lower() == 'exit':
            break

        # Lager-variabler för att räkna spelarens och datorns kort.
        player_card_count = player_cards.count(player_choice)
        computer_card_count = computer_cards.count(computer_guesses)

        # Om spelarens kort finns i datorns hand så tas korten bort från dator och läggs till spelaren.
        if player_choice in player_cards:
            if player_choice in computer_cards:
                while player_choice in computer_cards:
                    computer_cards.remove(player_choice)
                    player_cards.append(player_choice)
                print(print_welcome_message(player))
                print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
                print("Player cards: ")
                print(*player_cards, sep=', ')
                print(symbols + symbol_list[0])
                # Ett meddelande skrivs ut som bekräftar att spelaren lyckas ta ett kort från datorn.
                print("")
                print(f"It's super effective! You stole {player_choice} from Computer!")
                print("")

                # Räknar spelarens kort. Om det finns 4 av samma så tas korten bort och poäng ges.
                player_card_count = player_cards.count(player_choice)
                if player_card_count == 4:
                    player_cards = [card for card in player_cards if card != player_choice]
                    player_score += 1
                    print("")
                    clear_terminal()
                    print(print_welcome_message(player))
                    print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
                    print("Player cards: ")
                    print(*player_cards, sep=', ')
                    print(symbols + symbol_list[0])
                    # Även då skrivs ett meddelande ut för att bekräfta detta.
                    print("")
                    print(f"It's super effective! You stole {player_choice} from Computer!")
                    print("! You scored a point !")
                    print("")

            else:
                # Om spelaren plockar upp ett kort som den redan har 3 av så totalen blir 4 ges ett poäng.
                new_card = deck.draw()
                if new_card:
                    player_cards.append(new_card)
                is_four_of_a_kind, player_cards = check_four_cards(player_cards)
                if is_four_of_a_kind:
                    player_score += 1
                    last_card = player_cards[-1]
                    print("")
                    # clear_terminal()
                    print(print_welcome_message(player))
                    print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
                    print("Player cards: ")
                    print(*player_cards, sep=', ')
                    print(symbols + symbol_list[0])
                    print("")
                    print(f"You picked up {new_card}...")
                    # Ett meddelande för att bekräfta när just det scenariot inträffar.
                    print("... And it made you score a point !")
                    print("")

                else:
                    # Om spelaren enbart gissar fel och behöver ta upp ett kort.
                    print(print_welcome_message(player))
                    print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
                    print("Player cards: ")
                    print(*player_cards, sep=', ')
                    print(symbols + symbol_list[0])
                    print("")
                    print(f"Computer doesn't have the card you asked for. Go Fish!")
                    # Berättar vilket kort som plockades upp från högen.
                    print(f"You picked up: {player_cards[-1]}")
                    print("")

        else:
            # Om spelaren skulle få för sig att gissa på ett kort den inte har på handen.
            print(print_welcome_message(player))
            print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
            print("Player cards: ")
            print(*player_cards, sep=', ')
            print(symbols + symbol_list[0])
            print("")
            print("You can only pick cards you have on your hand. Better luck next time.")
            print("")

        # Datorns logik:
        # Gissningarna sker slumpmässigt utefter de kort datorn har på handen.
        computer_guesses = random.choice(computer_cards)
        if computer_guesses in player_cards:
            while computer_guesses in player_cards:
                player_cards.remove(computer_guesses)
                computer_cards.append(computer_guesses)
            # en text skrivs ut när datorn tar ett kort från spelaren.
            print("Computer guessing . . . ", computer_guesses)
            print(f"{nemesis} stole {computer_guesses} from you!")
            print("")

            # Om datorn har 4 av samma kort på handen ges den ett poäng.
            computer_card_count = computer_cards.count(computer_guesses)
            if computer_card_count == 4:
                computer_cards = [card for card in computer_cards if card != computer_guesses]
                computer_score += 1
                # Och ett meddelande skrivs ut för att visa för spelaren.
                print("! Computer scored a point !")
                print("")

        else:
            # Om datorn gissar fel och behöver plocka upp ett kort från högen.
            print(f"Computer guessing . . . {computer_guesses}!")
            print("Your nemesis guessed wrong. Go Fish! ")
            print("")
            new_card = deck.draw()
            computer_cards.append(new_card)

        # När resultaten är inne: Den som först får 3 poäng vinner spelet.
        if player_score >= 3:
            clear_terminal()
            print(print_welcome_message(player))
            print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
            print("Player cards: ")
            print(*player_cards, sep=', ')
            print(symbols + symbol_list[0])
            print(draw_border("Game Over! You Won!"))
            # Och får välja om den vill spela igen. Om svaret är nej återgår programmet till huvudmenyn.
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break
            else:
                # Om nej så startas spelet om.
                player_score = 0
                computer_score = 0
                player_cards = []
                computer_cards = []
                deck.reset()
                clear_terminal()
                player_cards, computer_cards = deck.deal_cards()
                print(print_welcome_message(player))
                print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
                print("Player cards: ")
                print(*player_cards, sep=', ')
                print(symbols + symbol_list[0])
                print("")

        elif computer_score >= 3:
            clear_terminal()
            print(print_welcome_message(player))
            print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
            print("Player cards: ")
            print(*player_cards, sep=', ')
            print(symbols + symbol_list[0])
            print(draw_border("Game Over! Computer Won!"))
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break
            else:
                player_score = 0
                computer_score = 0
                player_cards = []
                computer_cards = []
                deck.reset()
                clear_terminal()
                player_cards, computer_cards = deck.deal_cards()
                print(print_welcome_message(player))
                print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
                print("Player cards: ")
                print(*player_cards, sep=', ')
                print(symbols + symbol_list[0])
                print("")


if __name__ == "__main__":
    main_game()
