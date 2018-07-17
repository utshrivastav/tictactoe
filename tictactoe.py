#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:17:46 2017

@author: utkarsh
"""

def tictactoe(theBoard):
    print(theBoard['topL']+' | '+theBoard['topM']+' | '+theBoard['topR'])
    print('.........')
    print(theBoard['midL']+' | '+theBoard['midM']+' | '+theBoard['midR'])
    print('.........')
    print(theBoard['lowL']+' | '+theBoard['lowM']+' | '+theBoard['lowR'])
    
theBoard = {'topL':'','topM':'','topR':'',
            'midL':'', 'midM':'', 'midR':'',
            'lowL':'','lowM':'','lowR':''}
choice = input('Player1 ! What do want "x" or "o"?' )
player1 = choice
if player1 == 'x':
    player2 ='o'
elif player1 == 'o':
    player2 = 'x'
flag = False
for i in range(9):
    move = input('Enter the place you want to mark :')
    if i%2 == 0:
        print('Player1')
        theBoard[move] = player1
    else:
        print('player2')
        theBoard[move] = player2
    tictactoe(theBoard)
    if (theBoard['topL'] == 'x' and theBoard['topM'] == 'x' and theBoard['topR'] == 'x') or (theBoard['topL'] == 'o' and theBoard['topM'] == 'o' and theBoard['topR'] == 'o'):
        if i == 8:
            flag = True
        break
    elif (theBoard['midL'] == 'x' and theBoard['midM'] == 'x' and theBoard['midR'] == 'x') or (theBoard['midL'] == 'o' and theBoard['midM'] == 'o' and theBoard['midR'] == 'o'):
        if i == 8:
            flag = True
        break
    elif (theBoard['lowL'] == 'x' and theBoard['lowM'] == 'x' and theBoard['lowR'] == 'x') or (theBoard['lowL'] == 'o' and theBoard['lowM'] == 'o' and theBoard['lowR'] == 'o'):
        if i == 8:
            flag = True
        break
    elif (theBoard['topL'] == 'x' and theBoard['midL'] == 'x' and theBoard['lowL'] == 'x') or (theBoard['topM'] == 'x' and theBoard['midM'] == 'x' and theBoard['lowM'] == 'x') or (theBoard['topR'] == 'x' and theBoard['midR'] == 'x' and theBoard['lowR'] == 'x'):
        if i == 8:
            flag = True
        break
    elif (theBoard['topL'] == 'o' and theBoard['midL'] == 'o' and theBoard['lowL'] == 'o') or (theBoard['topM'] == 'o' and theBoard['midM'] == 'o' and theBoard['lowM'] == 'o') or (theBoard['topR'] == 'o' and theBoard['midR'] == 'o' and theBoard['lowR'] == 'o'):
        if i == 8:
            flag = True
        break
    elif (theBoard['topL'] == 'x' and theBoard['midM'] == 'x' and theBoard['lowR'] == 'x') or (theBoard['topL'] == 'o' and theBoard['midM'] == 'o' and theBoard['lowR'] == 'o'):
        if i == 8:
            flag = True
        break
    elif (theBoard['topR'] == 'x' and theBoard['midM'] == 'x' and theBoard['lowL'] == 'x') or (theBoard['topR'] == 'o' and theBoard['midM'] == 'o' and theBoard['lowL'] == 'o'):
        if i == 8:
            flag = True
        break
if i<8:
    print('player'+str((i%2)+1)+' won')
else:
    if flag :
        print('player'+str((i%2)+1)+' won')
    else:
        print('Game Draw')