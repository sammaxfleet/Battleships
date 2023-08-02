import random
#User Interaction/Rules Section 1.
def run_game():
    print ("Hi welcome to Battleships Game 2023!")
    while True:
        ans = input("The rules are needed to be reviewed before starting the game, are you ready tosee them? (yes/no)")
        if ans == 'yes':
            print("Rules...\n","1.The Battleship Board has a 10 by 10 layout \n", "2.To take yourshot at the board type a number followed a comma followed by another number, example... 1,1 \n", "3.The battleships are invisible, the board will tell you if your shot has hit by using a 4... a missed shot will be represented by a * \n " "4..You can play as many times as you wish.")
            break
        elif ans == 'no':
            print ("Ok, come back when you're ready.")
            continue
        else:
            print ('You did not say yes/no. Please try again.')
            continue
    
def create_grid(size):
    return [[' ' for _ in range(size)] for _ in range(size)]

def print_grid(grid):
    print(" +" + "-+" * len(grid))
    for i, row in enumerate(grid):
        print(f"| {' '.join(row)} |")
    print(" +" + "-+" * len(grid))

def place_ship(grid, row, col):
    grid[random.randint(0,row)][random.randint(0,col)] = 'X'


def place_computer_ship(grid):
    NUM_COMPUTER_SHIPS = 3
    placed_ships = set()
    for _ in range(NUM_COMPUTER_SHIPS):
        while True:
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            if (row, col) not in placed_ships:
                place_ship(grid, row, col)
                placed_ships.add((row, col))
                break

def get_user_guess():
    try:
        guess_row = int(input(f"Guess Row (0-{GRID_SIZE-1}): "))
        guess_col = int(input(f"Guess Col (0-{GRID_SIZE-1}): "))
        if 0 <= guess_row < GRID_SIZE and 0 <= guess_col < GRID_SIZE:
            return guess_row, guess_col
        else:
            print("Oops, that's not even in the ocean! Try again.")
            return get_user_guess()
    except ValueError:
        print("Invalid input. Please enter numbers between 0 and 7.")
        return get_user_guess()

def is_hit(grid, row, col):
    return grid[row][col] == 'X'

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
    
    # Play the game 
    play_game(grid)