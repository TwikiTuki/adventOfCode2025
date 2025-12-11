from enum import Enum

basicInputPath = "input/basic_input_1.txt"
inputPath = "input/input_1.txt"

def parseInput(input):
    parsed = []
    with open(input)as inp:
        for line in inp:
            parsed.append(Action.fromString(line))
    return parsed

class Direction(Enum):
    RIGHT = 1
    LEFT = -1

    @classmethod
    def fromString(clss, direction):
        if(direction == 'R'):
            return clss.RIGHT
        if(direction == 'L'):
            return clss.LEFT
        raise Exception("Invalid Direction: " + direction)
    def __repr__(self):
        if(self == Direction.RIGHT):
            return 'R'
        if(self == Direction.LEFT):
            return 'L'

class Action:
    def __init__(self, direction, steps):
        self.direction = direction
        self.steps = steps

    @classmethod
    def fromString(clss, string):
        return Action(Direction.fromString(string[0]), int(string[1:-1]))

    def __str__(self):
        return("" + self.direction.__repr__() + self.steps.__str__())

class Locker():
    MIN_POSITION = 0
    MAX_POSITION = 99
    STEPS = 99 - 0 + 1

    def countActionTimesThrough0(self, action):
        return self.countTimesThrough0(action.steps, action.direction)

    def countTimesThrough0(self, steps, direction):
        loops = int(steps / Locker.STEPS)
        remainder = steps % Locker.STEPS
        if (direction == Direction.RIGHT and (self.position + remainder) >= Locker.STEPS):
            loops += 1
        elif (direction == Direction.LEFT and (self.position - remainder) <= 0):
            loops += 1
        return loops

    def __init__(self, position = 50):
        self.position = position

    def doAction(self, action):
        self.rotate(action.steps, action.direction)

    def rotate(self, steps, direction):
        self.position += steps * direction.value
        self.position %= self.STEPS

def doExercice1(inputPath):
    parsedInput = parseInput(inputPath) 
    locker = Locker()
    zeroCount = 0
    for action in parsedInput:
        if (locker.position == 0):
            zeroCount += 1
        locker.doAction(action)
    print(f"The zeros count is {zeroCount}")
    return zeroCount

def doExercice2(inputPath):
    parsedInput = parseInput(inputPath) 
    locker = Locker()
    zeroCount = 0
    for action in parsedInput:
        if (locker.position == 0):
            zeroCount += locker.countActionTimesThrough0(action)
        locker.doAction(action)
    print(f"The zeros count is {zeroCount}")
    return zeroCount

def __main__(): 
    print("Main")
    # doExercice1(inputPath)
    # doExercice2(inputPath)

def tests():
    parsedInput = parseInput(basicInputPath) 
    assert Direction.fromString("R") ==  Direction.RIGHT
    assert Direction.fromString("L") ==  Direction.LEFT
    locker = Locker()
    assert locker.position == 50
    # locker.rotate(50, Direction.RIGHT)
    # assert locker.position == 0
    # locker.rotate(5, Direction.RIGHT)
    # assert locker.position == 5
    # locker.rotate(6, Direction.LEFT)
    # assert locker.position == 99
    # locker.doAction(parsedInput[0])
    # assert locker.position == 99 - 68
    # locker.doAction(parsedInput[1])
    # assert locker.position == 99 - 68 - 30
    # locker.doAction(parsedInput[2])
    # assert locker.position == 99 - 68 - 30 + 48 
    print(locker.countTimesThrough0(100, Direction.RIGHT))
    assert locker.countTimesThrough0(100, Direction.RIGHT) == 1
    assert locker.countTimesThrough0(100, Direction.LEFT) == 1
    assert locker.countTimesThrough0(200, Direction.RIGHT) == 2
    assert locker.countTimesThrough0(200, Direction.LEFT) == 2
    assert locker.countTimesThrough0(300, Direction.RIGHT) == 3
    assert locker.countTimesThrough0(300, Direction.LEFT) == 3
    assert locker.countTimesThrough0(49, Direction.RIGHT) == 0
    assert locker.countTimesThrough0(49, Direction.LEFT) == 0
    print(locker.countTimesThrough0(50, Direction.RIGHT))
    assert locker.countTimesThrough0(50, Direction.RIGHT) == 1
    assert locker.countTimesThrough0(50, Direction.LEFT) == 1
    assert locker.countTimesThrough0(150, Direction.RIGHT) == 2
    assert locker.countTimesThrough0(150, Direction.LEFT) == 2
    assert doExercice1(basicInputPath) == 3
    print(doExercice2(basicInputPath))
    # assert doExercice2(basicInputPath) == 6
    print("ALL TESTS PASSED")

__main__()
tests()