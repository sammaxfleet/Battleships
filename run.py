import random

#User Interaction 1
def run_game():
    print ("Hi welcome to Battleships 2023!") 
    ans = input ("Do you wish to review the rules before playing? (yes/no)")
    if ans.lower () == 'yes':
            print("Rules...\n","1.The Battleship Board has a 10 by 10 layout \n", "2.To take your shot at the board type a number followed a comma  follwed by another number, example.   1,1 \n", "3.The battleships are invisible, the board will tell you if your shot has hit by using an X... a missed shot will be represented by a * \n " "4..You can play as many times as you wish.")
        
    elif ans == "no":
            print ("Ok, come back when you're ready.")
run_game()    

#Board Layout & Shots.

def board_layout(board_width, board_height, shots):
    print("#" + "-" * board_width + "#")

    for y in range(board_height):
        row = []
        for x in range(board_width):
            if (x,y) in shots:
                ch = "4"
            else:
                ch = " "
            row.append(ch)
        print("|" + "".join(row) + "|")

        #print("|" + " " * board_width + "|")
    
    footer = ("#" + "-" * board_width + "#")
    print(footer)



        #User interaction 2 & continuation of plotting board & shots 
if __name__ == "__main__":
    board_layout (10,10, [(3,1), (4,5), (8,1)])

    inp= input ("Where on the board do you want to shoot your missile?..\n")
    xstr, ystr = inp.split (",")
    x = int(xstr)
    y = int(ystr)