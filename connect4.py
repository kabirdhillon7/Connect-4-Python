import numpy as np

# Static Variables
ROW_COUNT = 6
COLUMN_COUNT = 7

# Initilizes board
def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece():
    pass

# Check if the top spot in a column is open or not
def is_valid_location(board, col):
    return board[ROW_COUNT][col] == 0

# Finds the next open row available
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

board = create_board()
print(board)

game_over = False
turn = 0

while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        col = int(input("Player 1, make your selection (0-6): "))
    # Ask for Player 2 Input
    else:
        col = int(input("Player 2, make your selection (0-6): "))

    turn += 1
    # Alternate between P1 and P2's turns
    turn = turn % 2
