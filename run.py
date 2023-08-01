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

