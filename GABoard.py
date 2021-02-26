import copy
from Functions import ncr
import math


class GABoard():
    def __init__(self, indices=None):
        self.indices = indices

    def fitness(self):
        # It is not needed to check for column-wise attacks because the indices array implementation does not allow more than one queen per column.

        # Check for duplicates by converting it into a set (removes duplicates, i.e., no row attacks.)
        indicesCopy = copy.deepcopy(self.indices)
        numAttacks = 0
        if len(indicesCopy) != len(set(indicesCopy)):
            for row in range(len(indicesCopy)):
                result = list(filter(lambda x: x == row, indicesCopy))
                rowQueens = len(result)
                numAttacks += ncr(rowQueens, 2)

        checkedIndices = []
        for column in range(len(indicesCopy)):
            row = indicesCopy[column]
            diagonalQueens = 0
            while (row, column) not in checkedIndices and row >= 0 and row < len(indicesCopy) and column >= 0 and column < len(indicesCopy):
                if indicesCopy[column] == row:
                    diagonalQueens += 1
                checkedIndices.append((row, column))
                row += 1
                column += 1
            numAttacks += ncr(diagonalQueens, 2)

        checkedIndices = []
        for column in range(len(indicesCopy)):
            row = indicesCopy[column]
            diagonalQueens = 0
            while (row, column) not in checkedIndices and row >= 0 and row < len(indicesCopy) and column >= 0 and column < len(indicesCopy):
                if indicesCopy[column] == row:
                    diagonalQueens += 1
                checkedIndices.append((row, column))
                row -= 1
                column += 1
            numAttacks += ncr(diagonalQueens, 2)
        return numAttacks

    def __lt__(self, other):
        return self.fitness() < other.fitness()
