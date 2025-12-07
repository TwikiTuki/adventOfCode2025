basicInputPath = 'input/basicInput.txt'
inputPath = 'input/input.txt'

ENTRY_LOCATION = 'S'
EMPTY_SPACE = '.'
SPLITER = '^'
BEAM = '|'

def parseInput(input):
    manifold = []
    with open(input) as file:
        for line in file:
            line = line.replace('\n', '')
            manifold.append([p for p in line])
    return manifold

def printManifold(manifold):
    for row in manifold:
        print(row)
        
def doExercie1(input):
    manifold = parseInput(input)
    timesSplited = 0
    # printManifold(manifold)
    for r in range(len(manifold[1:])):
        row = manifold[r]
        # printManifold(manifold)
        for c in range(len(row)):
            if (manifold[r-1][c] not in [BEAM, ENTRY_LOCATION]):
                continue
            location = manifold[r][c]
            if (location == SPLITER):
                manifold[r][c-1] = BEAM
                manifold[r][c+1] = BEAM
                timesSplited += 1
            else:
                manifold[r][c] = BEAM
    return timesSplited


def doExercie2(inputPath):
    pass

def executeTest(value, expected):
    if (value != expected):
        raise Exception(f"Expected {expected} but got {value}")
def tests():
    # assert doExercie1(basicInputPath) == 4277556
    # assert doExercie1(inputPath) == 6757749566978
    executeTest(doExercie1(basicInputPath), 21)
    print("ALL TESTS PASSED")

tests()
print("EXERCICE 1")
result = doExercie1(inputPath)
print(f"The result of exercice 1 is: {result}")
#print("EXERCICE 2")
#result = doExercie2(inputPath)
#print(f"There are total of {result} fresh items")