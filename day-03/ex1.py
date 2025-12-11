
from enum import Enum

basicInputPath = "input/basic_input_1.txt"
inputPath = "input/input_1.txt"

def parseInput(input):
    parsed = []
    with open(input)as inp:
        for line in inp:
            line = line.replace('\n', '')
            parsed.append([int(batery) for batery in line])
    return parsed

def doExercice1(input):
    bateryBanks = parseInput(input)
    sum = 0
    for bank in bateryBanks:
        maxBatery = 0
        for batery in range(1, len(bank) - 1):
            if bank[batery] > bank[maxBatery]:
                maxBatery = batery
        bateriesAdition =  f"{bank[maxBatery]}"
        maxBatery += 1
        for batery in range(maxBatery, len(bank)):
            if bank[batery] > bank[maxBatery]:
                maxBatery = batery
        bateriesAdition += str(bank[maxBatery])
        sum += int(bateriesAdition)
    print(f"The bateries sum is: {sum}")
    return sum

def doExercice2(input, bankSize):
    bateryBanks = parseInput(input)
    sum = 0
    for bank in bateryBanks:
        # print(bank)
        maxBatery = 0
        bateriesAdition = ""
        for iteration in range(bankSize):
            for batery in range(maxBatery, len(bank) - bankSize + iteration + 1):
                if bank[batery] > bank[maxBatery]:
                    maxBatery = batery
            bateriesAdition += str(bank[maxBatery])
            # print("  ", maxBatery, bateriesAdition, end = "")
            maxBatery += 1
            # print("  |  ", maxBatery, bateriesAdition)
        sum += int(bateriesAdition)
    print(f"The bateries sum is: {sum}")
    return sum

def tests():
    assert doExercice1(basicInputPath) == 357
    assert doExercice1(inputPath) == 17613
    assert doExercice2(basicInputPath, 2) == 357
    assert doExercice2(inputPath, 2) == 17613
    assert doExercice2(basicInputPath, 12) ==3121910778619
    # assert doExercice2(inputPath, 12) == 17613

tests()
print("Exercice 1")
doExercice1(inputPath)
print("Exercice 2")
doExercice2(inputPath, 12)