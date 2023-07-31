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


run_game()    
#Section 3- How to represent the battleships on the board. & the rules/ data structures. 

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
#Board Layout & Shots represented. Section 2 

def board_layout(board_width, board_height, shots):
    header = ("#" + "-" * board_width + "#")
    print(header)

    for y in range(board_height):
        row = []
        
        for x in range(board_width):
            column = []
            if (x,y) in shots:
                ch = "4"
            else:
                ch = " "
            row.append (ch)
            column.append (ch)
        print("|" + "".join(row) + "|")
    
        
    
#Building the battleships & Shots continued 

if __name__ == "__main__":
        
    shots = []
    while True:

        inp= input ("Where on the board do you want to shoot your missile?..\n")
        xstr, ystr = inp.split (",")
        x = int(xstr)
        y = int(ystr)
        shots.append((x,y))
        board_layout (10, 10, shots)
    battleships = [
        Battleship.build ((1,1), 2, "UP"),
        Battleship.build ((5,8), 3, "UP"),
        Battleship.build ((2,3), 4, "RIGHT"),
        ]
        
    for b in battleships:
            print (b.body)

