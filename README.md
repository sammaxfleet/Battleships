 # BATTLESHIPS GAME, PROJECT 3 CODE INSTITUTE 
   Python Essentials.



Heroku link - https://battleships2023.herokuapp.com/

GitHub Link - https://github.com/sammaxfleet/Battleships


## Things I've worked on since the last submission.

Submission 2
- I've kept the welcome message the same, but added the grid question for the user to be able to change the grid size.
- The board wasn't working properly.
- The shots at the board were working but there was no battleships.
- I've made the battleships invisible, and looped the game so it has a try of 10 shots. 
- I've tried to focus on smoother testing and deployment. 


Submission 3

- Error handling has been a big focus, getting  a more efficient running game for the User.
- Changing the grid size, which gives changes the amount of shots to the grid size, it enhances the difficulty.
- Deployment in the Readme
- More thorough testing with User Stories being added.
- Testing in the Readme
- Better Commits 



#  Responsiveness -

<img width="1108" alt="Screenshot 2023-08-04 at 10 15 05" src="https://github.com/sammaxfleet/Battleships/assets/114914739/2e7f39a9-cb01-4f8f-9954-3990277bc287">


# Table Of Contents - 





# Creators Goal & Description - 

The purpose of this project is to build an interactive brain game for a user to play against the computer.
The game is fun & the difficulty can be adjusted depedning on the users preference. 
The grid size is chosen by the user, the minimum grid size is 3 & the maximum is 10. 
The higher the grid size the more attempts the User gets to shoot at the battleship. 

The rules are explained at the beginning to give the user clear instruction before starting.
The user has to blow up the invisible battleships that are randmoised by the computer on the grid, th he user gets to do this by taking shots at the Row/Column which are
represented by a 'H' for hit and a 'M' for miss. 
There are 3 invisible battlehsips that randomise. 


##  Planning Phase -

 It took me a while to get to a logic that flowed the way I wanted. I watched this tutorial first of all to get an idea
 Link: 
 https://www.youtube.com/watch?v=Gi0Fdyhk1_0&t=9s

 I took inspiration from the Peer code review page on slack and this tutorial to create the game which was uniquq as my creation. 
 
 My first initial ideas made the game a bit too complex, wanting to constantly add features! 
 The main aim for me was to get the User experience to be smooth and the error handling to be efficient aswell as it to be fun and have it's own personalised touch.  
 The biggest challenge I had coding was the battleships and hiding them. 
 Once I conquered this it was about getting the logic to flow. 

# Game creation breakdown 


 - User Interaction/Rules Section 1.

 - Create the grid
 
 - Set the size of the grid + generate shots

 - Print entire grid & choose how shots are represented

 - Place battleship positions & store random positions to the file whilst visible. 
  
 - Save ship positions to the JSON file (using 0-based coordinates)

 - Make battlehips invisible & randomise each new game try

 - Make grid size changeable

 - Change GridSize & Shots so difficulty level can be changed

 - Run through error handling to make sure there's a smooth experience

 - Game over 

   
 
# Flow chart  -

