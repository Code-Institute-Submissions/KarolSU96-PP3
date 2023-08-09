
import random

def game():
    """
    Main game function. Starts and runs the game
    """
    
    print("Welcome to the Battleship game")
    print("Board size: 5. Number of ships: 4")
    print("Top left corner is row: 0, col: 0\n")
    player = input("Please enter your name: ")

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
    
    #Computer board
    computer_board = [["." for _ in range(5)] for _ in range(5)]
    def computer_grid():
        copied_board = [["." for _ in range(5)] for _ in range(5)]
        for row in range(5):
            for col in range(5):
                if computer_board[row][col] == "X":
                    copied_board[row][col] = "X"
                if computer_board[row][col] == "*":
                    copied_board[row][col] = "*"
                elif computer_board[row][col]== ".":        
                    copied_board[row][col] = "."    
        for row in copied_board:
            print(" ".join(row))

    #Randomly places 4 ships on computer board
    def random_ship_comp():
        for _ in range(4):
            row, col = random.randint(0,4), random.randint(0,4)
            while computer_board[row][col] == "@":
                row, col = random.randint(0,4), random.randint(0,4)
            computer_board[row][col]= "@"
    random_ship_comp()        
    
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

   
    
    def player_shot():
        player_row = input_row() -1
        player_col = input_col() -1
        
        if computer_board[player_row][player_col] == "@":
            computer_board[player_row][player_col] = "X"
            return True
        else:
            computer_board[player_row][player_col] = "*"    
            return False
        
    def computer_shot():
        computer_row = random.randint(0,4)
        computer_col = random.randint(0,4)
        if board[computer_row][computer_col] == "@":
            board[computer_row][computer_col] = "X"
            return True
        if board[computer_row][computer_col] == "X":
            board[computer_row][computer_col] = "X"
            return True
        else:
            board[computer_row][computer_col] = "*"
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

        if not any("@" in row for row in board):
            print(f"\n{player}'s board:\n")
            board_grid()
            print("\nComputer board:\n")
            computer_grid()
            print("Computer won!")
            break
        elif not any("@" in row for row in computer_board):
            print(f"\n{player}'s board:\n")
            board_grid()
            print("\nComputer board:\n")
            computer_grid()
            print(f"{player} won!")
            break
        elif not any("@" in row for row in board) and not any ("@" in row for row in computer_board):
            print(f"\n{player}'s board:\n")
            board_grid()
            print("\nComputer board:\n")
            computer_grid()
            print("Tie!")
game()
