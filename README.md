# Battleships game

The Battleships is a Python terminal game that runs on Heroku using Code Institute mock terminal.
The players compete against the computer and try to shot down computers ships before computer does that.

![Game](./readme-images/game.png)

## User stories

### Player goals
 - As a player, I want to quickly gasp the rules and objective of the game.
 - I want a straightforward way to start the game.
 - I want to add my name in game and be able to clearly identify my board.
 - I want feedback on whather my shots hit the computer's ships or missed. 
 - I want the game to accurately determine and announce the winner when all ships on onse side are sunk.
 - I want to be able to view the final state of the game before seeing who won. 


## How to play

- At the beginning the playe is prompted to enter their name.
- After that he receives his board with randomly placed ships.
- The board of the computer is displayed under the players board.
- The hits are marked with "X" and misses with "*".
- Each round the player and computer target each others boards.
- The winner sinks opponent's battleships first. 


## Features

- Greeting of the player and short explanation of the game

    ![Greeting](./readme-images/welcome.png)

- Customisable player name

    ![Name](./readme-images/name.png)

- Computer as opponent
- Random ship placement
- Displaying both game boards each turn
- Win conditions
- Clear interface


## Testing 

- PEP8 Valdator  https://pep8ci.herokuapp.com/ - All clear, no errors found

    ![Pep](./readme-images/pep8.png)

- The game handles the wrong inputs for rows and columns by accepting only the numbers from 1 to 5.
If the player provides invalid input, they will be prompted to enter valid numeric values between 1 to 5.

    ![Error](./readme-images/error.png)

## Bugs

During the development I encountered a bug in computer_grid function. The board of the computer had visible ships all the time. 
I solved this bug by duplicating the board and printing only the hits and misses on the copy. 

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

To deploy this project on heroku: 
1. Clone this GitHub repository.
2. Go to Heroku https://dashboard.heroku.com/apps and add a new app.
3. For the buildbacks Chose the "Python" and "NodeJS".
4. Add the Github link for the repository.
5. Click on Deploy button. 




