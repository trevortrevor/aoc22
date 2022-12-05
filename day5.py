testing = False
import re
from common import inputLine
from collections import deque

if testing:
    infile = "./input/day5test.txt"
else:
    infile = "./input/day5.txt"


def parseMove(move:list, stacks):
    for _ in range(int(move[1])):
        stacks[int(move[5])].append(stacks[int(move[3])].pop())
        
    

def initStacks(stacklist:list):
    stacks = {}
    for elem in stacklist[-1]:
        if elem != '':
            stacks[int(elem)] = deque()
    for elem in reversed(stacklist[0:-1]):
        for column, val in enumerate(elem):
            if val != '   ':
                stacks[int(column + 1)].append(val)
    return stacks


moves = []
stacks = []  
for line in inputLine(infile):
    if len(line) == 0:
        continue
    elif line[0] == 'm':
        moves.append(re.split("[\s*]+", line))
    else:
        line += " "
        stacks.append(re.findall("(.{3})\s", line))
        
stacks = initStacks(stacks)
    
def part1(moves, stacks):
    p1Result = []
    for move in moves:
        parseMove(move, stacks)
    for stack in stacks.values():
        p1Result.append(stack[-1].strip("[]"))
    return ''.join(p1Result)

print(part1(moves, stacks))

def parseMove2(move, stacks):
    interim = []
    for _ in range(int(move[1])):
        interim.append(stacks[int(move[3])].pop())
    for i in range(len(interim)):
        stacks[int(move[5])].append(interim.pop())
        


def part2(moves, stacks):
    p2Result = []
    for move in moves:
        parseMove2(move, stacks)
    for stack in stacks.values():
        p2Result.append(stack[-1].strip("[]"))
    return ''.join(p2Result) 

moves = []
stacks = []  
for line in inputLine(infile):
    if len(line) == 0:
        continue
    elif line[0] == 'm':
        moves.append(re.split("[\s*]+", line))
    else:
        line += " "
        stacks.append(re.findall("(.{3})\s", line))
        
stacks = initStacks(stacks)

print(part2(moves,stacks))  
        