from common import inputLine

testing = False

if testing:
    infile = "./input/day4test.txt"
else:
    infile = "./input/day4.txt"
 
elves = []

def parseElf(elfString:str) -> range:
    elfString = elfString.split("-")
    return set(range(int(elfString[0]), int(elfString[-1]) + 1))

for line in inputLine(infile):
    elf1, elf2 = line.split(",")
    elf1 = parseElf(elf1)
    elf2 = parseElf(elf2)
    elves.append((elf1, elf2))


def elfSubset(elves):
    p1total = 0
    for elfPair in elves:
        if elfPair[0].issubset(elfPair[1]) or elfPair[1].issubset(elfPair[0]):
            p1total +=1
    return p1total
print(f"Part 1: {elfSubset(elves)}")
    
def elfIntersection(elves):
    p2total = 0
    for elfPair in elves:
        if not elfPair[0].isdisjoint(elfPair[1]):
            p2total +=1
    return p2total

print(f"Part 2: {elfIntersection(elves)}")
