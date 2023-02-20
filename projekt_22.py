"""
projekt_22.py: Druhý projekt do Engeto Online Python Akademie

author: Rostislav Rabiec
email: rosta.rabiec@icloud.com
discord: Rostislav R.#9305
"""


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


def create_gamefield(field_numbers):
    field = f"""
+---+---+---+
| {field_numbers[6]} | {field_numbers[7]} | {field_numbers[8]} |
+---+---+---+
| {field_numbers[3]} | {field_numbers[4]} | {field_numbers[5]} |
+---+---+---+
| {field_numbers[0]} | {field_numbers[1]} | {field_numbers[2]} |
+---+---+---+
"""
    return field


def input_player(x):
    while True:
        player = input(f"Player {x} | Please enter your number: ")
        if player == "0" or len(player) > 1:
            print("Please, enter number from 1 to 9.")
            continue
        elif not player.isdigit():
            print("Please, enter only number, not another symbols.")
            continue 
        else:
            return int(player)


def player_move(y, z):
    while True:
        print(40 * "=")  
        player = input_player(y)
        print(40 * "=")
        if z[player - 1] == "X" or z[player - 1] == "O":
            print("Field is already signed. Please choose another one.") 
            continue            
        else:    
            z[player - 1] = y
            return print(create_gamefield(z))
                
                          
def play_game():
    field_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    game = True
    print("Let's start the game.")
    print(40 * "-")
    print(create_gamefield(field_numbers))
    while game:
        for move in "X", "O": 
            player_move(move, field_numbers)
            continue
       
       
if __name__ == "__main__":
    main()
