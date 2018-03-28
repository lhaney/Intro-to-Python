"""
This program simulates the game of tic tac toe.
"""

def get_valid_index(prompt): #this board is defined for actions when index is valid
    while True:
        try:
            index = int(input(prompt))
            if index >= 0 and index <= 2:#this would limit the board size to be a 3x3 grid
                return index
            print "Must be 0 - 2 inclusive!"
        except ValueError: 
            print "Must be an integer!"


def game_is_over(board):#this board is defined for actions when one player wins or no one wins
    for i in range(3):# 3 is the side length of the board
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ": # this checks the vertical ones |
            print board[i][0] + " wins!" #this is the message u want the winner to view after they win
            return True
        
        if board[0][i] == board[1][i] == board[2][i] \ # this checks the horizontal ones __
            and board[0][i] != " ":
            print board[0][i] + " wins!" #this is the message u want the winner to view after they win
            return True
        
    if board[0][0] == board[1][1] == board[2][2] \ #diagnal  \
        and board[0][0] != " ":
        print board[0][0] + " wins!" #this is the message u want the winner to view after they win
        return True
    
    if board[2][0] == board[1][1] == board[0][2] \#diagnal 2 /
        and board[2][0] != " ":
        print board[2][0] + " wins!" #this is the message u want the winner to view after they win
        return True
    
    if " " not in board[0] and " " not in board[1] \
        and " " not in board[2]:
        print "Tie game!" # this is the message u want the players to see if they result in a tie
        return True
    
    return False
    
def print_board(board):
    print board[0]
    print board[1]
    print board[2]
    print ""

board = []
for i in range(3):
    board.append([' ']*3)

turn = "x" # x is the side u would like to go first in a new game

for i in range(9):
    print_board(board)
    print "It's " + turn + "'s turn." # this is the message u want the player to see to figure out whose turn is it. 
    row = get_valid_index("Row: ") # this is the y coordinate of the box
    col = get_valid_index("Col: ") #this is the x coordinate of the box
    if board[row][col]==' ':
        board[row][col]=turn
    else:
        print 'that space is taken. try again.' # this is the message you want the player to view if their choice of square is already token
        continue
    if game_is_over(board):
        break
    else:
        if i%2==0:
            turn='o'# o is the opponent side of x
        else:
            turn='x' # x is the opponent side of o
