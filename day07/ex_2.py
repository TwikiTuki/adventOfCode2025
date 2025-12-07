basicInputPath = 'input/basicInput.txt'
inputPath = 'input/input.txt'

ENTRY_LOCATION = 'S'
EMPTY_SPACE = '.'
SPLITER = '^'

def parseInput(input):
    manifold = []
    with open(input) as file:
        for line in file:
            line = line.replace('\n', '')
            manifold.append([p for p in line])
    for row in range(len(manifold)):
        for col in range(len(manifold[row])):
            if (manifold[row][col] == EMPTY_SPACE):
                manifold[row][col] = 0
            elif (manifold[row][col] == ENTRY_LOCATION):
                manifold[row][col] = 1
    return manifold

def printManifold(manifold):
    for row in manifold:
        for loc in row:
            print(loc, end = " ")
        print()
    print()
        
def doExercie2(input):
    manifold = parseInput(input)
    # printManifold(manifold)
    for r in range(len(manifold)):
        numCols = len(manifold[r])
        for c in range(numCols):
            location = manifold[r][c]
            prevValue = manifold[r-1][c]
            if (location == SPLITER):
                manifold[r][c-1] += prevValue
                manifold[r][c+1] += prevValue
            elif (prevValue != SPLITER):
                manifold[r][c] += prevValue
    # printManifold(manifold)
    return sum(manifold[-1])

def executeTest(value, expected):
    if (value != expected):
        raise Exception(f"Expected {expected} but got {value}")
def tests():
    executeTest(doExercie2(basicInputPath), 40)
    executeTest(doExercie2(inputPath), 5137133207830)
    print("ALL TESTS PASSED")

tests()
print("EXERCICE 2")
result = doExercie2(inputPath)
print(f"The result of exercice 2 is: {result}")
#print("EXERCICE 2")
#result = doExercie2(inputPath)
#print(f"There are total of {result} fresh items")