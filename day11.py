import operator
from collections import deque
import math
testing = False

if testing:
    infile = "./input/day11test.txt"
else:
    infile = "./input/day11.txt"
    
    
ops = {
    '+' : operator.add,
    '*' : operator.mul,
}
class Monkey():
    def __init__(self, id:int):
        self.id = id
        self.items = deque()
        self.operand = "+"
        self.opConst = 0
        self.divisor = 0
        self.trueMonkey = 0
        self.falseMonkey = 0
        self.inspections = 0
        
    def addItem(self, item):
        self.items.append(item)
        return self.items
        
    def inspect(self, item) -> int:
        self.inspections += 1
        if self.opConst == 'old':
            opConst = item.worry
            #opConst = 1
            #if opConst % 13 == 0:
            #    opConst = 13
        else:
            opConst = int(self.opConst)
        item.worry = ops[self.operand](item.worry, opConst)
        return item
    
    def getConst(self):
        if self.opConst == 'old':
            return self.items[-1].worry
        else:
            return int(self.opConst)
        
    def test(self, item):
        if item.worry % self.divisor == 0:
            return self.trueMonkey, item
        else:
            return self.falseMonkey, item
        
    def throw(self):
        return self.items.pop()
    
    def catch(self, item):
        self.items.append(item)
   
class MonkeyItem():
    def __init__(self, worry:int):
        self.worry = worry     
        
def parseFile(text):
    monkeys = {}
    with open(infile) as f:
        for line in f.readlines():
            line = line.split()
            if line == []:
                pass
            elif line[0] == 'Monkey':
                monkeyID = int(line[1].strip(':'))
                monkeys[monkeyID] = Monkey(monkeyID)
            elif line[0] == 'Starting':
                monkeys[monkeyID].items = deque([MonkeyItem(int(x.strip(','))) for x in line[2:]])
            elif line[0] == 'Operation:':
                monkeys[monkeyID].opConst = line[5]
                monkeys[monkeyID].operand = line[4]
            elif line[0] == 'Test:':
                monkeys[monkeyID].divisor = int(line[-1])
            elif line[1] == 'true:':
                monkeys[monkeyID].trueMonkey = int(line[-1])
            elif line[1] == 'false:':
                monkeys[monkeyID].falseMonkey = int(line[-1])
    return monkeys            
              
monkeys = parseFile(infile)

def decWorry(item:MonkeyItem, divisor=3):
    item.worry = item.worry // divisor
    return item
    
def worryFactor(monkeys:dict):
    divisors = []
    for monkey in monkeys.values():
        divisors.append(monkey.divisor)
    factor = math.prod(divisors)
    for monkey in monkeys.values():
        for item in monkey.items:
            item.worry = item.worry % factor  
    return monkeys
    

def p1Loop(cycles):
    for cycle in range(cycles):
        for id, monkey in monkeys.items():
            for i in range(len(monkey.items)):
                item = monkey.items.popleft()
                item = monkey.inspect(item)
                item = decWorry(item)
                result, item = monkey.test(item)
                monkeys[result].catch(item)
        
p1Loop(20)
for monkey in monkeys.values():
    print(f"{monkey.id} : {monkey.inspections}")
    
def monkeyBusiness(monkeys=monkeys):
    inspections = [x.inspections for x in monkeys.values()]
    inspections.sort()
    print(inspections)
    print(f"Part 1: {inspections[-1]*inspections[-2]}")

monkeyBusiness()

def p2Loop(cycles, monkeys):
    for cycle in range(cycles):
        monkeys = worryFactor(monkeys)
        for id, monkey in monkeys.items():
            for i in range(len(monkey.items)):
                item = monkey.items.popleft()
                item = monkey.inspect(item)
                item = decWorry(item, 1)
                result, item = monkey.test(item)
                monkeys[result].catch(item)
monkeys = parseFile(infile)
p2Loop(10000, monkeys)    
        
for monkey in monkeys.values():
    print(f"{monkey.id} : {monkey.inspections}")
    
def monkeyBusiness(monkeys=monkeys):
    inspections = [x.inspections for x in monkeys.values()]
    inspections.sort()
    return inspections

result = monkeyBusiness()
print(f"Part 2: {result[-1] * result[-2]}")



                
                    
