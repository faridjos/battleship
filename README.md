# The battleship game
The battleship game is a computer version of the classic paper and pen game. It is a game for two players. Each player has a board with ships and tries to guess the position of the ships of the other player to sink them. In the computer version the user plays against the computer. 

# Table of contents

- [UX](#ux)
    - [Website owner business goals](#website-owner-business-goals)
    - [User goals](#user-goals)
- [Structure of the project](#structure-of-the-project)
- [Features](#features)
- [Technologies](#technologies)
- [Data model](#data_model)
- [Testing](#testing)
    - [Functionality testing](#functionality-testing)
    - [Code validation](#code-validation)
    - [Unfixed bugs](#unfixed-bugs) 
- [Deployment](#deployment)
- [Credits](#credits)

# UX

## Website owner business goals
The main objective is to provide a simple and well-known game for the users.

## User goals
- The user wants to play a classic game on the computer.
- He wants to store the scores so he can see how well he is doing.

[Back to contents](#table-of-contents)

# Structure of the project
To facilitate the development of the project the algorithm of the game was visualized in a flow diagram using the website Lucidchart.

<img src="assets/images/battleship.png">

[Back to contents](#table-of-contents)

# Features
- The programme starts by printing a welcome message. Random positions are chosen for the ships on both boards. The player guesses a position to try to hit a ship of the computer. The position is validated. The computer also chooses a (random) position to try to sink the player's ship. The program checks if the guesses result in hits or misses and displays the score. The boards are printed. The game continues until all the ships of one side are sunk or the player wants to end the game. The score of the five latest games is shown. Finally he can either start a new game or stop playing.
- In the future one can allow for ships of different sizes and the user can decide the positions of his ships.

<img src="assets/images/start_of_game.PNG">

[Back to contents](#table-of-contents)

# Technologies used
- Python for the code
- Github for cloud-based storage of project and deployment
- GitPod for development
- Git for version control

[Back to contents](#table-of-contents)

# Data model

We decided to have an object oriented approach. Four classes were defined: The ship class containing grid variables such as grid size and lists that store the positions of the ships and the guesses of the enemy.
 - The ship class has methods such as randomly assigning positions to the ships.
 - The human class has just one instance variable which is the name and one method to enter and validate that name. 
 - The two remaining classes ComputerPlayer and HumanPlayer are similar. They both contain the ship class and have methods to guess coordinates of the enemy's ship and print the board. Since the methods differ somewhat between the user and the computer I decided to use two classes.
 
[Back to contents](#table-of-contents)

# Testing

## Functionality testing
I tested if the application works as intended both on gitpod and heroku. I tested that the coordinates entered or generated are not repeated; that they are integers between 0 and gridsize - 1; and that the input name is not an empty string.

## Code validation
The code passed through the PEP8 linter without errors.

## Unfixed bugs
There is no unfixed bugs

[Back to contents](#table-of-contents)

# Deployment
The application was deployed using the Code Institute mock terminal in Heroku. The steps for deployment are as follow.
- Create an app in Heroku.
- Set environment variables.
- Add the backpacks for Python and Node.js in the correct order.
- Connect to the github repository.
- The application is ready to be deployed

[Back to contents](#table-of-contents)

# Credit
- My inspiration came from the love sandwiches walkthrough project and from the video about the battleship game example application. The code handling gspread and authorization towards google drive was directly taken from the love sandwiches application. A few lines of code, from the same source, which writes to and reads from the google sheet, was adapted to our application.
- The flowchart was made in the website Lucidchart.

[Back to contents](#table-of-contents)
