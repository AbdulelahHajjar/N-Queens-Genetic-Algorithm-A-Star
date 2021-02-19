import random
import math
from collections import defaultdict
from queue import PriorityQueue

N = 8

# TODO: Explain how the queens move


def generateBoard(N):
    # In my implementation of the board, 0 == space on the board with no queen. 1 == space on the board with one queen.

    # Create (N^2 - N) elements (spaces) in a list with NO queens, and join it with N elements with all queens. (List size = N^2 - N + N = N^2)
    board = [0]*(8**2 - 8) + [1]*(8)

    # Shuffle the array for the initial state
    random.shuffle(board)

    # Convert array to 2D by slicing it into rows
    board2D = []
    for i in range(0, N**2, N):
        board2D.append(board[i:i+8])

    # return board2D
    return [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]


def ncr(n, r):
    if r > n:
        return 0
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))


def calculateHeuristic(board):
    # TODO: Explain heuristic used.
    numberOfAttacks = 0

    # Row-wise Check (Count possible attacks)
    for i in range(N):
        queensInRow = len(list(filter(lambda x: x == 1, board[i])))
        numberOfAttacks += ncr(queensInRow, 2)

    # Column-wise Check (Count possible attacks)
    for column in range(N):
        queensInColumn = 0
        for row in range(N):
            queensInColumn += board[row][column]
        numberOfAttacks += ncr(queensInColumn, 2)

    # Extract all diagonals from board (Count possible attacks)
    mainDias = defaultdict(list)
    altDias = defaultdict(list)
    for i in range(N):
        for j in range(N):
            mainDias[i-j].append(board[i][j])
            altDias[i+j].append(board[i][j])

    # Diagonals Check (Count possible attacks)
    queensInDiagonal = 0
    for i in mainDias:
        queensInDiagonal = len(list(filter(lambda x: x == 1, mainDias[i])))
        numberOfAttacks += ncr(queensInDiagonal, 2)

    queensInDiagonal = 0
    for i in altDias:
        queensInDiagonal = len(list(filter(lambda x: x == 1, altDias[i])))
        numberOfAttacks += ncr(queensInDiagonal, 2)

    return numberOfAttacks


def drawBoard(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ', sep='')
        print()


class Node():
    def __init__(self, parentNode=None, board=None):
        self.parentNode = parentNode
        self.board = board
        self.gn = 0
        self.hn = 0
        self.fn = 0


def astar(board):
    root = Node(None, board)

    fringe = PriorityQueue()
    visited = []

    fringe.put((calculateHeuristic(board), board))
    while not fringe.empty():
        currentNode = fringe.get()[1]
        visited.append(currentNode)
        hn = calculateHeuristic(currentNode)

        # TODO: Add note
        if hn == 0:
            # Found board
            # TODO: Print board
            break


board = generateBoard(N)
astar(board)
