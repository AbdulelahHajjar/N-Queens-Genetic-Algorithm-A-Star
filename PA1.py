import random
import math
from collections import defaultdict
from queue import PriorityQueue
import time
import copy
from itertools import *
import functools
import heapq

N = 8

# TODO: Explain how the queens move


def generateBoard(N):
    # In my implementation of the board, 0 == space on the board with no queen. 1 == space on the board with one queen.

    # Create (N^2 - N) elements (spaces) in a list with NO queens, and join it with N elements with all queens. (List size = N^2 - N + N = N^2)
    board = [0]*(N**2 - N) + [1]*(N)

    # Shuffle the array for the initial state
    random.shuffle(board)

    # Convert array to 2D by slicing it into rows
    board2D = []
    for i in range(0, N**2, N):
        board2D.append(board[i:i+N])

    indexRepresentationArray = []
    for i in range(N):
        for j in range(N):
            if board2D[i][j] == 1:
                indexRepresentationArray.append((i, j))
    return indexRepresentationArray


def ncr(n, r):
    if r > n:
        return 0
    elif r == n:
        return 1
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))


# def calculateHeuristic(board):
#     # TODO: Explain heuristic used.
#     numberOfAttacks = 0

#     # Row-wise Check (Count possible attacks)
#     for i in range(N):
#         queensInRow = len(list(filter(lambda x: x == 1, board[i])))
#         numberOfAttacks += ncr(queensInRow, 2)

#     # Column-wise Check (Count possible attacks)
#     for column in range(N):
#         queensInColumn = 0
#         for row in range(N):
#             queensInColumn += board[row][column]
#         numberOfAttacks += ncr(queensInColumn, 2)

#     # Extract all diagonals from board (Count possible attacks)
#     mainDias = defaultdict(list)
#     altDias = defaultdict(list)
#     for i in range(N):
#         for j in range(N):
#             mainDias[i-j].append(board[i][j])
#             altDias[i+j].append(board[i][j])

#     # Diagonals Check (Count possible attacks)
#     queensInDiagonal = 0
#     for i in mainDias:
#         queensInDiagonal = len(list(filter(lambda x: x == 1, mainDias[i])))
#         numberOfAttacks += ncr(queensInDiagonal, 2)

#     queensInDiagonal = 0
#     for i in altDias:
#         queensInDiagonal = len(list(filter(lambda x: x == 1, altDias[i])))
#         numberOfAttacks += ncr(queensInDiagonal, 2)

#     return numberOfAttacks


def newCalculateHeuristic(queensIndices):
    numAttacks = 0

    tempBoard = copy.deepcopy(queensIndices)
    while len(tempBoard) > 0:
        queen = tempBoard[0]
        del tempBoard[0]
        nextQueen = (queen[0], 0)
        numQueens = 1
        while nextQueen[0] < N and nextQueen[1] < N and nextQueen[0] >= 0 and nextQueen[1] >= 0:
            if nextQueen in tempBoard:
                numQueens += 1
                tempBoard.remove(nextQueen)
            nextQueen = (nextQueen[0], nextQueen[1] + 1)
        # print("Found: " + str(numQueens) + ", in row: " + str(queen[0]))
        numAttacks += ncr(numQueens, 2)

    tempBoard = copy.deepcopy(queensIndices)
    while len(tempBoard) > 0:
        queen = tempBoard[0]
        del tempBoard[0]
        nextQueen = (0, queen[1])
        numQueens = 1
        while nextQueen[0] < N and nextQueen[1] < N and nextQueen[0] >= 0 and nextQueen[1] >= 0:
            if nextQueen in tempBoard:
                numQueens += 1
                tempBoard.remove(nextQueen)
            nextQueen = (nextQueen[0] + 1, nextQueen[1])
        # print("Found: " + str(numQueens) + ", in column: " + str(queen[1]))
        numAttacks += ncr(numQueens, 2)

    tempBoard = copy.deepcopy(queensIndices)
    while len(tempBoard) > 0:
        queen = tempBoard[0]
        del tempBoard[0]
        nextQueen = (queen[0] - min(queen[0], queen[1]),
                     queen[1] - min(queen[0], queen[1]))
        numQueens = 1
        while nextQueen[0] < N and nextQueen[1] < N and nextQueen[0] >= 0 and nextQueen[1] >= 0:
            if nextQueen in tempBoard:
                numQueens += 1
                tempBoard.remove(nextQueen)
            nextQueen = (nextQueen[0] + 1, nextQueen[1] + 1)
        # print("Found: " + str(numQueens) + ", in main diagonals")
        numAttacks += ncr(numQueens, 2)

    tempBoard = copy.deepcopy(queensIndices)
    while len(tempBoard) > 0:
        queen = tempBoard[0]
        del tempBoard[0]
        firstIDiagonal = queen[0]
        firstJDiagonal = queen[1]
        while firstIDiagonal >= 0 and firstJDiagonal < N:
            if firstIDiagonal - 1 < 0 or firstJDiagonal + 1 >= N:
                break
            firstIDiagonal -= 1
            firstJDiagonal += 1
        nextQueen = (firstIDiagonal, firstJDiagonal)
        numQueens = 1
        while nextQueen[0] < N and nextQueen[1] < N and nextQueen[0] >= 0 and nextQueen[1] >= 0:
            if nextQueen in tempBoard:
                numQueens += 1
                tempBoard.remove(nextQueen)
            nextQueen = (nextQueen[0] + 1, nextQueen[1] - 1)
        # print("Found: " + str(numQueens) + ", in alternative diagonals")
        numAttacks += ncr(numQueens, 2)
    return numAttacks


