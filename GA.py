import random
from random import randint
import math
import copy

N = 10
mutationProbability = 0.1


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


def generateQueenIndicesPopulation(numQueens, populationCount):
    population = []
    for x in range(populationCount):
        indices = []
        for i in range(numQueens):
            indices.append(randint(0, numQueens - 1))
            board = GABoard(indices)
        population.append(board)
    population.sort()
    return population


def drawBoard(indices):
    for i in range(len(indices)):
        for j in range(len(indices)):
            print("1 " if i == indices[j] else "0 ", end="")
        print("")


def ncr(n, r):
    if r > n:
        return 0
    elif r == n:
        return 1
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))


def geneticAlgorithm(p):
    population = p
    solution = solutionInPopulation(population)
    generation = 1

    while solution == None:
        newPopulation = []
        for i in range(len(population)):
            s = len(population)
            index1 = int(s * random.random() ** (len(population) / 15))
            index2 = int(s * random.random() ** (len(population) / 15))
            parent1 = population[index1]
            parent2 = population[index2]
            child = crossover(parent1, parent2)
            child = mutate(child, mutationProbability)
            newPopulation.append(child)
        newPopulation.sort()
        population = newPopulation
        solution = solutionInPopulation(population)
        generation += 1
    drawBoard(solution.indices)


def mutate(child, probaility):
    indicesCopy = copy.deepcopy(child.indices)
    for i in range(len(indicesCopy)):
        if random.random() < probaility:
            indicesCopy[i] = randint(0, len(indicesCopy) - 1)
    board = GABoard(indicesCopy)
    return board


def crossover(parent1, parent2):
    # Single-point crossover, first half, and second half
    newIndices = []
    for i in range(len(parent1.indices)):
        if i <= len(parent1.indices) // 2:
            newIndices.append(parent1.indices[i])
        else:
            newIndices.append(parent2.indices[i])
    board = GABoard(newIndices)
    return board


def solutionInPopulation(population):
    for i in range(len(population)):
        board = population[i]
        if board.fitness() == 0:
            return board
    return None


population = generateQueenIndicesPopulation(N, 300)
geneticAlgorithm(population)
