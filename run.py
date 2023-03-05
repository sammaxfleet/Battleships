import random
    #User Interaction Section 1.
def run_game():
    print ("Hi welcome to Battleships 2023!") 
    ans = input ("Do you wish to review the rules before playing? (yes/no)")
    if ans.lower () == 'yes':
            print("Rules...\n","1.The Battleship Board has a 10 by 10 layout \n", "2.To take your shot at the board type a number followed a comma  follwed by another number, example.   1,1 \n", "3.The battleships are invisible, the board will tell you if your shot has hit by using an X... a missed shot will be represented by a * \n " "4..You can play as many times as you wish.")
        
    elif ans == "no":
            print ("Ok, come back when you're ready.")
run_game()    
#Section 3- How to represent the battleships & the rules/ data structures. 
class Battleship(object):  

    @staticmethod
    def build(top, length, direction):
        body = []
        for i in range(length):
            if direction == "UP":
                el = (top[0], top[1] - i)
            elif direction == "DOWN":
                el = (top[0], top[1] + i)
            elif direction == "LEFT":
                el = (top[0] -i, top[1])
            elif direction == "RIGHT":
                el = (top[0] +i, top[1])

            body.append(el) 
        return Battleship(body)
        print(body)

    def __init__(self, body):
        self.body = body
#User interaction 2 & continuation of plotting board & shots  #section 3b 
if __name__ == "__main__":
    battleships = [
    Battleship.build ((1,1), 2, "UP"),
    Battleship.build ((5,8), 3, "UP"),
    Battleship.build ((2,3), 4, "RIGHT"),]
        
    for b in battleships:
        print (b.body)

#Board Layout & Shots. Section 2 

def board_layout(board_width, board_height, shots):
    print("#" + "-" * board_width + "#")
    print(header)

    for y in range(board_height):
        row = []
        for x in range(board_width):
            if (x,y) in shots:
                ch = "4"
            else:
                ch = " "
            row.append(ch)
        print("|" + "".join(row) + "|")
    
    footer = ("#" + "-" * board_width + "#")
    print(footer)

# Putting the battleships onto the board  
def render(board_width, bard_height, battleships):
    header("#" + "-" * board_width + "#")
    print(header)
    footer = ("#" + "-" * board_width + "#")
    print(footer)
    board = []
    board.append in b.body ([None for y in range (board_height)])
    board.append in b.body ([None for x in (board_width)])
    for b in battleships:
        for x, y in b.body:
            board [x][y] = "0"

    for y in board_height_:
        row = []
        for x in range(board_width):
            row.append(board[x][y] or " ")
        print("|" + "".join(row) + "|")

    print(header)
   
#section 2b
    shots = []

    while True:
        inp= input ("Where on the board do you want to shoot your missile?..\n")
        xstr, ystr = inp.split (",")
        x = int(xstr)
        y = int(ystr)

        shots.append((x,y))
        board_layout (10, 10, shots)