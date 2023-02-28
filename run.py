
# Import random package to be able to create random integers within the game
import random 

# User interaction at the start of the game.
# Welcoming the user to the game, giving them the option to also view the rules before they play.

def RunGame (): 
    print ("Hello, Welcome to Battleships2023!") 
    ans = input ('Are you ready to play (yes/no)')
    if ans.lower () == 'yes':
        print ('Ok, lets quickly recap the rules before we play!' )
    


#Developing the Gameboard for the user to play on. 

class GameBoard(object):

    def __init__(self, battleships, board_width, board_height):
        self.battleships = battleships
        self.shots = []
        self.board_width = board_width 
        self.board_height = board_height

 # * Update the battleships with any shots to them. 
 # * Save after wether the shot was a hit or a miss.  
    
    def take_shot(self, shot_location):
        hit_battleship = None
        is_hit = False
        for b in self.battleships:
            idx = b.body_index(shot_location)
            if idx is not None:
                is_hit = True
                b.hits[idx] = True
                hit_battleship = b
                break
        
        self.shots.append(Shot(shot_location, is_hit))
        return hit_battleship

    def is_game_over(Self):
        for b in self.battleships: 
            if not b.is_destroyed():
                return False 
        return True 

        # For each battleship, is it destroyed? 
        # If yes for all, return True, else False. 

    

 #Battleship Building & layout. 


class Battleship(object):  

    @staticmethod
    def build(head, length, direction):
        body = []
        for i in range(length):
            if direction == "N":
                el = (head[0], head[1] - i)
            elif direction == "S":
                el = (head[0], head[1] + i)
            elif direction == "W":
                el = (head[0] - i, head[1])
            elif direction == "E":
                el = (head[0] + i, head[1])

            body.append(el)

        return Battleship(body,)

    def __init__(self, body):
        self.body = body 
        self.hits = [False] * len(body)

    def body_index(self, location):
        try:
            return self.body.index(location)
        except ValueError:
            return None 

    def is_destroyed(self):
        return all(self.hits)

#Game Render 

def render(game_board, show_battleships=False):
    header  = "#" + "-"* game_board.board_width + "#"
    print(header)

    # Construct empty board 
    board = []
    for _ in range(game_board.board_width):
        board.append([None for _ in range (game_board.board_height)])
    if show_battleships:

    # Add the battleships to the board 
        for b in game_board.battleships:
         for x, y in b.body:
            board[x][y] = "0"

    # Add the shots to the board
    for sh in game_board.shots: 
        x, y = sh.location
        if sh.is_hit:
            ch = "X"
        else: 
            ch = "*"
        board [x][y] = ch 


    for y in range(game_board.board_height): 
        row = []
        for x in range(game_board.board_width):
            row.append(board[x][y] or " ")
        print("|" + "".join(row) + "|")
    print(header)


# Make the Board then get player input 

def board (board_width, board_height, shots): 
    header  = "#" + "-"* board_width + "#"
    print(header)

    shots_set = set(shots)
    for y in range(board_height):
        row = ""
        for x in range(board_width):
            if (x,y) in shots_set: 
                ch = "X"
            else:
                ch = " "
            row.append(ch)

        print("|" + "".join(row) + "|")
    
    print(header)


    if __name__ == "__main__":
        battleships = [
            Battleship.build ((1,1), 2, "N"),
            Battleship.build ((5,8), 2, "N"),
            Battleship.build ((2,3), 4, "E"),
    ]

    for b in battleships:
        print(b.body)
    
    game_board = GameBoard(battleships, 10, 10)

    while True: 
        inp = input("Whereabouts do you want to shoot your misile onto the board?\n")
        #User could give bad input need to sort 
        xstr, ystr = inp.split (",")
        x = int(xstr)
        y = int(ystr)

        game_board.take_shot((x,y))
        render(game_board)

        if game_board.is_game_over():
            print("YOU WIN!")
            break
print (board)

        #if game_has_ended: 
        #   print "YOU WIN"
        #   break 