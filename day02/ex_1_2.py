basicInputPath = 'input/basicInput.txt'
inputPath = 'input/input.txt'

def strArrToNumArr(arr):
    arr = [int(n) for n in arr]
    return arr

def parseInput(input):
    with open(input) as file:
        text = file.read()
    ranges = text.split(',') 
    ranges = [strArrToNumArr(r.split('-')) for r in ranges]
    return ranges

def fixSplit(str, ln):
    res = []
    # for i in range(int(len(str)/ln)):
    i = 0
    while (i < len(str)):
        res.append(str[i : i+ln])
        i += ln
    return res

def checkNumber(number):
    number = str(number)
    ln = len(number)
    if (ln % 2 != 0):
        return True 
    midle = int(ln/2)
    left = number[0:midle]
    right = number[midle:]
    # print("splited: ", left, right)
    return left != right

def checkNumberFixedLen(number, ln):
    number = str(number)
    if (len(number) % ln != 0):
        return True
    splited = fixSplit(number, ln)
    # print("splited: ", splited)
    for number in splited:
        if number != splited[0]:
            return True
    return False


def checkNumberMultipleRepeats(number):
    for i in range(1, len(str(number))): 
        if (not checkNumberFixedLen(number, i)):
            return False
    return True

def doExercice(inputPath, check):
    ranges = parseInput(inputPath)
    # print("Ranges are: ", ranges)
    invalidNumbersSum = 0
    for rang in ranges:
        # print('==================')
        for i in range(rang[0], rang[1] + 1):
            if (not check(i)):
                # print("invalid: ", i)
                invalidNumbersSum += i
    return invalidNumbersSum

def doExercice1(inputPath):
    return doExercice(inputPath, checkNumber)

def doExercice2(inputPath):
    return doExercice(inputPath, checkNumberMultipleRepeats)
    
def executeTest(value, expected):
    if (value != expected):
        raise Exception(f"Expected {expected} but got {value}")

def tests():
    executeTest(checkNumber(11221122), False)
    executeTest(checkNumber(112211223), True)
    executeTest(checkNumber(11221123), True)
    executeTest(checkNumber(0), True)
    executeTest(checkNumber(1), True)
    executeTest(doExercice1(basicInputPath), 1227775554)
    executeTest(doExercice1(inputPath), 64215794229)
    executeTest(checkNumberFixedLen(123123, 3), False)
    executeTest(checkNumberFixedLen(123123, 2), True)
    executeTest(checkNumberFixedLen(123123, 4), True)
    executeTest(doExercice2(basicInputPath), 4174379265)
    executeTest(doExercice2(inputPath), 85513235135)
    print("ALL TESTS PASSED")

tests()
print("EXERCICE 1")
result = doExercice1(inputPath)
print(f"The sum of invalid ids is: {result}")
print("EXERCICE 2")
result = doExercice2(inputPath)
print(f"There are total of {result} fresh items")
# print(fixSplit("123123123", 3))
# print(fixSplit("12312312", 2))
# print(fixSplit("12312312", 4))