# def drawBoard(board):
#     for i in range(N):
#         for j in range(N):
#             print(board[i][j], end=' ', sep='')
#         print()


def newDrawBoard(queensIndices):
    for i in range(N):
        for j in range(N):
            if (i, j) in queensIndices:
                print("1", end=' ', sep='')
            else:
                print("0", end=' ', sep='')
        print()


class Node():
    def __init__(self, board=None):
        self.board = board
        self.gn = 0
        self.hn = 0

    def fn(self):
        return self.gn + self.hn

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.board == other.board
        else:
            return False

    def __lt__(self, other):
        return self.fn() < other.fn()


# def generateNextStatesForQueenAt(i, j, board):
#     nextStates = []
#     for xOffset in [-1, 0, 1]:
#         for yOffset in [-1, 0, 1]:
#             if xOffset == 0 and yOffset == 0:
#                 continue

#             newI = i + xOffset
#             newJ = j + yOffset

#             if newI < 0 or newJ < 0 or newI >= N or newJ >= N:
#                 continue

#             if board[newI][newJ] == 1:
#                 continue

#             tempBoard = copy.deepcopy(board)
#             tempBoard[i][j] = 0
#             tempBoard[newI][newJ] = 1

#             node = Node(tempBoard)
#             nextStates.append(node)
#     return nextStates


def newGenerateNextStatesForQueenAt(i, j, queensIndices):
    nextStates = []
    for iOffset in [-1, 0, 1]:
        for jOffset in [-1, 0, 1]:
            if iOffset == 0 and jOffset == 0:
                continue

            newI = i + iOffset
            newJ = j + jOffset

            if newI < 0 or newJ < 0 or newI >= N or newJ >= N:
                continue

            if (newI, newJ) in queensIndices:
                continue

            newQueensIndices = copy.deepcopy(queensIndices)
            newQueensIndices.remove((i, j))
            newQueensIndices.append((newI, newJ))

            node = Node(newQueensIndices)
            nextStates.append(node)
    return nextStates


def astar(board):
    # TODO: Explain gn and hn
    fringe = []
    visited = []

    root = Node(board)
    root.hn = newCalculateHeuristic(root.board)
    root.gn = 0

    heapq.heappush(fringe, root)
    while len(fringe) > 0:
        currentNode = heapq.heappop(fringe)

        print("Visited: " + str(len(visited)) +
              ", Fringe: " + str(len(fringe)) + ", Current h(n): " + str(currentNode.hn))

        visited.append(currentNode)

        newDrawBoard(currentNode.board)

        print()

        # TODO: Add note
        if currentNode.hn == 0:
            # Found board
            # TODO: Print board
            print("Found solution.")
            print(currentNode.board)
            break

        childrenNodes = []
        for queen in currentNode.board:
            childrenNodes = list(
                chain(childrenNodes, newGenerateNextStatesForQueenAt(queen[0], queen[1], currentNode.board)))

        for childNode in childrenNodes:
            childNode.hn = newCalculateHeuristic(childNode.board)
            childNode.gn = 1

            isVisitedBefore = False
            isFringedBefore = False
            childNodeIsBetter = False

            for visitedNode in visited:
                if visitedNode.board == childNode.board:
                    isVisitedBefore = True
                    break

            for i in range(len(fringe)):
                if fringe[i].board == childNode.board:
                    isFringedBefore = True
                    childNodeIsBetter = childNode.fn() < fringe[i].fn()
                    del fringe[i]
                    heapq.heapify(fringe)
                    break

            if not isVisitedBefore and not isFringedBefore:
                heapq.heappush(fringe, childNode)
            elif isFringedBefore and childNodeIsBetter:
                heapq.heappush(fringe, childNode)


board = generateBoard(N)
newDrawBoard(board)
astar(board)
