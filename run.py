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

    # Creates the grid for the game.
    board = [["." for _ in range(5)] for _ in range(5)]
    def board_grid():
        for row in board:
            print(" ".join(row))
    
    # Creates 4 ships at random points on board.
    def random_ship():
        for _ in range(4):
            row, col = random.randint(0,4), random.randint(0,4)
            while board[row][col] == "@":
                row, col = random.randint(0,4), random.randint(0,4)
            board[row][col]= "@"
    random_ship()
    grid = board_grid()
    
    
        
    print("\nComputer board:\n")

    computer_board = [["." for _ in range(5)] for _ in range(5)]
    def computer_grid():
        for row in computer_board:
            print(" ".join(row))

    def random_ship_comp():
        for _ in range(4):
            row, col = random.randint(0,4), random.randint(0,4)
            while computer_board[row][col] == "@":
                row, col = random.randint(0,4), random.randint(0,4)
            computer_board[row][col]= "@"
    random_ship_comp()
    computer_grid()
    
    

    #Gets input for targeted row of opponent grid.
    def input_row():
        while True:
            try:
                targeted_row = int(input("Target row:\n"))
                if 1 <= targeted_row <=5:
                    return targeted_row
            except ValueError:
                print("Please write numbers!")
            else:
                print("Number out of range! Chose from 1 to 5.")
    
    #Gets input for targeted column of opponent grid.
    def input_col():
        while True:
            try:
                targeted_col = int(input("Target column:\n"))
                if 1 <= targeted_col <= 5:
                    return targeted_col
            except ValueError:
                print("Please write numbers!")
            else:
                print("Number out of range! Chose from 1 to 5.")
    

    
    def player_shot(player_row, player_col, computer_row, computer_col):
        player_row = input_row() -1
        player_col = input_col() -1
        
        if computer_board[player_row][player_col] == "@":
            computer_board[player_row][player_col] = "X"
            player_hits.append((player_row, player_col))  # Add the hit to player_hits
            return True
        else:
            computer_board[player_row][player_col] = "*"    
            return False
        
    def computer_shot():
        computer_row = random.randint(0,4)
        computer_col = random.randint(0,4)
        if board[computer_row][computer_col] == "@":
            board[computer_row][computer_col] = "X"
            computer_hits.append((computer_row, computer_col))
            return True
        else:
            board[player_row][player_col] = "*"
            return False

        
    
    while any("@" in row for row in board) and any("@" in row for row in computer_board):
        print(f"\n{player}'s board:\n")
        board_grid()
        print("\nComputer board:\n")
        computer_grid()
        
        print("\nPlayer's turn:")
        player_hit = player_shot()
        if player_hit:
            print("You hit a ship")
        else:
            print("You missed!")

        print("Computer turn:")
        computer_hit = computer_shot()
        if computer_hit:
            print("Computer hit your ship!")
        else:
            print("Computer missed!")

            
            

game()
