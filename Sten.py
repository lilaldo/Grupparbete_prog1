import random
import os

ui_width = 40

def get_username():
    if os.path.exists('username.txt'):
        with open('username.txt', 'r') as f:
            return f.read()

class RockPaperScissor:

    def __init__(self):
        self.options = ["sten", "sax", "påse"]
        self.user_score = 0  # spelarens poäng
        self.computer_score = 0  # datorns poäng
        self.game_over = False

    def play(self):
        while not self.game_over:
            self.clear_screen()
            self.spel()

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def exit_game(self):
        return True

    def spel(self):
        print("=" * 40)
        print(f"|  .:Välkommen {get_username()} till sten, sax, påse:.  |".center(ui_width))
        print("=" * 40)
        print(f"| Poäng - Utmanare: {self.user_score} | Datorn: {self.computer_score} |".center(40))
        print("| Först till 3 vinner! |".center(ui_width))
        print("-" * 40)
        players_choice = input("| Välj sten, sax eller påse: ").lower()
        print("-" * 40)

        if players_choice not in self.options:
            print("Ogiltig inmatning, Vänligen försök igen.")
            return

        computer_choice = random.choice(self.options)

        print(f"| Du valde {players_choice}. Datorn valde {computer_choice}.")

        if players_choice == computer_choice:
            print("| Det blev oavgjort.")
        elif (players_choice == "sten" and computer_choice == "sax") or \
                (players_choice == "sax" and computer_choice == "påse") or \
                (players_choice == "påse" and computer_choice == "sten"):
            print("| Du vann")
            self.user_score += 1

        else:
            print("| Datorn vann")
            self.computer_score += 1

        if self.computer_score == 3 or self.user_score == 3:
            self.game_over = True  # Markera spelet som över
            self.clear_screen()
            print("=" * 40)
            print(f"|  .:Välkommen {get_username()} till sten, sax, påse:.  |".center(ui_width))
            print("=" * 40)
            print(f"| Poäng - Utmanare: {self.user_score} | Datorn: {self.computer_score} |".center(40))
            print("| Först till 3 vinner! |".center(ui_width))
            print("-" * 40)

        if self.game_over:
            cont = input("| Vill du spela igen (ja/nej): ").strip().lower()
            while cont not in ["ja", "nej"]:
                print("| Ogiltig inmatning. Vänligen svara med 'ja' eller 'nej'.")
                cont = input("| Vill du spela igen (ja/nej): ").strip().lower()

            if cont == "nej":
                self.exit_game()


if __name__ == "__main__":
    game = RockPaperScissor()
    while True:
        game.clear_screen()
        game.spel()
        print("-" * 40)