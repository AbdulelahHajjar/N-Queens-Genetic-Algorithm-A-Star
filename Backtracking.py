from random import randint
import enum
import time
import copy
import sys
import pygame

# GUI Related Variables and Functions
WIDTH = 600
HEIGHT = 600
FPS = 60


def squareSize(N):
    return (WIDTH) // N


def queenImage(N):
    return pygame.transform.scale(
        pygame.image.load("queen.png"), (squareSize(N), squareSize(N)))


# Global Game State Variables
iterations = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
globalBoard = []
pause = False

# Enum for Solution Options (MCV or MRV, ARC or FC)


class VariableOrderings(enum.Enum):
    mcv = 0
    mrv = 1


class EarlyCheck(enum.Enum):
    arc = 0
    fc = 1

# GUI Function (Start Calling This Function First)


def start(N, variableOrdering, earlyCheck, lcv):
    pygame.init()
    pygame.display.set_caption("PHW02")

    foundSolution = False
    initialStart = False
    board = [None]*N

    run = True
    clock = pygame.time.Clock()
    while run:
        global pause
        global iterations
        clock.tick(FPS)
        screen.fill(pygame.Color("white"))

        if (initialStart == False):
            solve(board, variableOrdering, earlyCheck, lcv)
            initialStart = True
    pygame.quit()

# Function used to Draw Game State


def drawGameState(screen, board, iterations, foundSolution, pause):
    drawQueens(screen, board)
    font = pygame.font.Font(pygame.font.get_default_font(), 18)
    textsurface = font.render(f"Iterations:{iterations}", False, (0, 0, 0))
    screen.blit(textsurface, (0, 0))

    font = pygame.font.Font(pygame.font.get_default_font(), 18)
    textsurface = font.render(
        f"Paused:{pause} (Press ESC to Toggle)", False, (0, 0, 0))
    screen.blit(textsurface, (0, 20))

    font = pygame.font.Font(pygame.font.get_default_font(), 18)
    textsurface = font.render(
        f"Solution found" if foundSolution else "Solution not found", False, (255 if not foundSolution else 0, 255 if foundSolution else 0, 0))
    screen.blit(textsurface, (0, 40))

# Draw Queens on Board


def drawQueens(screen, board):
    colors = [pygame.Color("white"), pygame.Color("light blue")]
    for row in range(len(board)):
        for col in range(len(board)):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(
                col * squareSize(len(board)), row * squareSize(len(board)), squareSize(len(board)), squareSize(len(board))))
            if board[col] == row:
                screen.blit(queenImage(len(board)), pygame.Rect(col * squareSize(len(board)),
                                                                row * squareSize(len(board)), squareSize(len(board)), squareSize(len(board))))

# Returns the number of legal moves in a given column, returns 0 if no moves are possible.


def numLegalValues(board, col):
    count = 0
    for i in range(len(board)):
        if (rowCollisions(board, i) == 0 and diagonalCollisions(board, i, col) == 0):
            count += 1
    return count

# Returns a column with the least amount of legal moves in it


def mrvColumn(board):
    cols = [x for x in range(0, len(board))]
    cols = list(filter(lambda col: board[col] == None, cols))
    cols.sort(key=lambda col: numLegalValues(board, col))
    return 0 if cols.count == 0 else cols[0]


# Returns a column which attacks the most amount of columns (However, all columns attack the same number of columns.)
def mcvColumn(board):
    # All variables (columns) attack all other columns in the same number.
    # Returns the next empty column
    return board.index(None)

# Returns an unassigned column (with no queen) based on a variable ordering variable


def selectUnassignedColumn(variableOrdering, board):
    if variableOrdering == VariableOrderings.mcv:
        return mcvColumn(board)
    elif variableOrdering == VariableOrderings.mrv:
        return mrvColumn(board)
    # return next empty column
    return board.index(None)

# Return a sorted list of rows for a given column. Placing a queen on the first row will create the LEAST amount of collisions
# Placing a queen in the last row will create the most collisions


def sortedLcvRows(board, column):
    rows = [x for x in range(0, len(board))]
    rows.sort(key=lambda row: rowCollisions(board, row) +
              diagonalCollisions(board, row, column))
    # print(rows, "[0]:", rowCollisions(board, rows[0]) + diagonalCollisions(board, rows[0], column),
    #       "[7]:", rowCollisions(board, rows[7]) + diagonalCollisions(board, rows[7], column))
    return rows

# Returns domain values (rows to place queens in) based on either LCV or no LCV.


def generateDomainValues(lcv, board, col):
    if lcv:
        return sortedLcvRows(board, col)
    return [x for x in range(0, len(board))]

# Checks if the forward checking algorithm passed for a given board.
# If any cell in the given board has NO legal moves at all, the board does not pass the forward checking algorithm


def fcPassed(board):
    for i in range(len(board)):
        if board[i] == None and numLegalValues(board, i) == 0:
            return False
    return True

# Checks the number of row collisions which is the number of repeated row in the 1D array of board


def rowCollisions(board, row):
    return len(list(filter(lambda r: r == row, board)))

# Checks diagonal collisions by checking if the manhatten distance between the column index of the two cells is equal to the distance of the row indices of the second cell


def diagonalCollisions(board, row, col):
    num = 0
    for i in range(len(board)):
        if (board[i] != None and abs(col - i) == abs(board[i] - row)):
            num += 1
    return num

# Debugging purposes


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print("1" if board[j] == i else "0", end=" ")
        print("")

# Recursive call to solve the N-Queens


def solve(board, variableOrdering, earlyCheck, lcv):
    global pause
    global iterations
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if pause:
                    pause = False
                else:
                    pause = True

    drawGameState(screen, board, iterations, None not in board, pause)
    pygame.display.flip()
    print(board)
    if pause:
        solve(board, variableOrdering, earlyCheck, lcv)
    if None not in board:
        return board
    iterations += 1
    newColumn = selectUnassignedColumn(variableOrdering, board)
    domainValues = generateDomainValues(lcv, board, newColumn)

    for domainValue in domainValues:
        if (rowCollisions(board, domainValue) == 0 and diagonalCollisions(board, domainValue, newColumn) == 0):
            board[newColumn] = domainValue

            if (earlyCheck == EarlyCheck.fc and not fcPassed(board)):
                board[newColumn] = None
                continue

            solved = solve(board, variableOrdering,
                           earlyCheck, lcv)

            if solved == None:
                board[newColumn] = None
            else:
                return solved


if __name__ == '__main__':
    start(N=8,
          variableOrdering=VariableOrderings.mrv,
          earlyCheck=EarlyCheck.fc,
          lcv=True)
