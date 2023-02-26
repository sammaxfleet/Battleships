
import gspread
import random 

# Import random package to be able to create random integers within the game

 #  User friendly interaction before starting game.
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
        return Battleship(body)

    def __init__(self, body):
        self.body = body 

b = Battleship.build((1,1), 5, "S")
b2 = Battleship ([(1,2), (2,2), (3,3), (4,2), (5,2)])



def board (board_width, board_height, shots): 
    header  = "#" + "-"* board_width + "#"
    print(header)

    shots_set = set(shots)
    for y in range(board_height):
        row = []
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
            Battleship.build ((5,8), 2, "S"),
            Battleship.build ((2,3), 4, "E"),
    ]

    print(battleships)

    exit(0)
    
    shots = []
    while True: 
        inp = input("Where do you want to shoot on the board?\n")
        xstr, ystr = inp.split (",")
        x = int(xstr)
        y = int(ystr)
        shots.append((x,y))
        board(10, 10, shots)
