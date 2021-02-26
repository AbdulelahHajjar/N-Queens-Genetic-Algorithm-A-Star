import random
from random import randint
import math
from GABoard import GABoard
import copy


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


def geneticAlgorithm(p):
    population = p
    solution = solutionInPopulation(population)
    generation = 1

    while solution == None:
        global currentFittestBoard
        currentFittestBoard = population[0].indices
        print("Best Board:", currentFittestBoard)
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


def breedPopulation(p, mutationProbability):
    population = p
    newPopulation = []
    for i in range(len(population)):
        print("jaja", i)
        s = len(population)
        index1 = int(s * random.random() ** (len(population) / 15))
        index2 = int(s * random.random() ** (len(population) / 15))
        parent1 = population[index1]
        parent2 = population[index2]
        child = crossover(parent1, parent2)
        child = mutate(child, mutationProbability)
        newPopulation.append(child)
    newPopulation.sort()
    return newPopulation


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


def start(numQueens, populationCount, mp):
    mutationProbability = mp
    population = generateQueenIndicesPopulation(numQueens, populationCount)
    geneticAlgorithm(population)


# def startBackgroundAlgorithm(numQueens, populationCount, mp):
#     def start(numQueens, populationCount, mp):
#         print("Starting genetic algorithm: N:", numQueens,
#               ", populationCount:", populationCount, "mutation %:", mp)
#         mutationProbability = mp
#         population = generateQueenIndicesPopulation(numQueens, populationCount)
#         geneticAlgorithm(population)

#     thread = threading.Thread(
#         target=start, name="GA", args=[numQueens, populationCount, mp])
#     thread.start()


if __name__ == "__main__":
    main()
