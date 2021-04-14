from random import randint
import enum
import time
import copy


class VariableOrderings(enum.Enum):
    mcv = True
    mrv = True


class EarlyCheck(enum.Enum):
    arc = True
    fc = True


def selectUnassignedColumn(variableOrdering, board):
    if variableOrdering == VariableOrderings.mcv:
        return board.index(None)  # FIX
    elif variableOrdering == VariableOrderings.mrv:
        return board.index(None)  # FIX
    return board.index(None)


def generateDomainValues(lcv, board):
    if lcv:
        return [x for x in range(0, len(board))]  # FIX
    return [x for x in range(0, len(board))]


def solve(board, variableOrdering, earlyCheck, lcv):
    if None not in board:
        return board

    newC = selectUnassignedColumn(variableOrdering, board)
    domainValues = generateDomainValues(lcv, board)

    print(board)

    for domainValue in domainValues:
        if (not (existsRowCollision(board, domainValue) or existsDiagonalCollision(board, domainValue, newC))):
            newBoard = copy.deepcopy(board)
            newBoard[newC] = domainValue
            result = solve(newBoard, variableOrdering, earlyCheck, lcv)
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
backtracking(8, variableOrdering=None, earlyCheck=None, lcv=False)
