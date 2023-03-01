
#outline for the board & ineraction with the user

import random

def board_layout(board_width, board_height):
    print("#" + "-" * board_width + "#")

    for i in range(board_height):
        print("|" + " " * board_width + "|")
    
    footer = ("#" + "-" * board_width + "#")
    print (footer)
        
if __name__ == "__main__":
    board_layout (10,10)
    inp= input ("Where on the board do you want to shoot your missile?..\n")
    xstr, ystr = inp.split (",")
    x = int(xstr)
    y = int(ystr)
    print (x)
    print (y)
    print (x+y)
