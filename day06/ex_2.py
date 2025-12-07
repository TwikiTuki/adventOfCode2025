basicInputPath = 'input/basicInput.txt'
inputPath = 'input/input.txt'

SUM_REPR = "+"
MULT_REPR = "*"
sum = lambda a,b: a + b 
multiplication = lambda a,b: a * b 
OPERATIONS = {SUM_REPR: sum, MULT_REPR: multiplication}

def parseInput(input):
    worksheet = []
    with open(input) as file:
        for line in file:
            line = line.replace("\n", "")
            worksheet.append(line)
    return worksheet[0:-1], worksheet[-1]

def flattenNumber(column, problemsMatrix):
    initialRow = 0
    while(problemsMatrix[initialRow][column] == " "):
        initialRow += 1
        if (initialRow == len(problemsMatrix)):
            return None
    number = ""
    for r in range(initialRow, len(problemsMatrix)):
        number = number + problemsMatrix[r][column]
    return int(number)
        
def doExercie2(inputPath):
    problemsMatrix, problemsOperations = parseInput(inputPath)
    total = 0
    problemResult = 0
    for c in range(len(problemsMatrix[0])):
        currentNumber = flattenNumber(c, problemsMatrix)
        if (currentNumber == None):
            total += problemResult
            problemResult = 0 ## Not needed but this way should handle mutiple column separation
            continue
        op = problemsOperations[c]
        if (op != " "):
            operation = OPERATIONS[op]
            if (op == '+'):
                problemResult = 0
            elif (op == '*'):
                problemResult = 1
        problemResult = operation(problemResult, currentNumber)
    if (currentNumber != None):
        total += problemResult
    return total

def tests():
    problemsMatrix, problemsOperations = parseInput(basicInputPath)
    assert doExercie2(basicInputPath) == 3263827
    assert doExercie2(inputPath) == 10603075273949
    print("ALL TESTS PASSED")

tests()
print("EXERCICE 2")
result = doExercie2(inputPath)
print(f"The sum of the problems results is {result}")
