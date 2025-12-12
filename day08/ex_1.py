import math
import heapq

basicInputPath = 'input/basicInput.txt'
inputPath = 'input/input.txt'

ENTRY_LOCATION = 'S'
EMPTY_SPACE = '.'
SPLITER = '^'
BEAM = '|'

class Point3():
    nextId = 0
    @classmethod
    def distance(clazz, A, B):
        result = 0
        for a, b in zip(A.toList(), B.toList()):
            result += (a - b) ** 2
        result = math.sqrt(result)
        result = abs(result)
        return result

    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.id = Point3.nextId
        Point3.nextId += 1

    def toList(self):
        return [self.x, self.y, self.z]

    def __eq__(self, other):
        # return self.x == other.x and self.y == other.y and self.z == other.z
        return self.id == other.id
    
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"

def pointTests():
    a =  Point3(1, 1, 1)
    b =  Point3(2, 2, 2)
    distance = int(Point3.distance(a, b) * 1000)
    print(f"The distance between {a}, {b} is {distance} /1000")
    assert(distance ==  1732)
    
def parseInput(input):
    junctionBoxes = []
    with open(input) as file:
        for line in file:
            line = line.replace('\n', '')
            line = line.split(',')
            junctionBoxes.append(Point3(*line))
    return junctionBoxes

class Connection():
    def __init__(self, p1, p2):
        assert p1 != p2
        if (p1.id > p2.id):
            p1, p2 = p2, p1
        self.p1 = p1
        self.p2 = p2
        self.distance = Point3.distance(p1, p2)
    
    def __str__(self):
        return f"{str(self.p1)}->{str(self.p2)}"
    
    def __repr__(self):
        return f"{self.p1}->{self.p2}"
    
    def __eq__(self, other):
        return self.distance == other.distance
    
    def __lt__(self, other):
        return self.distance < other.distance

class JunctionBox():
    def __init__(self, position):
        self.position = position
        self.connected = []
        self.id = position.id
    
    def __str__(self):
        return f"{self.position}"
    
    def __repr__(self):
        return f"{self.position}"

def connectionTests():
    con1 = Connection(Point3(1,2,3), Point3(2,3,4))
    con2 = Connection(Point3(2,3,4), Point3(3,4,5))
    assert con1 == con2
    con3 = Connection(Point3(0,0,0), Point3(3,4,5))
    assert con1 < con3
    assert con3 > con2
    assert con2 != con3

def createCircuit(box, boxesDict, circuit=[]):
    if (len(boxesDict) == 0) : return circuit
    if (box == None):
        # box = next(iter(boxesDict.values()))
        box = list(boxesDict.values())[0]
        assert box != None
        boxesDict.pop(box.id)
    for connectedBoxId in box.connected:
        connectedBox = boxesDict.pop(connectedBoxId, None)
        if (box != None):
            circuit.append(box)
            createCircuit(connectedBox, boxesDict, circuit)
    return circuit
        
def doExercie1(input):
    junctionBoxes = parseInput(input)
    for box in junctionBoxes:
        print("box: ", box)

    connections = []
    for i in range(len(junctionBoxes)):
        newConnections = []
        for j in range(i + 1, len(junctionBoxes)):
            newConnections.append(Connection(junctionBoxes[i], junctionBoxes[j]))
        newConnections.sort()
        connections = list(heapq.merge(connections, newConnections)) # TODO could be more eficient it is creating a list out of the returned iterator. Ideally sholuld work with the iterator
        if (len(connections) > 1000):
            connections[1000:] = []
    for conn in connections[:10]:
        print(conn)
    topConnections = connections[10:]
    junctionBoxesDict = {j.id: JunctionBox(j) for j in junctionBoxes}
    for con in topConnections:
        junctionBoxesDict[con.p1.id].connected.append(con.p2.id)
        junctionBoxesDict[con.p2.id].connected.append(con.p1.id)
    
    print("--------------")
    circuits = []
    while(len(junctionBoxesDict) > 0):
        print("junctionBoxes: ", junctionBoxesDict.keys())
        circuits.append(createCircuit(None, junctionBoxesDict, []))
    for circuit in circuits:
        print(f"{len(circuit)}: {circuit}")



def doExercie2(inputPath):
    pass

def executeTest(value, expected):
    if (value != expected):
        raise Exception(f"Expected {expected} but got {value}")
def tests():
    # assert doExercie1(basicInputPath) == 4277556
    # assert doExercie1(inputPath) == 6757749566978
    # executeTest(doExercie1(basicInputPath), 21)
    pointTests()
    connectionTests()
    print("ALL TESTS PASSED")

tests()
print("EXERCICE 1")
result = doExercie1(basicInputPath)
# result = doExercie1(inputPath)
# print(f"The result of exercice 1 is: {result}")
#print("EXERCICE 2")
#result = doExercie2(inputPath)
#print(f"There are total of {result} fresh items")