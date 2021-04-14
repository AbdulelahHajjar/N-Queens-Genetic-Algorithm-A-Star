from random import randint
import enum
import time
import copy
import sys

calls = 0


class VariableOrderings(enum.Enum):
    mcv = 0
    mrv = 1


class EarlyCheck(enum.Enum):
    arc = 0
    fc = 1


def numLegalValues(board, col):
    count = 0
    for i in range(len(board)):
        if (rowCollisions(board, i) == 0 and diagonalCollisions(board, i, col) == 0):
            count += 1
    return count


def mrvColumn(board):
    cols = [x for x in range(0, len(board))]
    cols = list(filter(lambda col: board[col] == None, cols))
    cols.sort(key=lambda col: numLegalValues(board, col))
    return 0 if cols.count == 0 else cols[0]


def mcvColumn(board):
    # All variables (columns) attack all other columns in the same number
    return board.index(None)


def selectUnassignedColumn(variableOrdering, board):
    if variableOrdering == VariableOrderings.mcv:
        return mcvColumn(board)
    elif variableOrdering == VariableOrderings.mrv:
        return mrvColumn(board)
    return board.index(None)


def sortedLcvRows(board, column):
    rows = [x for x in range(0, len(board))]
    rows.sort(key=lambda row: rowCollisions(board, row) +
              diagonalCollisions(board, row, column))
    # print(rows, "[0]:", rowCollisions(board, rows[0]) + diagonalCollisions(board, rows[0], column),
    #       "[7]:", rowCollisions(board, rows[7]) + diagonalCollisions(board, rows[7], column))
    return rows


def generateDomainValues(lcv, board, col):
    if lcv:
        return sortedLcvRows(board, col)
    return [x for x in range(0, len(board))]


def fcPassed(board):
    for i in range(len(board)):
        if board[i] == None and numLegalValues(board, i) == 0:
            return False
    return True


def solve(board, variableOrdering, earlyCheck, lcv):
    global calls
    calls += 1
    if None not in board:
        return board
    newC = selectUnassignedColumn(variableOrdering, board)
    domainValues = generateDomainValues(lcv, board, newC)
    print(calls)
    for domainValue in domainValues:
        if (rowCollisions(board, domainValue) == 0 and diagonalCollisions(board, domainValue, newC) == 0):
            board[newC] = domainValue

            if (earlyCheck == EarlyCheck.fc and not fcPassed(board)):
                board[newC] = None
                continue

            solved = solve(board, variableOrdering,
                           earlyCheck, lcv)

            if solved == None:
                board[newC] = None
            else:
                return solved


def rowCollisions(board, row):
    return len(list(filter(lambda r: r == row, board)))


def diagonalCollisions(board, row, col):
    num = 0
    for i in range(len(board)):
        if (board[i] != None and abs(col - i) == abs(board[i] - row)):
            num += 1
    return num


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print("1" if board[j] == i else "0", end=" ")
        print("")


def backtracking(N, variableOrdering, earlyCheck, lcv):
    result = solve([None] * N, variableOrdering, earlyCheck, lcv)
    printBoard(result)


# board = [1, None, None, None]
# printBoard(board)
# print(numLegalValues(board, 0))

backtracking(8, variableOrdering=VariableOrderings.mrv,
             earlyCheck=EarlyCheck.fc, lcv=False)
