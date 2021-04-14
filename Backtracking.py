from random import randint
from BTBoard import BTBoard
import enum


class VariableOrderings(enum.Enum):
    mcv = True
    mrv = True


def generateEmptyBoard(numQueens):
    indices = [None] * numQueens
    return BTBoard(indices)


def solve(board, i):
    if i == len(board):
        return board


def selectUnassignedColumnIndex(variableOrdering, board, i):
    if variableOrdering == VariableOrderings.mcv:
        return i + 1  # FIX
    else if variableOrdering == VariableOrderings.mrv:
        return i + 1  # FIX
    return i + 1


def backtracking(board, variableOrdering, lcv, fc, arc):
    print(repr(variableOrdering))


board = generateEmptyBoard(8)
backtracking(None, True, True, True)
