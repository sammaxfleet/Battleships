import random
    #User Interaction/Rules Section 1.
def run_game():
    print ("Hi welcome to Battleships Game 2023!") 
    
    while True:
        ans = input ("The rules are needed to be reviewed before starting the game, are you ready to see them? (yes/no)")
        if ans == 'yes':
            print("Rules...\n","1.The Battleship Board has a 10 by 10 layout \n", "2.To take your shot at the board type a number followed a comma followed by another number, example... 1,1 \n", "3.The battleships are invisible, the board will tell you if your shot has hit by using a 4... a missed shot will be represented by a * \n " "4..You can play as many times as you wish.")
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

def place_user_ships(grid):
    NUM_USER_SHIPS = 3
    for _ in range(NUM_USER_SHIPS):
        while True:
            try:
                row = int(input(f"Enter the row for your Ship {_+1} (0-{GRID_SIZE-1}): "))
                col = int(input(f"Enter the col for your Ship {_+1} (0-{GRID_SIZE-1}): "))
                if 0 <= row < GRID_SIZE or 0 <= col < GRID_SIZE:
                    place_ship(grid, row, col)
                    break
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Try again.")


def place_computer_ship(grid):
    NUM_COMPUTER_SHIPS = 3
    for _ in range(NUM_COMPUTER_SHIPS):
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        place_ship(grid, row, col)

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