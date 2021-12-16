import string
import os
os.chdir(os.path.dirname(__file__))

numbers = []
boards = [[]]

def readInFile():
    firstLine = True
    boardCounter = 0
    tempBoard = []
    for line in open('input.txt'):
        if firstLine:
            numbers.extend(line.strip().split(','))
            firstLine = False
            
            
        else:
            if len(line.strip().split()) == 5:
                boards[boardCounter].append(line.strip().split())
                #print('bingo: ' + str(boards[boardCounter]))
                #print('board size: ' + str(len(tempBoard)))
                
                if(len(boards[boardCounter]) == 5):
                    #print('bingo2: ' + str(boards))
                    boards.append([])
                    boardCounter += 1
            
    boards.pop()
        
def printBoards(boardArr):
    for board in boardArr:
        printBoard(board)

def printBoard(board):
        for row in board:
            for elem in row:
                print(elem, end='\t')
            print()
        print()



def doTheThing():
    winningNumbers = []
    checkForBingoCalls = 0
    for num in numbers:
        #print('checking num: ' + str(num))
        for boardCount, board in enumerate(boards):
            #print('checking board: ' + str(board))
            for rowCount, row in enumerate(board):
                for elemCount, elem in enumerate(row):
                    if elem == num:
                        print('setting val true!')
                        boards[boardCount][rowCount][elemCount] = True
                        print('board: ' + str(boards[boardCount]))
                        
                        rowCol, rowColNum = checkForBingo(board)
                        checkForBingoCalls += 1
                        if rowCol == 'r' or rowCol == 'c':
                            print('elem: ' + str(num))
                            #print('winning board: \n' + str(board))
                            printBoard(board)
                            print('enums boardCount, rowCount, elemCount: ' + str(boardCount) + ', ' + str(rowCount) + ', ' + str(elemCount))
                            print('num bingo checks: ' + str(checkForBingoCalls))
                            return getBoardSum(board) * int(num)
                        
            
def getBoardSum(board):
    boardSum = 0
    for row in board:
        for elem in row:
            if str(elem).isdigit():
                boardSum += int(elem)
    print('board sum: ' + str(boardSum))
    return boardSum

def checkForBingo(board):
    cntRow = 0
    cntCol = 0
    for i in range(0, 5):
        for j in range(0,5):
            if board[i][j] == True:
                cntRow += 1
                if cntRow == 5:
                    return 'r', i;
            if board[j][i] == True:
                cntCol += 1
                if cntCol == 5:
                    return 'c', i;
        cntRow = 0
        cntCol = 0
    return 'n', -1;

readInFile()
#printBoards(boards)

winningNumber = doTheThing()
print('winningNumbers: ' + str(winningNumber))