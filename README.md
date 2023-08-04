 # BATTLESHIPS GAME, PROJECT 3 CODE INSTITUTE 
   Python Essentials.

Heroku link - https://battleships2023.herokuapp.com/

GitHub Link - https://github.com/sammaxfleet/Battleships

## Things I've worked on since the last submission.

- I've kept the welcome message the same, but added the grid question for the user to be able to change the grid size.
- The board wasn't working properly. 
- The shots at the board were working but there was no battleships.
- I've made the battleships invisible, and looped the game so it has a try of 10 shots. 
- I've tried to focus on smoother testing and deployment. 

#  Responsiveness -

<img width="1108" alt="Screenshot 2023-08-04 at 10 15 05" src="https://github.com/sammaxfleet/Battleships/assets/114914739/2e7f39a9-cb01-4f8f-9954-3990277bc287">


# Table Of Contents - 

- [BATTLESHIPS GAME, PROJECT 3 CODE INSTITUTE - Python Essentials.](#battleships-game--project-3-code-institute---python-essentials)
  * [Things I've worked on since the last submission.](#things-i-ve-worked-on-since-the-last-submission)
- [Responsiveness -](#responsiveness--)
- [Table Of Contents](#table-of-contents)
- [Creators Goal & Description -](#creators-goal---description--)
  * [Planning Phase -](#planning-phase--)
- [Flow chart  -](#flow-chart---)
- [User Experience](#user-experience)
  * [User Sotries](#user-sotries)
- [Features](#features)
  * [Welcome Message](#welcome-message)
- [Rules](#rules)
- [Grid](#grid)
- [Shots](#shots)
- [Game creation breakdown.](#game-creation-breakdown)
- [Credits](#credits)
- [Testing](#testing)
- [Deployment](#deployment)

# Creators Goal & Description - 

The purpose of this project is to build an interactive brain game for a user to play against the computer.
The game is simple, and repeats in a loop of 10 tries then it restarts. The loop brings a competitive touch to the game, giving the user 10 tries to hit the battleships. 
The grid size is chosen by the user, the maximum it's set to is a grid of 8, if a harder game was to be functioned it could go to 25 for example. 
The rules are explained at the beginning to give the user clear instruction, the user has to blow up the invisible battleships that are randmoised by the computer on the grid.
The user does this by taking shots at the Row/Column. 
Their missile which is represented by a H for hit & an M for Miss fire to try and hit the 3 invisible battleships. 



##  Planning Phase -

 It took me a while to get to a logic that flowed the way I wanted.  My first initial ideas made the game a bit too complex, wanting to constantly add features.
 I watched a few tutorials to get ideas for the game flow..
 The main aim for me was to get the User experience to be smooth, & the biggest challenge I had coding was the battleships and hiding them. 
 Having a clear game flow, made the game much easier to code. 
 My flow chart example below. 
 
# Flow chart  -

 ![Flowchart Template (1)](https://github.com/sammaxfleet/Battleships/assets/114914739/6770f8b3-9a2b-4235-97ca-2e586bd00edc)
 

 # User Experience -
 
 ## User Sotries -
 
1. Welcome message & explain the Rules to the User.
2. Make a board your own size with a Maximum of 8.
3. Any wrong entries throughout the game have messages to identify wrong input. 
4. Fire shots at the board & decide how they register.
5. Decide how the battleships are represented & randomise hits for each game. 
6. Make Battleships invisble for game.
7. Say if shot isn't on the board with a 'H' for hit or 'M' for miss.
8. Make the flow of the game feel user friendly .
9. Loop the game X 10 with a 'Game Over' notification. 

   

# Features -

## Welcome Message -

<img width="373" alt="Screenshot 2023-08-04 at 10 28 54" src="https://github.com/sammaxfleet/Battleships/assets/114914739/1630b738-b9e7-4a4a-a133-3a7217ffd8b2">


A quick, swift intro! The Welcome message goes straight to the point, asking the user if they're ready for the Rules?..

If no...

# Rules -

<img width="374" alt="Screenshot 2023-08-04 at 10 30 32" src="https://github.com/sammaxfleet/Battleships/assets/114914739/af509c3c-8ea8-40c2-8d38-9b90d09b5bbd">

A polite message is left with the rules question still appearing to encourage the user to play. 

If Yes...

<img width="442" alt="Screenshot 2023-08-04 at 10 35 57" src="https://github.com/sammaxfleet/Battleships/assets/114914739/c1d5a1b5-1d7f-48ee-b80c-663ba8544af0">


The rules are explained in bullet points, four bullet points, keeping the logic short and to the point.

# Grid  -
The Grid Size & Game Begins

<img width="298" alt="Screenshot 2023-08-02 at 20 45 15" src="https://github.com/sammaxfleet/Battleships/assets/114914739/68f9aa12-1849-4431-ae7e-7534e508f7d6">


# Shots -
As you shoot it either gets represented by an M or a H

<img width="119" alt="Screenshot 2023-08-02 at 20 45 59" src="https://github.com/sammaxfleet/Battleships/assets/114914739/fb12ebc9-fe5d-43a0-a8ca-a5c029497416">

The games loops upto 10 tgoes o try and hit all 3 battleships, then resets. 

<img width="768" alt="Screenshot 2023-08-02 at 20 47 42" src="https://github.com/sammaxfleet/Battleships/assets/114914739/8b47f69a-e7ef-4e7d-a170-ca6a314d46c7">



# Game creation breakdown -


Comments from the code on how it was created. 

 - User Interaction/Rules Section 1.

 - Create the grid and set the size of the grid + generate positions. 

 - Print entire grid

 - Place battleship positions & store random positions to the file.
  
 - Save ship positions to the JSON file (using 0-based coordinates)

 - User input

 - Hits or Misses

 - Loop game after 10 tries. 
 



# Credits -

- Youtube tutorial- Battleships to understand logic. 
- https://www.youtube.com/watch?v=Gi0Fdyhk1_0&t=511s
- Stackoverflow was great resource.
- https://www.w3schools.com/ 
- https://www.geeksforgeeks.org/ understanding how to make battleships invisible 
- Tutors at code Institute
- Slack meet with the September intake.


# Testing -

PEP 8
Duriing the testing my main error was that my lines of code were too long so I asked the tutors from code institute to help with 
breaking a line.
This was shown with Python Linter & pycodestyle. 

<img width="544" alt="Screenshot 2023-08-04 at 10 01 23" src="https://github.com/sammaxfleet/Battleships/assets/114914739/c45341ac-aaa2-4b59-a067-3d008ceba22f">

https://www.geeksforgeeks.org/break-a-long-line-into-multiple-lines-in-python/

<img width="1226" alt="Screenshot 2023-08-04 at 09 58 07" src="https://github.com/sammaxfleet/Battleships/assets/114914739/07d711a3-02eb-4d2b-be4a-109213d81e4e">


https://extendsclass.com/python-tester.html

https://pep8ci.herokuapp.com/#


Error messages are shown if wrong input

<img width="422" alt="Screenshot 2023-08-04 at 11 29 28" src="https://github.com/sammaxfleet/Battleships/assets/114914739/172b3bbe-38e5-4049-bd17-8cda7d34f734">

<img width="479" alt="Screenshot 2023-08-04 at 11 30 27" src="https://github.com/sammaxfleet/Battleships/assets/114914739/5fe5a4c2-af18-4960-a129-66b99acda619">



# Deployment -

Heroku- The Game is fully functional and deployed by Heroku. 

<img width="738" alt="Screenshot 2023-08-04 at 11 25 33" src="https://github.com/sammaxfleet/Battleships/assets/114914739/e4c785de-681c-49e4-a305-6e876c7f3a57">








