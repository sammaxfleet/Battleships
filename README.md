# BATTLESHIPS GAME Portfolio Project 3 - Python Essentials.

Heroku link - https://battleships2023.herokuapp.com/

Things I've worked on since the last submission.

I've kept the welcome message the same, but added the grid question for the user to be able to change the grid size.
From here the game in my opinion is fully functional. 
Before the shots at the board were working but there was no battleships.
I've made the battleships invisible, and looped the game so it has a try of 10 shots. 
I've tried to focus on smoother testing and deployment. 

#  Responsiveness -

<img width="1125" alt="Screenshot 2023-08-03 at 11 39 50" src="https://github.com/sammaxfleet/Battleships/assets/114914739/084db136-4e5b-4887-b7e4-905aec906e31">

# Planning Phase -

# Flow chart example -
 For Game Creation. 
 ![Flowchart Template (1)](https://github.com/sammaxfleet/Battleships/assets/114914739/6770f8b3-9a2b-4235-97ca-2e586bd00edc)
 
User Stories to achieve:

User Sories 

1. Make a board your own size with a Maximum of 8. 
2. Fire shots at the board & decide how they register.
3. Decide how the battleships are represented & randomise hits for each game. 
4. Make Battleships invisble for game.
5. Say if shot isn't on the board with a 'H' for hit or 'M' for miss.
6. Explain the Rules to the User. 
7. Make the flow of the game feel user friendly .
8. Loop the game X 10.
   


Portfolio Project 3 - Python Essentials.
Purpose of the project & description of game created.
=======
- [BATTLESHIPS GAME Portfolio Project 3 - Python Essentials.](#battleships-game-portfolio-project-3---python-essentials)
- [Purpose of the project & description](#purpose-of-the-project---description)
- [Game creation breakdown.](#game-creation-breakdown)
- [Flow chart example -](#flow-chart-example--)
- [Credits](#credits)
- [Testing](#testing)


# Purpose of the project & description.
>>>>>>> 87fb1c317d72b475cf61e685ef71dc0c42442d17

The purpose of this project is to build an interactive brain game for a user to play against the computer.
The game is simple, and repeats in a loop of 10 tries then it restarts.
The grid size is chosen by the user. The maximum it's set to is a grid of 8, if a harder game was to be functioned it could go to 25 for example. 
The rules are explained at the beginning to give the user clear instruction. 
There's 3 battleships placed Invisibly on the board, the user then has 10 tries to hit the battleships with their missile which is represented by a H for hit 
& an M for Miss. 



# Features

## Welcome Message 

<img width="752" alt="Screenshot 2023-08-02 at 13 30 10" src="https://github.com/sammaxfleet/Battleships/assets/114914739/8154625a-5239-4f0d-844f-5f47f00f9040">

A quick, swift intro! The Welcome message goes straight to the point, asking the user if they're ready for the Rules?..

If no...
# Rules
<img width="766" alt="Screenshot 2023-08-02 at 13 32 56" src="https://github.com/sammaxfleet/Battleships/assets/114914739/ecfaa24d-c070-4657-af60-32425bf3ab62">
A polite message is left, 
With the rules question still appearing to encourage the user to play. 

If Yes...


<img width="1125" alt="Screenshot 2023-08-02 at 13 34 51" src="https://github.com/sammaxfleet/Battleships/assets/114914739/6fbc40ce-a019-49a5-8d27-a0258f4b429b">

The rules are explained in bullet points, four bullet points, keeping the logic short and to the point.

# Grid 
The Grid Size & Game Begins

<img width="298" alt="Screenshot 2023-08-02 at 20 45 15" src="https://github.com/sammaxfleet/Battleships/assets/114914739/68f9aa12-1849-4431-ae7e-7534e508f7d6">


# Shots 
As you shoot it either gets represented by an M or a H

<img width="119" alt="Screenshot 2023-08-02 at 20 45 59" src="https://github.com/sammaxfleet/Battleships/assets/114914739/fb12ebc9-fe5d-43a0-a8ca-a5c029497416">

The games loops upto 10 tgoes o try and hit all 3 battleships, then resets. 

<img width="768" alt="Screenshot 2023-08-02 at 20 47 42" src="https://github.com/sammaxfleet/Battleships/assets/114914739/8b47f69a-e7ef-4e7d-a170-ca6a314d46c7">



# Game creation breakdown.


Comments from the code on how it was created. 

 - User Interaction/Rules Section 1.

 - Function for Grid Size Section 2.

 - Grid styling

 - Battleship Placement 

 - User input

 - Hits or Misses

 - Loop game after 10 tries. 
 




# Credits

- Youtube tutorial- Battleships to understand logic. 
- https://www.youtube.com/watch?v=Gi0Fdyhk1_0&t=511s
- Stackoverflow was great resource.
- https://www.w3schools.com/ 
- https://www.geeksforgeeks.org/ understanding how to make battleships invisible 
- Tutors at code Institute
- Slack meet with the September intake.


# Testing




PEP 8

https://extendsclass.com/python-tester.html

https://pep8ci.herokuapp.com/#

<img src = "img/screenshot2.png">


Deployment & Error Handling 

Heroku- The Game is fully functional and deployed by Heroku. 
<img width="740" alt="Screenshot 2023-08-02 at 21 01 54" src="https://github.com/sammaxfleet/Battleships/assets/114914739/fdb3fcd1-6ccf-49db-98cb-d9d8c3b347ba">



