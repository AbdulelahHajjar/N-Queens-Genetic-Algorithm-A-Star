import random
import math

N = 8


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
    numberOfAttacks = 0

    # Row-wise Check
    for i in range(N):
        queensInRow = len(list(filter(lambda x: x == 1, board[i])))
        numberOfAttacks += ncr(queensInRow, 2)

    # Column-wise Check
    for column in range(N):
        queensInColumn = 0
        for row in range(N):
            queensInColumn += board[row][column]
        numberOfAttacks += ncr(queensInColumn, 2)


def drawBoard(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ', sep='')
        print()


board = generateBoard(N)
drawBoard(board)
calculateHeuristic(board)
