from FourQueens import *
import random

def generateBoard(white, black):
    list = []
    positions = []
    for i in range(25):
        if i in white:
            list += ["w"]
        else:
            if i in black:
                list += ["b"]
            else:
                list += [""]

    for j in range(5):
        positions += [list[(j)*5:(j+1)*5]]
    return positions

print("Initialized Board")
board = FourQueens()
print(board)

print("Move")
moves = board.generateMoves()
print(moves[0])
board.doMove(moves[0])

print(board)
white = list(range(3)) + [4]
black = range(5, 25)

positions = generateBoard(white, black)
print("Winning Board")
board = FourQueens(positions)
print(board)
moves = board.generateMoves()
board.doMove(moves[1])

randomSamples = random.sample(range(25), 12)
white = randomSamples[:6]
black = randomSamples[6:]

positions = generateBoard(white, black)

print("Random Board")
print(FourQueens(positions))

# print(encode(FourQueens(positions)))
