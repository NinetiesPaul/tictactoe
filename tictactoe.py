import matplotlib.pyplot as plt
import numpy as np
import random

def row_win(board,player):
    res = False
    for row in board:
        if np.all(row==player):
            res = True
    return res
        
def col_win(board,player):
    new_board=board.transpose()
    res = False
    for row in new_board:
        if np.all(row==player):
            res = True
    return res

def diag_win(board,player):
    diags=[]
    diags.append(board.diagonal())
    diags.append(np.fliplr(board).diagonal())
    res = False
    for row in diags:
        if np.all(row==player):
            res = True
    return res
    
def create_board():
    board=np.array([[0,0,0],[0,0,0],[0,0,0]])
    return board

def possibilities(board):
    free_pos=[]
    for k in range(len(board)):
        for j in range(len(board[k])):
            if board[k][j] == 0:
                free_pos.append((k,j))
    return free_pos

def random_place(board,player):
    pos = random.choice(possibilities(board))
    board[pos]=player

def evaluate(board, player):
    winner = 0

    if row_win(board,player) == True:
        winner = player
    elif col_win(board,player) == True:
        winner = player
    elif diag_win(board,player) == True:
        winner = player

    if np.all(board!=0) and winner == 0:
        winner = -1

    return winner
    
def start_game():
    board = create_board()

    winner = 0
    play = True

    while play:
        for player in [1,2]:
            random_place(board,player)
            winner = evaluate(board,player)

            if winner != 0:
                play=False
                break

    return winner
    
