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
    return board[ROW_COUNT - 1][col] == 0

# Finds the next open row available
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

# Due to using numpy, this will format the board correctly
def print_board(board):
    # flips board over x-axis so it's correctly formatted
    print(np.flip(board, 0))

# Checks for wins
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positive sloped diagonals
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negative sloped diagonals
    for r in range(ROW_COUNT-3):
        # diagonal negative sloped wins can't start til the 4th row
        for c in range(3, COLUMN_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

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

            if winning_move(board, 1):
                print("Player 1 Wins!")
                game_over = True
                break;

    # Player 2's turn
    else:
        col = int(input("Player 2, make your selection (0-6): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                print("Player 2 Wins!")
                game_over = True
                break;

    print_board(board)

    turn += 1
    # Alternate between P1 and P2's turns
    turn = turn % 2
