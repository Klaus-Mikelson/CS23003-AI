# Create the board
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

# Player symbols
current_player = "X"

# Game control variables
game_running = True
winner = None

# Main game loop
while game_running:

    # Display the board
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

    # Ask for player input
    move = input("Player " + current_player + ", choose a position (1-9): ")

    # Validate input
    if move not in ["1","2","3","4","5","6","7","8","9"]:
        print("Invalid input. Choose a number from 1 to 9.")
        continue

    position = int(move) - 1

    if board[position] != " ":
        print("That spot is already taken.")
        continue

    # Place the move
    board[position] = current_player

    # Check for win
    if (
        (board[0] == board[1] == board[2] != " ") or
        (board[3] == board[4] == board[5] != " ") or
        (board[6] == board[7] == board[8] != " ") or
        (board[0] == board[3] == board[6] != " ") or
        (board[1] == board[4] == board[7] != " ") or
        (board[2] == board[5] == board[8] != " ") or
        (board[0] == board[4] == board[8] != " ") or
        (board[2] == board[4] == board[6] != " ")
    ):
        winner = current_player
        game_running = False

    # Check for tie
    elif " " not in board:
        game_running = False

    # Switch player
    else:
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# Game result
print()
print(board[0] + " | " + board[1] + " | " + board[2])
print("--+---+--")
print(board[3] + " | " + board[4] + " | " + board[5])
print("--+---+--")
print(board[6] + " | " + board[7] + " | " + board[8])
print()

if winner:
    print("Player " + winner + " wins!")
else:
    print("It's a tie!")