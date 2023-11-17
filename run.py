import random
import json
import os

number_of_tries = 0
# User Interaction/Rules


def run_game():
    if os.path.exists("ship_positions.json"):
        os.remove("ship_positions.json")
    print("Hi welcome to Battleships Game 2023!")
    while True:
        ans = input(
            "Are you ready to review the rules? (yes/no)",
        ).lower()
        if ans == "yes":
            print(
                "Rules...\n",
                "1. Choose the size of your Grid, the maximum is 8 x 8\n",
                "2. Guess row & Column to shoot missile \n",
                "3. The Battleships are invisible \n",
                "4a. The board will tell you if your shot has hit \n",
                "4b. With a H for hit & a M for miss \n",
                "5. The game loops after 10 tries \n",)
            break
        elif ans == "no":
            print("Ok, come back when you're ready.")
            continue
        else:
            print("You did not say yes/no. Please try again.")
        continue


# Create the grid and set the size of the grid + generate positions.


def create_grid(size, ship_positions=None):
    if ship_positions is None:
        ship_positions = set()
    return [
        [(" " if (r, c) not in ship_positions else "X") for c in range(size)]
        for r in range(size)
    ]


# print entire grid


def print_grid(grid):
    print(" +" + "-+" * len(grid))
    for i, row in enumerate(grid):
        print(f"| {' '.join(cell if cell != 'X' else ' ' for cell in row)} |")
    print(" +" + "-+" * len(grid))

# place a ship with value 'X'


def place_ship(grid, row, col):
    grid[row][col] = "X"


# place positions & store random positions to the file.


def place_computer_ship(grid):
    NUM_COMPUTER_SHIPS = 3

    # Load ship positions from JSON file
    try:
        with open("ship_positions.json", "r") as json_file:
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
    with open("ship_positions.json", "w") as json_file:
        json.dump(list(ship_positions), json_file)


# user guesses and game loop
def get_user_guess():
    global number_of_tries
    try:
        if number_of_tries == GRID_SIZE:
            print("GameOver")
            number_of_tries = 0
            run_game()
        guess_row = int(input(f"Guess Row (0-{GRID_SIZE-1}): "))
        guess_col = int(input(f"Guess Col (0-{GRID_SIZE-1}): "))
        number_of_tries += 1
        if guess_row == 1 and guess_column == 1:
           print("Please Guess between 2 & 10 for the gridsize")
           return get_user_guess()

        if 0 <= guess_row < GRID_SIZE and 0 <= guess_col < GRID_SIZE:
            return guess_row, guess_col
        else:
            print("Oops, that's not even in the ocean! Try again.")
            return get_user_guess()
    except ValueError:
        print("Invalid input. Please enter numbers between 0 and 7.")
        return get_user_guess()


# to check if the given value from the user is true in the jsonfile


def is_hit(grid, row, col):
    with open("ship_positions.json", "r") as json_file:
        ship_positions = set(tuple(pos) for pos in json.load(json_file))

    return (row, col) in ship_positions

# play game to start the game and request from the user


def play_game(grid):
    print("Let's play Battleships!")
    print("Try to sink the computer's ships.")
    while True:
        print_grid(grid)
        user_guess_row, user_guess_col = get_user_guess()

        if is_hit(grid, user_guess_row, user_guess_col):
            print("Congratulations! You hit the computer's ship!")
            grid[user_guess_row][user_guess_col] = "H"
        else:
            print("You missed the computer's ship!")
            grid[user_guess_row][user_guess_col] = "M"


# New function


# main function


if __name__ == "__main__":
    # Allow the user to set the grid size
    run_game()
    try:
        GRID_SIZE = int(input("Enter the grid size (e.g., 8): "))
    except:
        print('An error has occured terminating game')

    # Create the game grid
    grid = create_grid(GRID_SIZE)

    # Place user and computer ships
    place_computer_ship(grid)

    # Play the game using the loaded grid
    play_game(grid)
