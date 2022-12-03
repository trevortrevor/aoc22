test = False

class Elf():
    def __init__(self, calList:list):
        self.calList = calList
        self._totalCals = sum(self.calList)
    
    @property
    def totalCals(self):
        return self._totalCals
    
testInput = "./input/day1test.txt"
realInput = "./input/day1.txt"
def openFile(input:str) -> list:
    with open(input, 'r') as f:
        return f.readlines()

if test:
    input = testInput
else:
    input = realInput
    
calList = [x.strip("\n") for x in openFile(input)]

def parseList(calList:list) -> list:
    cals = []
    elves = []
    for val in calList:
        if val != "":
            cals.append(int(val))
        else:
            elves.append(Elf(cals))
            cals = []
    elves.append(Elf(cals))
    return elves

def findMaxElf(elves:list):
    totals = [x.totalCals for x in elves]
    return max(totals)
    
    
elves = parseList(calList)
print(findMaxElf(elves))

def findTopThree(elves:list):
    totals = [x.totalCals for x in elves]
    totals.sort(reverse=True)
    return totals[:3]

print(f"Part 2: {sum(findTopThree(elves))}")


    