
import gspread
import random 

# Import random package to be able to create random integers within the game

def render (board_width, board_height): 
    header  = "#" + "-"* board_width + "#"
    print(header)

    for i in range(board_height):
        print("|" + " "* board_width + "|")
    print(header)

if __name__ == "__main__":
    render (10, 10)

print('Hello, Welcome to Battleships2023!')
ans = input ('Are you ready to play (yes/no)')
if ans.lower () == 'yes':
    print('Ok, lets do this' )
else: 
    print('Ok, Come back when you are ready') 

 #  User friendly interaction before starting game. 
def where_to_shoot ():
    inp = input ("Where do you want to shoot on the board?\n")
    xstr, ystr = insp.split (",")
    x = int(xstr)
    y = int(ystr)
    print (x)
    print (y)
    print (x + y)

    
