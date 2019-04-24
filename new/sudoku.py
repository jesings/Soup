#! /usr/bin/python3
import sys
#9x9 sudoku board
Cliques=[[0,1,2,3,4,5,6,7,8], [9,10,11,12,13,14,15,16,17], [18,19,20,21,22,23,24,25,26], [27,28,29,30,31,32,33,34,35], [36,37,38,39,40,41,42,43,44], [45,46,47,48,49,50,51,52,53], [54,55,56,57,58,59,60,61,62], [63,64,65,66,67,68,69,70,71], [72,73,74,75,76,77,78,79,80], [0,9,18,27,36,45,54,63,72], [1,10,19,28,37,46,55,64,73], [2,11,20,29,38,47,56,65,74], [3,12,21,30,39,48,57,66,75], [4,13,22,31,40,49,58,67,76], [5,14,23,32,41,50,59,68,77], [6,15,24,33,42,51,60,69,78], [7,16,25,34,43,52,61,70,79], [8,17,26,35,44,53,62,71,80], [0,1,2,9,10,11,18,19,20], [3,4,5,12,13,14,21,22,23], [6,7,8,15,16,17,24,25,26], [27,28,29,36,37,38,45,46,47], [30,31,32,39,40,41,48,49,50], [33,34,35,42,43,44,51,52,53], [54,55,56,63,64,65,72,73,74], [57,58,59,66,67,68,75,76,77], [60,61,62,69,70,71,78,79,80] ]
def sudokuprint(board):
    strresult = ""
    for n in range(81):
        strresult += str(board[n])+("," if n%9!=8 else "\n")
    return strresult
cliquemap = {}
for n in range(81):
    cliquemap[n] = []
    for clique in Cliques:
        if n in clique:
            cliquemap[n].append(clique)
def possible(board,index):
    dumbhash = [0]*10
    for clique in cliquemap[index]:
        for member in clique:
            if board[member]!=0:
                dumbhash[board[member]]+=1
    for n in range(1,10):
        if dumbhash[n]==0:
            yield n
def heuristic1(board):
    changes = 0
    for n in range(81):
        if board[n]: continue
        poss = list(possible(board,n))
        if len(poss) ==1:
            board[n] = poss[0]
            changes +=1
    return changes
def heuristic1w(board):
    while heuristic1(board):pass
def solveboard(board,index):
    global backtracks
    if index==0:
        backtracks = 0
        heuristic1w(board)
    if index==81:
        print(backtracks)
        print(board)
        return sudokuprint(board)
    board = board[:]
    heuristic1w(board)
    if board[index]!=0:
        return solveboard(board,index+1)
    genlen = 0
    for n in possible(board,index):
        board[index] = n
        solutionp = solveboard(board,index+1)
        if solutionp:
            return solutionp
        genlen+=1
    if genlen!=1:
        backtracks+=1
    return False
inputfile = open(sys.argv[1],'r')
boards = {}
while True:
    thisline = inputfile.readline()
    if not thisline:
        break
    if thisline=="\n":
        continue
    board = ""
    for n in range(9):
        board+=inputfile.readline().strip()+','
    board = board[:-1].replace("_","0")
    board = board.split(',')
    board = [int(x) for x in board]
    boards[thisline.strip()] = board
inputfile.close()
outputfile = open(sys.argv[2],'w')
outputfile.write(solveboard(boards[sys.argv[3]],0))
outputfile.close()
