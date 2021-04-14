from random import randint
import enum
import time
import copy
import sys

iterations = 0
queenImage = pygame.transform.scale(
    pygame.image.load("queen.png"), (squareSize(numQueens), squareSize(numQueens)))


class VariableOrderings(enum.Enum):
    mcv = 0
    mrv = 1


class EarlyCheck(enum.Enum):
    arc = 0
    fc = 1


def start(N, variableOrdering, earlyCheck, lcv):
    pygame.init()
    pygame.display.set_caption("PHW02")
    foundSolution = False
    pause = False

    global queenImage
    global calls

    queenImage = pygame.transform.scale(
        pygame.image.load("queen.png"), (squareSize(numQueens), squareSize(numQueens)))

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    run = True
    clock = pygame.time.Clock()

    while run:
        if foundSolution == False and not pause:
            iterations += 1

        clock.tick(FPS)
        screen.fill(pygame.Color("white"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = True

        drawGameState(screen,
                      population[0].indices,
                      populationCount,
                      generation,
                      maxGenerations,
                      mutationProbability,
                      foundSolution)

        if not pause and generation <= maxGenerations and (foundSolution == False and solutionInPopulation(population) == None):
            population = breedPopulation(population, mutationProbability)
        else:
            if solutionInPopulation(population) != None and generation <= maxGenerations:
                foundSolution = True
        pygame.display.flip()
    pygame.quit()


def drawGameState(screen, board, iterations, foundSolution):
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


if __name__ == '__main__':
    start(N=8,
          variableOrdering=VariableOrderings.mrv,
          earlyCheck=EarlyCheck.fc,
          lcv=True)
