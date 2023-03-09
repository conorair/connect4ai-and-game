import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT-3):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for r in range(ROW_COUNT-3):
        for c in range(3, COLUMN_COUNT):
            if board[r][c] == piece and board[r+1][c-1] == piece and board[r+2][c-2] == piece and board[r+3][c-3] == piece:
                return True


board = create_board()
game_over = False
turn = 0

while not game_over:
    # Ask for Player 1 input
    if turn == 0:
        col = int(input("Player 1 make your selection (0-6):"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print("PLAYER 1 WINS!!!")
                game_over = True

    # Ask for Player 2 input
    else:
        col = int(input("Player 2 make your selection (0-6):"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                print("PLAYER 2 WINS!!!")
                game_over = True

    print_board(board)
    turn += 1
    turn = turn % 2

# Set up the game
game_over = False
turn = 0

# Game loop
while not game_over:
    # Human player's turn
    if turn == 0:
        # Get column choice from human player
        col = int(input("Player 1 (Yellow): Choose a column (0-6): "))

        # Place yellow piece in chosen column
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, YELLOW)

            # Check if human player wins
            if winning_move(board, YELLOW):
                print("Congratulations, you win!")
                game_over = True

        else:
            print("Invalid move. Please try again.")
            continue

    # Computer player's turn
    else:
        # Get column choice from computer player using minimax algorithm
        col, minimax_score = minimax(board, 5, -math.inf, math.inf, True, RED)

        # Place red piece in chosen column
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, RED)

            # Check if computer player wins
            if winning_move(board, RED):
                print("Sorry, the computer wins!")
                game_over = True

        else:
            print("Invalid move. Please try again.")
            continue
