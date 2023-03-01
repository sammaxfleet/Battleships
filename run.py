import random

#User Interaction 1
def run_game():
    print ("Hi welcome to Battleships 2023!") 
    ans = input ("Do you wish to review the rules before playing? (yes/no)")
    if ans.lower () == 'yes':
            print("Rules...\n",".The Battleship Board has a 10 by 10 layout \n", ".To take your shot at the board type a number followed a comma follwed by another number, example 1,1 \n""The battleships are invisible, the board will tell you if your shot has hit by and X or a missed shot will be represented by a * \n " ".You can play as many times as you wish.")
    elif ans == "no":
            print ("Come back when you're ready")
#Board Layout 

def board_layout(board_width, board_height):
    print("#" + "-" * board_width + "#")

    for i in range(board_height):
        
        print("|" + " " * board_width + "|")
    
    footer = ("#" + "-" * board_width + "#")
    print (footer)

        #User interaction 2 & shots 
def play_turn():
    board_layout (10,10)
    inp= input ("Where on the board do you want to shoot your missile?..\n")
    xstr, ystr = inp.split (",")
    x = int(xstr)
    y = int(ystr)
    print (x)
    print (y)
    print (x+y)

run_game()