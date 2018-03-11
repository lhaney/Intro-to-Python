"""

This program simulates the game of tic tac toe.
"""

def get_valid_index(prompt):
    while True:
        try:
            index = int(input(prompt))
            if index >= 0 and index <= 2:
                return index
            print "Must be 0 - 2 inclusive!"
        except ValueError:
            print "Must be an integer!"


def game_is_over(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] \
            and board[i][0] != " ":
            print board[i][0] + " wins!"
            return True
        
        if board[0][i] == board[1][i] == board[2][i] \
            and board[0][i] != " ":
            print board[0][i] + " wins!"
            return True
        
    if board[0][0] == board[1][1] == board[2][2] \
        and board[0][0] != " ":
        print board[0][0] + " wins!"
        return True
    
    if board[2][0] == board[1][1] == board[0][2] \
        and board[2][0] != " ":
        print board[2][0] + " wins!"
        return True
    
    if " " not in board[0] and " " not in board[1] \
        and " " not in board[2]:
        print "Tie game!"
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

turn = "x"

for i in range(9):
    print_board(board)
    print "It's " + turn + "'s turn."
    row = get_valid_index("Row: ")
    col = get_valid_index("Col: ")
    if board[row][col]==' ':
        board[row][col]=turn
    else:
        print 'that space is taken. try again.'
        continue
    if game_is_over(board):
        break
    else:
        if i%2==0:
            turn='o'
        else:
            turn='x'
        
    
