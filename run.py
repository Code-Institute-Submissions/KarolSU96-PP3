# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

def game():
    """
    Starts the game, greets user and waits for the input
    """
    
    print("Welcome to the Battleship game")
    print("Board size: 5. Number of ships: 4")
    print("Top left corner is row: 0, col: 0\n")
    player = input("Please enter your name: ")

    
    print(f"{player} board:\n")

    # Creates board for the game
    board = [["." for _ in range(5)] for _ in range(5)]
    def board_grid():
        for row in board:
            print(" ".join(row))
    
    grid = board_grid()
game()