Original Flow Chart -

 ![Flowchart Template (1)](https://github.com/sammaxfleet/Battleships/assets/114914739/6770f8b3-9a2b-4235-97ca-2e586bd00edc)

Updated Flow Chart - 
 

   

# Game Layout

## Welcome Message -

<img width="457" alt="Screenshot 2023-11-19 at 16 08 34" src="https://github.com/sammaxfleet/Battleships/assets/114914739/314e84ba-7130-4b65-825e-df2000f16bbf">


A quick, swift introduction to the game! The Welcome message gets straight to the point, asking the user if they're ready for the rules before starting the game. 

## Answer NO - 

<img width="467" alt="Screenshot 2023-11-19 at 16 09 13" src="https://github.com/sammaxfleet/Battleships/assets/114914739/3fa7bdfa-1cc8-436f-8ec2-e7abaad89cd0">

If No a polite message is left with the rules question still appearing to encourage the user to play. 


# Answer Yes & Rules 

<img width="656" alt="Screenshot 2023-11-19 at 16 10 45" src="https://github.com/sammaxfleet/Battleships/assets/114914739/d5827dfe-5106-4a8b-bd72-71863407fcbc">


The rules are explained using a numbered list. This give clarity to the User before being thrown straight to the Game Board. 
If they've never played battleships before the rules are essential and even if so there's many different versions. 

Rules...
 1. Firstly the Battleships are invisible!! 
 2. The board will tell you if your shot has hit! 
 3. a H is for hit & an M for miss! 
 4. To start choose the size of your Grid choose between 3 & 10 
 5. The game gets harder the bigger the grid 
 6. You get as many tries as the size of your grid chosen 
 7. Guess row & Column to shoot missile between 1 & 10 
 8. After your tries are complete it will be GameOver 



# Choosing Grid Size

<img width="609" alt="Screenshot 2023-11-19 at 16 11 52" src="https://github.com/sammaxfleet/Battleships/assets/114914739/cf4c933b-f522-44b2-b771-4834723d5c69">

Here the user can select the grid size depending on the difficulty level they wish to play. 


## Guess row & guess Column SHOTS

<img width="448" alt="Screenshot 2023-11-19 at 16 12 30" src="https://github.com/sammaxfleet/Battleships/assets/114914739/c6b7bcfa-78c5-43fa-a7d1-f20445607ca0">

Guess row & Column to shoot your missile 

## Amount of Tries & Gameover

 <img width="742" alt="Screenshot 2023-11-19 at 16 13 45" src="https://github.com/sammaxfleet/Battleships/assets/114914739/cd5fa14f-43d0-4b77-beb7-5d909a690008">

The amount of tries matches to the gridsize as explained in the rules. After the Game Over the game resets. 


 



# Deployment -


Use the following steps to deploy the poject to Heroku:

1. Use the "pip freeze -> requiremnts.txt" command in the gitPod terminal; to save any libraries that need to be installed to the project files in Heroku.
2. Login or create a Heroku account.
3. Click the "New" button in the upper right corner and select "Create New App".
4. Choose an app name and your region and click "Create App". Note: the app name must be unique.
6. G5. o to the "Settings" tab, add the python build pack and then the node.js build pack. This is to ensure the project functions correctly with the Code Institute pre-installed template.
7. Create a "Config VAR" with the 'CREDS' key and the enter the value of the creds.json file.
8. Create a second "Config VAR" with the key of 'PORT' and value of '8000'
9. Go to the "Deploy" tab and pick GitHub as a deployment method.
10. Search for a repository to connect to.
11. Click enable automatic deploys and then deploy branch.
12. Wait for the app to build and then click on the "View" link.


You can fork the repository by following these steps:

Go to the GitHub repository.
Click on the Fork button in the upper right-hand corner.
You can clone the repository by following these steps:

Go to the GitHub repository.
Locate the Code button above the list of files and click it.
Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard.
Open Git Bash.
Change the current working directory to the one where you want the cloned directory.
Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY).
Press Enter to create your local clone.


The Game is fully functional and deployed by Heroku. 

<img width="761" alt="Screenshot 2023-11-19 at 16 39 59" src="https://github.com/sammaxfleet/Battleships/assets/114914739/143fb2c3-2580-4dba-bbf2-a5898d0c8dc8">




# Testing 

## User Stories


Issue
1. To create a Welcome Message

   User Story:

   A message the tells the User the game is starting, that is friendly and inviting for the user to start the game.

   
2. To Explain the Rules

   User Story:
   
   To Explain the rules before the game starts, have a simplified way of explaining the rules. Maybe bullet points would be good and a YES/NO to continue with a loop!
   Make the points short and snappy so the user can understand. 

   
3. To allow the user to choose the Gridd size depending on the difficult they wish to play

   User Story:

   Difficulty level being able to be chosen with the board size being adaptable between 2 & 10!
   A grid of 1 is not possible to play this game so 2-10 is ideal.

4. Create the Game Board

   User Story:

   Decide how the game board is going to look maybe it being represented by "- and a "#" or '+' on the corners is great.
   Something visual  and bold so the users can see end of the grid clearly to know where to shoot.

5. Create the battleships
   
   User Story: For the battleships to be invisible and change at random every time we rungame function. Maybe created 2/3 battleships. 

6. Decide how Shots are Represented

   User Story: Create shots decide how they're represented. maybe a 'H' for hit or 'M' for miss.

  7. 

7.  To have a game over after a certain amount of tries

   User story: For the game over to happen after the tries.

   
8. To have an error message if the hits are insuffcient

 User Stories

1. If any characters are entered that aren't corrected to be redirected by the Game.
2. Any shots not on the board to have a message "Sorry that's not even in the ocean"
3. If not ready to play the game to have a "come back later message"
4.To make sure the board size has a minimum of 2 and maximum 10 which changes with the amount of shots.
5. To make sure the flow of the game is professional and slick for the user, especially the rule explanation and grid size choice.
6. To have clarity and a fluent rythm to the game



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




# Credits -

- Youtube tutorial- Battleships to understand logic. 
- https://www.youtube.com/watch?v=Gi0Fdyhk1_0&t=511s
- Stackoverflow was great resource.
- https://www.w3schools.com/ 
- https://www.geeksforgeeks.org/ understanding how to make battleships invisible 
- Tutors at code Institute
- Slack meet with the September intake.
- My mentor Rory





