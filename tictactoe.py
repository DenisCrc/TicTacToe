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

def aimove(board,curentp):
    empty=[]
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty.append((i,j))
    if empty:
        r,c= random.choice(empty)
        if curentp==1:
            board[r][c]='X'
        else:
            board[r][c]='O'

def playgame():
    board=create_board()
    print("Do you want to be player 1(X) or player 2(O)?")
    p=int(input())
    while True:
        curentp=1
        if p==curentp==1:
            player_move(board,curentp)
            print_board(board)
            curentp=2
        else:
            print("AI is thinking...")
            aimove(board,curentp)
            print_board(board)
            curentp=2
        w=win_check(board)
        if w!=0:
            print(w," WON")
            break
        d=draw_check(board)
        if d==1:
            print("DRAW")
        if p==curentp==2:
            player_move(board,curentp)
            print_board(board)
            curentp=1
        else:
            print("AI is thinking...")
            aimove(board,curentp)
            print_board(board)
            curentp=1
        w=win_check(board)
        if w!=0:
            print(w," WON")
            break
        d=draw_check(board)
        if d==1:
            print("DRAW")

playgame()
