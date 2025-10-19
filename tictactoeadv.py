import random
def create_board():
    """Create and return a 3x3 Tic-Tac-Toe board."""
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    return board

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---+---+---")
        print()

def player_move(board, player):
    print("Please enter your move (row and column, 0-2):")
    row = int(input())
    column = int(input())
    if row>2 or column>2:
        print("Please enter a valid move")
        row = int(input())
        column = int(input())
    else:
        if board[row][column] != ' ':
            print("Please enter a valid move")
            row = int(input())
            column = int(input())
    
    if player == 1:
        board[row][column] = 'X'
    else:
        board[row][column] = 'O'

def win_check(board):
    for i in board:
        if i[0]==i[1]==i[2]!=' ':
            return i[0]
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != ' ':
            return board[0][c]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return 0

def draw_check(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                return 0
    return 1

def aimove(board, curentp):
    ai_symbol = 'O' if curentp == 2 else 'X'
    player_symbol = 'X' if ai_symbol == 'O' else 'O'

    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

    for r, c in empty:
        board[r][c] = ai_symbol
        if win_check(board) == ai_symbol:
            print(f"AI places {ai_symbol} at ({r}, {c})")
            return
        board[r][c] = ' ' 

    for r, c in empty:
        board[r][c] = player_symbol
        if win_check(board) == player_symbol:
            board[r][c] = ai_symbol
            print(f"AI places {ai_symbol} at ({r}, {c})")
            return
        board[r][c] = ' ' 

    if board[1][1] == ' ':
        board[1][1] = ai_symbol
        print(f"AI places {ai_symbol}")
        return

    for r, c in [(0,0), (0,2), (2,0), (2,2)]:
        if board[r][c] == ' ':
            board[r][c] = ai_symbol
            print(f"AI places {ai_symbol}")
            return

    if empty:
        r, c = random.choice(empty)
        board[r][c] = ai_symbol
        print(f"AI places {ai_symbol}")

def playgame():
    board = create_board()
    print("Do you want to be player 1 (X) or player 2 (O)?")
    p = int(input("Enter 1 or 2: "))

    currentp = 1 

    while True:
        print_board(board)

        if (currentp == p):
            print(f"Your turn ({'X' if currentp == 1 else 'O'}):")
            player_move(board, currentp)
        else: 
            print("AI is thinking...")
            aimove(board, currentp)
        w = win_check(board)
        if w != 0:
            print_board(board)
            if (w == 'X' and p == 1) or (w == 'O' and p == 2):
                print("You win!")
            else:
                print("AI wins!")
            break
        if draw_check(board) == 1:
            print_board(board)
            print("It's a draw! 🤝")
            break
        currentp = 2 if currentp == 1 else 1
playgame()
