import numpy as np

# Initilizes board
def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece():
    pass

# Check if the top spot in a column is open or not
def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row():
    pass

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
