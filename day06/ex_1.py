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
            line = line.split(" ")
            line = [l for l in line if l != ""]
            worksheet.append(line)
    problems = []
    for line in  worksheet[:-1]:
        problems.append([int(num) for num in line])
    return problems, worksheet[-1]
        
def doProblem(problemColumn, problemMatrix, problemsOperations):
    operationSimbol = problemsOperations[problemColumn]
    if (operationSimbol == SUM_REPR):
        result = 0
    elif (operationSimbol == MULT_REPR):
        result = 1
    operation = OPERATIONS[operationSimbol]
    for num in range(len(problemMatrix)):
        result = operation(result, problemMatrix[num][problemColumn])
    return result

def doExercie1(input):
    problemsMatrix, problemsOperations = parseInput(input)
    result = 0
    for problem in range(len(problemsMatrix[0])):
        result += doProblem(problem, problemsMatrix, problemsOperations)
    return result

    # print("problemsMatrix")
    # print(problemsMatrix)
    # print("problemsOperations")
    # print(problemsOperations)

def doExercie2(inputPath):
    pass

def tests():
    problemsMatrix, problemsOperations = parseInput(basicInputPath)
    assert doProblem(0, problemsMatrix, problemsOperations) == 33210
    assert doProblem(1, problemsMatrix, problemsOperations) == 490
    assert doProblem(2, problemsMatrix, problemsOperations) == 4243455
    assert doProblem(3, problemsMatrix, problemsOperations) == 401
    assert doExercie1(basicInputPath) == 4277556
    assert doExercie1(inputPath) == 6757749566978
    print("ALL TESTS PASSED")

tests()
print("EXERCICE 1")
result = doExercie1(inputPath)
print(f"The sum of the problems results is {result}")
#print("EXERCICE 2")
#result = doExercie2(inputPath)
#print(f"There are total of {result} fresh items")