import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board():
    return [[' ' for _ in range(7)] for _ in range(6)]

def print_board(board):
    for row in board:
        print('|' + '|'.join(row) + '|')
    print('-' * 15)
    print(' 1 2 3 4 5 6 7 ')

def is_valid_move(board, col):
    return board[0][col] == ' '

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(4):
        for r in range(6):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
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

    return False

def play_game():
    scores = {'X': 0, 'O': 0}
    while True:
        board = create_board()
        game_over = False
        turn = 0

        while not game_over:
            clear_screen()
            print_board(board)
            print(f"Scores - Joueur X: {scores['X']}, Joueur O: {scores['O']}")
            
            if turn % 2 == 0:
                piece = 'X'
            else:
                piece = 'O'
            
            col = int(input(f"Joueur {piece}, choisissez une colonne (1-7): ")) - 1

            if 0 <= col <= 6:
                if is_valid_move(board, col):
                    row = 5
                    while row >= 0:
                        if board[row][col] == ' ':
                            drop_piece(board, row, col, piece)
                            break
                        row -= 1

                    if winning_move(board, piece):
                        clear_screen()
                        print_board(board)
                        print(f"Le joueur {piece} gagne!")
                        scores[piece] += 1
                        game_over = True
                else:
                    print("Colonne pleine, choisissez une autre.")
                    continue
            else:
                print("Entrée invalide. Choisissez une colonne entre 1 et 7.")
                continue

            if all(board[0][i] != ' ' for i in range(7)):
                clear_screen()
                print_board(board)
                print("Match nul!")
                game_over = True

            turn += 1

        play_again = input("Voulez-vous jouer à nouveau? (o/n): ").lower()
        if play_again != 'o':
            break

    print("Merci d'avoir joué!")
    print(f"Scores finaux - Joueur X: {scores['X']}, Joueur O: {scores['O']}")

if __name__ == "__main__":
    play_game()
