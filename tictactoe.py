print("Do you want to be player 1(x) or player 2(O)?")
p=int(input())
def create_board():
    """Create and return a 3x3 Tic-Tac-Toe board."""
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    return board
board=create_board()

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

    if row>2 | column>2:
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

player_move(board,p)
print_board(board)
