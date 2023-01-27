"""
projekt_22.py: Druhý projekt do Engeto Online Python Akademie

author: Rostislav Rabiec
email: rosta.rabiec@icloud.com
discord: Rostislav R.#9305
"""

import random


def main():
    create_greetings()
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
"""
    return print(greeting, rules)


def create_gamefield():
    field = f"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
"""
    return field


def input_player1():
    while True:
        player1 = input("Player X | Please enter your number: ")
        if player1 == "0" or len(player1) > 1:
            print("Please, enter number from 1 to 9.")
            continue
        elif not player1.isdigit():
            print("Please, enter only number, not another symbols.")
            continue 
        else:
            return player1


def input_player2():
    while True:
        player2 = input("Player O | Please enter your number: ")
        if player2 == "0" or len(player2) > 1:
            print("Please, enter number from 1 to 9.")
            continue
        elif not player2.isdigit():
            print("Please, enter only number, not another symbols.")
            continue
        else:
            return player2

def play_game():
    print("Let's start the game.")
    print(40 * "-")
    game_field = create_gamefield()
    print(game_field)
    print(40 * "=")
    player1 = input_player1()
    print(40 * "=")
    
    print(40 * "=")    
    player2 = input_player2()
    print(40 * "=")
        

       
        
        
    
               


if __name__ == "__main__":
    main()