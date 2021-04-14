from random import randint
from BTBoard import BTBoard
import enum


class VariableOrderings(enum.Enum):
    mcv = True
    mrv = True


def selectUnassignedColumnIndex(variableOrdering, board, i):
    if variableOrdering == VariableOrderings.mcv:
        return i + 1  # FIX
    else if variableOrdering == VariableOrderings.mrv:
        return i + 1  # FIX
    return i + 1


def generateDomainValues(lcv, boardSize):
    if lcv:
        return [x for x in range(0, boardSize)]  # FIX
    return [x for x in range(0, boardSize)]


def solve(board, variableOrdering, i):
    if i == len(board):
        return board

    newI = selectUnassignedColumnIndex(variableOrdering, board, i)
    domainValues = generateDomainValues()


def backtracking(board, variableOrdering, lcv, fc, arc):
    solve([], variableOrdering, 0)


backtracking(True, True, True)
