#importing required modules
import numpy as n
import random               
from time import sleep                

# code for 9 x 9 tic tac toe board
def board_design():
    return(n.array([[0,0,0,],
                   [0,0,0,],
                   [0,0,0,]]))

# the following function calculates the currently empty spots on the board
def possible_spots(board):
    l=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                l.append((i,j))
    return l

# the following function selects one random place from the currently empty spots
def rand_spot(board, player):
    chosen_spot = possible_spots(board)
    present_position = random.choice(chosen_spot)
    board[present_position] = player
    return(board)

# cheking whether the player won horizontally
def horizontally(board, player):
    for i in range(len(board)):
        win = True
    for j in range(len(board)):
        if board[i,j]!= player:
            win = False
            continue
    if win == True:
        return(win)
    return(win)

# checking whether player won vertically
def vertically(board, player):
    for i in range(len(board)):
        win = True
    for j in range(len(board)):
        if board[j,i]!= player:
            win = False
            continue
    if win == True:
        return(win)
    return(win)

# checking whether player won vertically
def diagonally( board, player):
    win= True
    j=0
    for i in range(len(board)):
        if board[i,i]!= player:
            win= False
    if win:
        return win
    win = True
    if win:
        for i in range(len(board)):
            j= len(board) - i -1
            if board[i,j]!=player:
                win = False
    return win

# checking for a tie
def check(board):
    winner = 0
    for player in [1, 2]:
        if ( horizontally(board, player) or vertically(board, player) or diagonally(board, player)):
            winner = player
    if n.all(board!=0) and winner ==0:
        winner =-1
    return winner

# main
def start():
    board = board_design()
    winner = 0
    c = 1
    print("********** TIC TAC TOE **********")
    print("\n\nX is represented by 1\n")
    print("O is represented by 2\n")
    print(board)
    sleep(2)
    while winner ==0 :
        for player in [1, 2]:
            board = rand_spot(board, player)
            print("After",str(c),"move : ")
            print(board)
            sleep(2)
            c+=1
            winner= check(board)
            if winner!=0:
                break
    return winner

print("WINNER : " + str(start()))
       