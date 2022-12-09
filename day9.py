import numpy as np

testing = False

if testing:
    infile = "./input/day9test.txt"
else:
    infile = "./input/day9.txt"
    
def moveGenerator(infile):
    with open(infile) as f:
        for line in f.readlines():
            line = line.strip()
            direction, steps = line.split()
            yield parseDirection(direction), int(steps)
        
def parseDirection(dir:str) -> tuple:
    if dir == "R":
        return np.array([0, 1])
    elif dir == "L":
        return np.array([0, -1])
    elif dir == "U":
        return np.array([-1, 0])
    elif dir == "D":
        return np.array([1, 0])
    
def moveHead(headPos:np.ndarray, direction:np.ndarray):
    return headPos + direction

def moveKnot(headPos:np.ndarray, knotPos:np.ndarray):
    moveVector = (np.greater(abs(headPos - knotPos), 1))
    if np.any(moveVector):
        moveVector = np.sign(headPos - knotPos)
        return knotPos + moveVector
    else:
        return knotPos
    
def mainLoop(knots = 2):
    rope = [np.array([0,0]) for i in range(knots)]
    headHistory = [tuple(rope[0])]
    tailHistory = [tuple(rope[-1])]
    for direction, steps in moveGenerator(infile):
        for _ in range(steps):
            rope[0] = moveHead(rope[0], direction)
            headHistory.append((tuple(rope[0])))
            for i, knotPos in enumerate(rope[1:], 1):
                rope[i] = moveKnot(rope[i-1], rope[i])
            tailHistory.append((tuple(rope[-1])))
    print(rope)
    return set(tailHistory)
tailHistory = mainLoop()

print(tailHistory)
print(f"Part 1 - Points visited by tail = {len(tailHistory)}")

tailHistory = mainLoop(10)
print(f"Part 2 - Points visited by tail = {len(tailHistory)}")

            
