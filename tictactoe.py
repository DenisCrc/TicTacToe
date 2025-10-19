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

