#----- Global Variables -----


#Game Board
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]
#if game still game still going
game_still_going = True

#Who Won or Win
winner = None

#Whos turn is it
current_player = "X"

def display_board():
    print(board[0]+ ' | '+board[1]+ " | "+ board[2])
    print(board[3]+ ' | '+board[4]+ " | "+ board[5])
    print(board[6]+ ' | '+board[7]+ " | "+ board[8])

def play_game():
    #display the board first
    display_board()

    #While Game still going
    while game_still_going:
        #handle a single turn of a player
        handle_turn(current_player)
        check_if_game_over()

        #go to other player
        flip_player()

    #The Game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


def handle_turn(player):
    print(player+ "'s turn.")
    position= input ("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
        position=int(position)-1
        if board[position] == '-':
            valid = True
        else:
            print("You cant go there go again")


    board[position]=player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner
    #check rows
    row_winner=checkRows()
    #check columns
    col_winner=checkColumns()
    #check diagonals
    diag_winner=checkDiagonals()
    if row_winner:
        winner=row_winner
        #Winner
    elif col_winner:
        winner=col_winner

        #winner
    elif diag_winner:
        winner=diag_winner
    else:
        #there is no Winner
        winner = None

    return
def checkRows():
    global game_still_going
    #check if row got same values and is not empty
    row_1=board[0]==board[1]==board[2] != "-"
    row_2=board[3]==board[4]==board[5] != "-"
    row_3=board[6]==board[7]==board[8] != "-"
    #set game to false
    if row_1 or row_2 or row_3:
        game_still_going = False
    #return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def checkColumns():
    global game_still_going
    #check if col got same values and is not empty
    col_1=board[0]==board[3]==board[6] !="-"
    col_2=board[1]==board[4]==board[7] !="-"
    col_3=board[2]==board[5]==board[8] !="-"
    #set game to false
    if col_1 or col_2 or col_3:
        game_still_going = False

    #return who won
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[5]

    return

def checkDiagonals():
    global game_still_going
    #check if diag got same values and is not empty
    diag_1=board[0]==board[4]==board[8] !="-"
    diag_2=board[6]==board[4]==board[2] !="-"
    #set game to false
    if diag_1 or diag_2:
        game_still_going = False

    #return who won
    if diag_1:
        return board[0]
    elif diag_2:
        return board[6]

    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return

    return

def flip_player():
    #if currrent play was x change to o and if current is o change to x
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player == "O":
        current_player="X"

    return


play_game()



#Tic Tac Toe

#board
#display board
#play game

#checkWin
    #check rows
    #check columns
    #check diagonals
#checkTie
#flip from play
