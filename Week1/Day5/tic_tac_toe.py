# Tic Tac Toe - Week 1, Day 5 mini-project


# Step 1: Representing the game board
def create_board():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]


# Step 2: Displaying the game board
def display_board(board):
    print("   1   2   3")
    for i in range(3):
        row = board[i]
        print(f"{i + 1}  {row[0]} | {row[1]} | {row[2]}")
        if i < 2:
            print("  ---+---+---")


# Step 3: Getting the player's move
def player_input(board, player):
    while True:
        row = input(f"Player {player}, choose a row (1-3): ")
        col = input(f"Player {player}, choose a column (1-3): ")

        if row not in ["1", "2", "3"] or col not in ["1", "2", "3"]:
            print("Please enter 1, 2 or 3. Try again.")
            continue

        row = int(row) - 1
        col = int(col) - 1

        if board[row][col] != " ":
            print("That square is already taken. Try again.")
            continue

        return row, col


# Step 4: Checking for a winner
def check_win(board, player):
    # Check the 3 rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    # Check the 3 columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # Check the 2 diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


# Step 5: Checking for a tie
def check_tie(board):
    for row in board:
        if " " in row:
            return False

    if check_win(board, "X") or check_win(board, "O"):
        return False

    return True


# Step 6: The main game loop
def play():
    board = create_board()
    current_player = "X"

    print("Welcome to Tic Tac Toe!")

    while True:
        display_board(board)

        row, col = player_input(board, current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break

        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


play()
