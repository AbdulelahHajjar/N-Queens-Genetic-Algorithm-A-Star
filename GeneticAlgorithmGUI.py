import pygame
import random
from random import randint
import math
from GABoard import GABoard
import copy

FPS = 60

WIDTH = 600
HEIGHT = 600

numQueens = 8


def squareSize(N):
    return (WIDTH) // numQueens


queenImage = pygame.transform.scale(
    pygame.image.load("queen.png"), (squareSize(numQueens), squareSize(numQueens)))


def start(n, populationCount, maxGenerations, mutationProbability):
    pygame.init()
    pygame.display.set_caption("Genetic Algorithm")
    foundSolution = False
    pause = False
    global numQueens
    numQueens = n

    global queenImage
    queenImage = pygame.transform.scale(
        pygame.image.load("queen.png"), (squareSize(numQueens), squareSize(numQueens)))

    population = generateQueenIndicesPopulation(numQueens, populationCount)

    generation = 0

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    run = True
    clock = pygame.time.Clock()

    while run:
        if foundSolution == False and not pause and generation <= maxGenerations:
            generation += 1

        clock.tick(FPS)
        screen.fill(pygame.Color("white"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = True

        drawGameState(screen, population[0].indices, populationCount,
                      generation, maxGenerations, mutationProbability, foundSolution)

        if not pause and generation <= maxGenerations and (foundSolution == False and solutionInPopulation(population) == None):
            population = breedPopulation(population, mutationProbability)
        else:
            foundSolution = True
        pygame.display.flip()
    pygame.quit()


def drawGameState(screen, board, populationSize, curGen, maxGen, mutationRate, foundSolution):
    drawQueens(screen, board)
    font = pygame.font.Font(pygame.font.get_default_font(), 18)
    textsurface = font.render(
        f"Population Size: {populationSize}", False, (0, 0, 0))
    screen.blit(textsurface, (0, 0))
    font = pygame.font.Font(pygame.font.get_default_font(), 18)
    textsurface = font.render(f"Generation #:{curGen}", False, (0, 0, 0))
    screen.blit(textsurface, (0, 20))
    font = pygame.font.Font(pygame.font.get_default_font(), 18)
    textsurface = font.render(f"Max Generations:{maxGen}", False, (0, 0, 0))
    screen.blit(textsurface, (0, 40))
    font = pygame.font.Font(pygame.font.get_default_font(), 18)
    textsurface = font.render(
        f"Mutation Rate:{mutationRate}", False, (0, 0, 0))
    screen.blit(textsurface, (0, 60))
    font = pygame.font.Font(pygame.font.get_default_font(), 18)
    textsurface = font.render(
        f"Solution found" if foundSolution else "Solution not found", False, (255 if not foundSolution else 0, 255 if foundSolution else 0, 0))
    screen.blit(textsurface, (0, 80))


def drawQueens(screen, board):
    colors = [pygame.Color("white"), pygame.Color("light blue")]
    for row in range(numQueens):
        for col in range(numQueens):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(
                col * squareSize(numQueens), row * squareSize(numQueens), squareSize(numQueens), squareSize(numQueens)))
            if board[col] == row:
                screen.blit(queenImage, pygame.Rect(col * squareSize(numQueens),
                                                    row * squareSize(numQueens), squareSize(numQueens), squareSize(numQueens)))


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
            index1 = int(s * random.random() ** (len(population) / 25))
            index2 = int(s * random.random() ** (len(population) / 25))
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


if __name__ == '__main__':
    start(numQueens, 300, 0.1)
