"""
projekt_22.py: Druhý projekt do Engeto Online Python Akademie

author: Rostislav Rabiec
email: rosta.rabiec@icloud.com
discord: Rostislav R.#9305
"""

# Vytvoř pozdrav a vysvětli pravidla hry
# Herní pole
# Samotný chod hry


def main():
    create_greetings()
    create_gamefield()
    play_game()


def create_greetings():
    separator = 40 * "="
    greeting = f"Welcome to Tic Tac Toe\n{separator}"
    rules = f"""
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal
* vertical
* diagonal row
{separator}
Let's start the game
"""
    return print(greeting, rules)


def create_gamefield():
    row = "+---+---+---+"
    set1 = "|   |   |   |"
    set2 = "|   |   |   |"
    set3 = "|   |   |   |"
    field = f"{row}\n{set1}\n{row}\n{set2}\n{row}\n{set3}\n{row}"
    return field

