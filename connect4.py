import numpy as np

# Static Variables
ROW_COUNT = 6
COLUMN_COUNT = 7

# Initilizes board
def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Check if the top spot in a column is open or not
def is_valid_location(board, col):
    return board[5][col] == 0

# Finds the next open row available
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

# Due to using numpy, this will format the board correctly
def print_board(board):
    # flips board over x-axis so it's correctly formatted
    print(np.flip(board, 0))


# Game Set Up
board = create_board()
print_board(board)
game_over = False
turn = 0

# Gameplay
while not game_over:
    # Player 1's turn
    if turn == 0:
        col = int(input("Player 1, make your selection (0-6): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

    # Player 2's turn
    else:
        col = int(input("Player 2, make your selection (0-6): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

    print_board(board)

    turn += 1
    # Alternate between P1 and P2's turns
    turn = turn % 2
