# BATTLESHIPS GAME Portfolio Project 3 - Python Essentials.

- [BATTLESHIPS GAME Portfolio Project 3 - Python Essentials.](#battleships-game-portfolio-project-3---python-essentials)
- [Purpose of the project & description](#purpose-of-the-project---description)
- [Game creation breakdown.](#game-creation-breakdown)
- [Flow chart example -](#flow-chart-example--)
- [Credits](#credits)
- [Testing](#testing)


# Purpose of the project & description


The purpose of this project was to build an interactive brain game for a user to play against the computer.

The locations of the fleets are concealed from the other player in this case the user is playing against the computer. I've started off my game by having some simple interacative questions with the User welcoming them, which then leads to the big question of the game ." Where do you want to shoot on the board?". The User taking a shot at the battleship which is represnentd by a "4".
a "*" represents a miss
a "4" represents a hit.
THe board is default 10x10 column and rows which is explained within the rules.
After 10 goes it restarts from the top of the game. 
Giving the user the chance of guessing over 100 squares on the grid, there's 3 battleships which take up approximately 10 squares. So there's a good ratio of possiblity for the player but it also makes it a fun challenge. 


# Features

## Welcome Message 
<img width="728" alt="Screenshot 2023-07-31 at 14 57 35" src="https://github.com/sammaxfleet/Battleships/assets/114914739/47fc9ea7-c9cf-4bdb-a237-adf1d40686be">

  A Welcome message, directing the user to read the rules pre playing. If you choose another option than yes/no on the keyboard number or letter it will not work.

<img width="1029" alt="Screenshot 2023-07-31 at 15 14 20" src="https://github.com/sammaxfleet/Battleships/assets/114914739/f30aec9c-1c35-4187-9469-84dcd3881660">

The Rules are then displayed to give the user a breakdown of how the game works before the button bashing begins. 


<img width="426" alt="Screenshot 2023-07-31 at 15 16 57" src="https://github.com/sammaxfleet/Battleships/assets/114914739/ac5b5860-edfb-4926-be4f-7016a20f1ab0">

For example the Missile above is fired at 1,1. The 4 represents the shot being succesful. 







# Game creation breakdown.

Stages of the game needed to create.  


  1. Create a welcoming introduction to the game with user response.
  2. Ask the user if they wish to view the rules to continue on playing. 
  3. Once explained- ask the user where they want to shoot on the board?
  4. Create the board 10x10. 
  5. Mark the shots by a “4” and misses by a “*”.
  6. Create the battleships/ decide what they look like.
  7. Hide the battleships from the user.
  8. Run the game in a loop of 10 shots, then let go back to the beginning. 
  9. Set a game over so they user can start again from the beginning with either a  Win/ 
    Loss print. 



# Flow chart example -

<img src = "images/screenshot1.png">


# Credits

Youtube tutorial- Battleships
https://www.youtube.com/watch?v=Gi0Fdyhk1_0&t=511s

Stackoverflow was great resource.


# Testing

PEP 8
https://extendsclass.com/python-tester.html

<img src = "img/screenshot2.png">

Deployment & Error Handling. 


