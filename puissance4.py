def create_board():
    return [[' ' for _ in range(7)] for _ in range(6)]

def print_board(board):
    for row in board:
        print('|' + '|'.join(row) + '|')
    print('+---' * 7 + '+')
    print(' 0   1   2   3   4   5   6')

def is_valid_location(board, col):
    return board[0][col] == ' '

def get_next_open_row(board, col):
    for r in range(5, -1, -1):
        if board[r][col] == ' ':
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(4):
        for r in range(6):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(7):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(4):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(4):
        for r in range(3, 6):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def play_game():
    board = create_board()
    game_over = False
    turn = 0

    print_board(board)

    while not game_over:
        if turn == 0:
            col = int(input("Player 1 Make your Selection (0-6):"))
            piece = 'X'
        else:
            col = int(input("Player 2 Make your Selection (0-6):"))
            piece = 'O'

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, piece)

            if winning_move(board, piece):
                print_board(board)
                print(f"Player {turn + 1} wins!")
                game_over = True

            turn += 1
            turn = turn % 2

            print_board(board)
        else:
            print("Invalid move, try again")

if __name__ == "__main__":
    play_game()
