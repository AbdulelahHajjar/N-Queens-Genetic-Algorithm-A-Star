import pygame
import random
from random import randint
import math
from GABoard import GABoard
import copy

FPS = 60

WIDTH = 800
HEIGHT = 600
SIDEBAR_WIDTH = 200

numQueens = 8

SQUARE_SIZE = (WIDTH - SIDEBAR_WIDTH) // numQueens

QUEEN_IMAGE = pygame.transform.scale(
    pygame.image.load("example.png"), (SQUARE_SIZE, SQUARE_SIZE))


def start(numQueens, populationCount, mutationProbability):
    pygame.init()
    pygame.display.set_caption("Genetic Algorithm")
    population = generateQueenIndicesPopulation(numQueens, populationCount)

    generation = 0

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    run = True
    clock = pygame.time.Clock()

    while run:
        generation += 1
        clock.tick(FPS)
        screen.fill(pygame.Color("white"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        drawGameState(screen, population[0].indices)

        if solutionInPopulation(population) == None:
            population = breedPopulation(population, mutationProbability)
        pygame.display.flip()
    pygame.quit()


def drawGameState(screen, board):
    drawQueens(screen, board)


def drawQueens(screen, board):
    colors = [pygame.Color("white"), pygame.Color("light blue")]
    for row in range(numQueens):
        for col in range(numQueens):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(
                col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[col] == row:
                screen.blit(QUEEN_IMAGE, pygame.Rect(col * SQUARE_SIZE,
                                                     row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


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
    population = copy.deepcopy(p)
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


start(numQueens, 300, 0.1)
