from common import *
import math
testmode = False
inlist = txt2list("./input/day1.txt")
if testmode:
    inlist = txt2list("./input/day1test.txt")
inlist = [int(x) for x in inlist]


def part1(inlist) -> int:
    output = []
    for i, value in enumerate(inlist[1:]):
        output.append(value > inlist[i])
    return output.count(True)

def part2(inlist) -> int:
    outlist = []
    for i in range(len(inlist)-2):
        range1 = sum(inlist[i:i+3])
        outlist.append(range1)
    print(outlist)
    return outlist
        
print(f"Part 1: {part1(inlist)}")
print(f"Part 2: {part1(part2(inlist))}")

            



