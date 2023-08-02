import random
import json
import os

number_of_tries = 0
# User Interaction/Rules Section 1.
def run_game():
    if os.path.exists("ship_positions.json"):
        os.remove("ship_positions.json")
    print("Hi welcome to Battleships Game 2023!")
    while True:
        ans = input("The rules are needed to be reviewed before starting the game, are you ready to see them? (yes/no)")
        if ans == 'yes':
            print("Rules...\n","1.The Battleship Board has a 10 by 10 layout \n", 
                  "2.To take your shot at the board type a number followed by a comma followed by another number, example... 1,1 \n", 
                  "3.The battleships are invisible, the board will tell you if your shot has hit by using a 4... a missed shot will be represented by a * \n", 
                  "4.You can play as many times as you wish.")
            break
        elif ans == 'no':
            print("Ok, come back when you're ready.")
            continue
        else:
            print('You did not say yes/no. Please try again.')
            continue

def create_grid(size, ship_positions=None):
    if ship_positions is None:
        ship_positions = set()
    return [[(' ' if (r, c) not in ship_positions else 'X') for c in range(size)] for r in range(size)]

def print_grid(grid):
    print(" +" + "-+" * len(grid))
    for i, row in enumerate(grid):
        print(f"| {' '.join(cell if cell != 'X' else ' ' for cell in row)} |")
    print(" +" + "-+" * len(grid))

def place_ship(grid, row, col):
    grid[row][col] = 'X'

def place_computer_ship(grid):
    NUM_COMPUTER_SHIPS = 3

    # Load ship positions from JSON file or create an empty set if the file doesn't exist
    try:
        with open('ship_positions.json', 'r') as json_file:
            ship_positions = set(tuple(pos) for pos in json.load(json_file))
    except FileNotFoundError:
        ship_positions = set()

    # Place computer ships on the grid
    for _ in range(NUM_COMPUTER_SHIPS):
        while True:
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            if (row, col) not in ship_positions:
                place_ship(grid, row, col)
                ship_positions.add((row, col))
                break

    # Save ship positions to the JSON file (using 0-based coordinates)
    with open('ship_positions.json', 'w') as json_file:
        json.dump(list(ship_positions), json_file)

def get_user_guess():
    global number_of_tries
    try:
        if number_of_tries == 10:
            print("GameOver")
            number_of_tries = 0
            run_game()
        guess_row = int(input(f"Guess Row (0-{GRID_SIZE-1}): "))
        guess_col = int(input(f"Guess Col (0-{GRID_SIZE-1}): "))
        number_of_tries += 1
        if 0 <= guess_row < GRID_SIZE and 0 <= guess_col < GRID_SIZE:
            return guess_row, guess_col
        else:
            print("Oops, that's not even in the ocean! Try again.")
            return get_user_guess()
    except ValueError:
        print("Invalid input. Please enter numbers between 0 and 7.")
        return get_user_guess()

def is_hit(grid, row, col):
    # Load ship positions from JSON file
    with open('ship_positions.json', 'r') as json_file:
        ship_positions = set(tuple(pos) for pos in json.load(json_file))

    return (row, col) in ship_positions



def play_game(grid):
    print("Let's play Battleships!")
    print("Try to sink the computer's ships.")
    while True:
        print_grid(grid)
        user_guess_row, user_guess_col = get_user_guess()

        if is_hit(grid, user_guess_row, user_guess_col):
            print("Congratulations! You hit the computer's ship!")
            grid[user_guess_row][user_guess_col] = 'H'
        else:
            print("You missed the computer's ship!")
            grid[user_guess_row][user_guess_col] = 'M'

if __name__ == "__main__":
    # Allow the user to set the grid size
    run_game()
    GRID_SIZE = int(input("Enter the grid size (e.g., 8): "))

    # Create the game grid
    grid = create_grid(GRID_SIZE)

    # Place user and computer ships
    place_computer_ship(grid)

    # Play the game using the loaded grid
    play_game(grid)