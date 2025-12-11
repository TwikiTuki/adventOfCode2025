

from enum import Enum

basicInputPath = "input/basic_input_1.txt"
inputPath = "input/input_1.txt"

def parseInput(input):
    parsed = []
    with open(input)as inp:
        for line in inp:
            parsed.append([r for r in line.replace('\n', "")])
    return parsed
    pass

class Department():
    EMPYT_SPACE = '.'
    ROLL = '@'
    MOVABLE_ROLL = 'x'
    EMPTY_SPACE_NEEDED = 5

    def __init__(self, input):
        self.room = input
        self.rows = len(self.room)
        self.cols = len(self.room[0])

    def insideDepartmen(self, row, col):
        if (row < 0 or row >= self.rows):
            return False
        if (col < 0 or col >= self.cols):
            return False
        return True

    def isEmpty(self, row, col):
        if (not self.insideDepartmen(row, col)):
            return True
        return self.room[row][col] == self.EMPYT_SPACE 
    
    def isMovable(self, row, col):
        # print('----')
        # print( row, col, self.rows, self.cols, self.room[row][col])
        if (self.isEmpty(row, col)):
            return False
        # print("  ", row, col)
        surroundingEmpty = 0
        for r in range(-1,2):
            for c in range(-1,2):
                if(self.isEmpty(row+r, col+c)):
                    surroundingEmpty += 1
        return surroundingEmpty >= self.EMPTY_SPACE_NEEDED
    
    def countMovable(self):
        movable = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.isMovable(row, col):
                    # print("sdaf")
                    self.room[row][col] = self.EMPYT_SPACE
                    movable += 1

        # for row in self.room:
            # print(row)
        return movable

# def doExercice1(inputPath):
#     input = parseInput(inputPath)
#     department = Department(input)
#     movable = department.countMovable()
#     print(f"The departme has {movable} movable elements")
#     return movable

def doExercice2(input):
    input = parseInput(inputPath)
    department = Department(input)
    totalMovable = 0
    while (True):
        movable = department.countMovable()
        totalMovable += movable
        if (movable == 0):
            break
        print(f"moved {movable} rolls")
    print(f"The departmen had {totalMovable} movable elements")
    return totalMovable
    pass

def tests():
    # assert doExercice1(basicInputPath) == 13
    # assert doExercice1(inputPath) == 1495
    assert doExercice2(basicInputPath) == 43
    print("ALL TESTS PASSED")
# print("----------------------------------")
# for row in parseInput(basicInputPath):
    # print(row)
print("----------------------------------")
tests()
print("Exercice 1")
doExercice1(inputPath)
print("Exercice 2")
# doExercice2(inputPath, 12)