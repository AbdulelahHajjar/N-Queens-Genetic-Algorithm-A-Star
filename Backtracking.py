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
        if (not (existsRowCollision(board, i) or existsDiagonalCollision(board, i, col))):
            count += 1
    return count


def mrvColumn(board):
    mrvCol = sys.maxsize
    for col in range(len(board)):
        count = numLegalValues(board, col)
        if board[col] == None and count < mrvCol:
            mrvCol = col
    return mrvCol


def selectUnassignedColumn(variableOrdering, board):
    if variableOrdering == VariableOrderings.mcv:
        return board.index(None)  # FIX
    elif variableOrdering == VariableOrderings.mrv:
        return mrvColumn(board)
    return board.index(None)


def generateDomainValues(lcv, board):
    if lcv:
        return [x for x in range(0, len(board))]  # FIX
    return [x for x in range(0, len(board))]


def solve(board, variableOrdering, earlyCheck, lcv):
    global calls
    calls += 1
    if None not in board:
        return board
    newC = selectUnassignedColumn(variableOrdering, board)
    domainValues = generateDomainValues(lcv, board)
    print(calls)
    for domainValue in domainValues:
        if (not (existsRowCollision(board, domainValue) or existsDiagonalCollision(board, domainValue, newC))):
            newBoard = copy.deepcopy(board)
            newBoard[newC] = domainValue
            result = solve(newBoard, variableOrdering,
                           earlyCheck, lcv)
            if result == None:
                newBoard[newC] = None
            else:
                return result


def existsRowCollision(board, newRow):
    return newRow in board


def existsDiagonalCollision(board, newR, newC):
    for i in range(len(board)):
        if (board[i] != None and abs(newC - i) == abs(board[i] - newR)):
            return True
    return False


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print("1" if board[j] == i else "0", end=" ")
        print("")


def backtracking(N, variableOrdering, earlyCheck, lcv):
    result = solve([None] * N, variableOrdering, earlyCheck, lcv)
    printBoard(result)


# print(existsDiagonalCollision([1], 1))
# print(existsDiagonalCollision([0, 3, None, None], 1, 2))
backtracking(4, None,
             earlyCheck=None, lcv=False)
