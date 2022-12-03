import string
testing = False

if testing:
    infile = "./input/day3test.txt"
else:
    infile = "./input/day3.txt"
    
def genValues():
    priorities = {}
    for val, char in enumerate(string.ascii_letters):
        priorities[char] = val + 1 
    return priorities

priorities = genValues()

def inputLine(infile):
    with open(infile) as f:
        for line in f.readlines():
            yield line.strip("\n")
            
class Compartment(set):
    pass
                
class Rucksack():
    def __init__(self):
        self.comp0 = Compartment()
        self.comp1 = Compartment()
        self.compartments = [self.comp0, self.comp1]
        self.dupes = set()
        self.dupeValue = 0
        
    def splitLine(self, line:str):
        lineaslist = list(line)
        noItems = len(lineaslist) // 2 
        return [set(lineaslist[:noItems]), set(lineaslist[noItems:])] 
    
    def addLine(self, line:str):
        self.comp0, self.comp1 = self.splitLine(line)
        self.allItems = self.comp0 | self.comp1  
        
    def findDupes(self):
        for item in self.comp0:
            if item in self.comp1:
                self.dupes.add(item)
    
    def getDupeValue(self):
        for item in self.dupes:
            self.dupeValue += priorities[item] 
        return self.dupeValue
    
           
rucksacks = []       
for line in inputLine(infile):
    currentSack = Rucksack()
    currentSack.addLine(line)
    currentSack.findDupes()
    currentSack.getDupeValue()
    rucksacks.append(currentSack)
    
p1Total = 0
for sack in rucksacks:
    print(f"Dupe: {sack.dupes}, value: {sack.dupeValue}")
    p1Total += sack.dupeValue
    
print(f"Part 1: {p1Total}")
    
def findCommonItem(listOfSacks:list):

    return listOfSacks[0].allItems.intersection(listOfSacks[1].allItems,listOfSacks[2].allItems)
    
badges = []   
for i in range(len(rucksacks)//3):
    badges.append(findCommonItem(rucksacks[3*i:3*i+3]))
    

p2Total = 0
for badge in badges:
    badge = badge.pop()
    print(f"Badge: {badge}, Priority {priorities[badge]}")
    p2Total += priorities[badge]
    
print(f"Part 2: {p2Total}")