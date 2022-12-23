#create a board
board=["-","-","-",
       "-","-","-",
       "-","-","-",]
current_player="X"
winner=None
gameRunning=True
def print_board(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("----------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("----------")
    print(board[6]+" | "+board[7]+" | "+board[8])
#make game
def user_input(board):
    inp=int(input("enter a number on the board: "))
    if inp>0 and inp<10 and board[inp-1]=="-":
        board[inp-1]=current_player
    else:
        print("Player already in that spot or you selected an unkown position")


#declare winners
def check_horizontal(board):
    global winner 
    if board[0]==board[1]==board[2] and board[1]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner=board[4]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner=board[7]
        return True
def check_row(board):
    global winner
    if board[0]==board[3]==board[6] and board[3]!="-":
        winner=board[3]
        return True
    elif board[1]==board[4]==board[7] and board[4]!="-":
        winner=board[4]
        return True
    elif board[2]==board[5]==board[8] and board[5]!="-":
        winner=board[5]
        return True
def check_cross(board):
    global winner
    if board[0]==board[4]==board[8] and board[4]!="-":
        winner=board[4]
        return True
    elif board[2]==board[4]==board[6] and board[4]!="-":
        winner=board[4]
        return True

def checkWin():
    global gameRunning
    if check_horizontal(board) or check_cross(board) or check_row(board):
        print("Winner is {}!".format(winner))
        gameRunning=False


#declare if its a tie
def checkTie(board):
    global gameRunning
    if "-" not in board:
        print_board(board)
        print("It's a tie!")
        gameRunning=False
#switch player:
def switch_player():
    global current_player
    if current_player=="X":
        current_player="O"
    else :
        current_player="X"

#run the game
while gameRunning:
    print_board(board)
    user_input(board)
    checkWin()
    checkTie(board)
    switch_player()
