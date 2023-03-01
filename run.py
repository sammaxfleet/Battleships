import random

def render(board_width, board_height):
    print("#" + "-" * board_width + "#")
if __name__ == "__main__":
    render (10,10)
    inp= input ("Where on the board do you want to shoot your missile?..\n")
    xstr, ystr = inp.split (",")
    x = int(xstr)
    y = int(ystr)
    print (x)
    print (y)
    print (x+y)
