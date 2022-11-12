board={1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

def showBoard():
    print(board[1],"|",board[2],"|",board[3])
    print("--+---+--")
    print(board[4],"|",board[5],"|",board[6])
    print("--+---+--")
    print(board[7],"|",board[8],"|",board[9])

showBoard()


def EndGame():
    for i in board.keys():
        if(board[i]==" "):
            return False
    return True

def CheckWhoWins(player):
    if board[1] == board[2] and board[1] == board[3] and board[1] == player :
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == player :
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == player :
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == player :
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == player :
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == player :
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == player :
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] == player :
        return True
    else:
        return False


def validPosition(position):
    for i in board.keys():
        if(i==position):
            return True
    return False


def insert(player,position):
    if(not validPosition(position)):
        print("Invalid Position.")
        position=int(input("Enter your position: "))
        insert(player ,position )
    if(board[position]==" "):
        board[position]=player
        showBoard()
    else:
        print("position used try again")

        position=int(input("Enter your position from 1-9: "))
        insert(player ,position )
        
    if CheckWhoWins(player) == True:
        print(player , "is the winner")
        quit()
        
    if(EndGame()==True):
        print("Game over")
        quit()

def playerO():
    position=int(input("enter the position for the O marker: "))
    insert("o",position)


def playerx():
    position=int(input("enter the position for the x marker: "))
    insert("x",position)
while True:

    playerO()



    playerx()


