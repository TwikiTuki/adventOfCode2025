basicInputPath = 'input/basicInput.txt'
inputPath = 'input/input.txt'

def parseInput(input):
    with open(input) as file:
        allInput = file.read()
        lines = allInput.split('\n')
        assert lines.count('') == 1
        emptyLine = lines.index("")
        freshRangesInput = lines[0: emptyLine]
        foodsIdsInput = lines[emptyLine + 1: ]
    freshRanges = []
    for range in freshRangesInput:
        min, max = range.split('-')
        freshRanges.append((int(min), int(max)))
    foodsIds = [int(id) for id in foodsIdsInput]
    return freshRanges, foodsIds

def checkInRange(foodId, freshRange):
    if foodId < freshRange[0]:
        return False
    if foodId > freshRange[1]:
        return False
    return True

def checkFreshnes(foodId, freshRanges):
    for range in freshRanges:
        # print(f"  Checking range {range}")
        if (checkInRange(foodId, range)):
            # print("  OK")
            return True
        # print("  KO")
    return False

def doExercie1(inputPath):
    freshRanges, foodsIds = parseInput(inputPath)
    freshCount = 0
    for food in foodsIds:
        # print(f"Checking food {food}")
        if (checkFreshnes(food, freshRanges)):
            freshCount += 1
    print(f"There are {freshCount} fresh foods")
    return freshCount

def doExercie2(inputPath):
    freshRanges, _ = parseInput(inputPath)
    freshRanges.sort(key = lambda range: range[0])
    last = 0
    for range in freshRanges:
        print(range[0])
        assert range[0] >= last
        last = range[0]
        # sif range[1] > maxNum:
        #     maxNum = range[1]
    
    # print("The maximum number is: ", maxNum)
    
def tests():
    assert checkInRange(1, (1 ,2)) == True
    assert checkInRange(2, (1 ,2)) == True
    assert checkInRange(0, (1 ,2)) == False
    assert checkInRange(3, (1 ,2)) == False
    assert doExercie1(basicInputPath) == 3
    print("ALL TESTS PASSED")

tests()
doExercie1(inputPath)
doExercie2(inputPath)