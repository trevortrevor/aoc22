import numpy as np
testing = False

if testing:
    infile = './input/day8test.txt'
else:
    infile = './input/day8.txt'
    
def genMatrix(infile):
    with open(infile) as f:
        return np.array([[int(x) for x in list(line.strip())] for line in f.readlines()])
        
treematrix = genMatrix(infile)
treematrix = np.pad(treematrix, [0,0])
print(treematrix)

boolmatrix = np.zeros_like(treematrix)

def findVisible(array):
    height = -1
    output = []
    for x in array:
        if x > height:
            output.append(True)
            height = x
        else:
            output.append(False)
    return output

def matrixRows(matrix):
    return np.vsplit(matrix, len(matrix))
    
def directions(matrix, output):
    for k in range(4):
        yield np.rot90(matrix, k), np.rot90(output, k)
        
def solveP1(matrix, output):
    outMat = output
    for k in range(4):
        rotation = np.rot90(matrix, k)
        interMat = np.array([findVisible(np.ravel(row)) for row in matrixRows(rotation)])
        #print(np.rot90(interMat,(4-k)))
        #print(f"Intermat: {k}\n")
        outMat = np.logical_or(outMat, np.rot90(interMat, (4-k)))
        #print(outMat)
        #print(f"OutputMat: {k}\n")
    return outMat

p1result = solveP1(treematrix, boolmatrix)
print(p1result)
print(np.count_nonzero(p1result))

def scenicScore(treematrix, pos, dir):
    blocked = False
    score = 0
    y, x = pos
    nextY, nextX = pos
    treeheight = treematrix[y][x]
    maxY, maxX = np.shape(treematrix)
    #print(f"Testing tree at y:{y}, x:{x} = {treeheight}")
    while not blocked:
        nextX += dir[1]
        nextY += dir[0]
        if nextX < 0 or nextY < 0:
            blocked = True
        elif nextX == maxX or nextY == maxY:
            blocked = True
        elif treematrix[nextY][nextX] >= treeheight:
            score += 1
            blocked = True
        else:
            score += 1
            #print(f"Tree at y:{nextY}, x:{nextX} = {treematrix[nextY][nextX]}")
    return score


directions = [(0,1),(0,-1),(1,0),(-1,0)]

scenicScores = np.ones_like(treematrix)
it = np.nditer(treematrix, flags=['multi_index'])
maxScore = 0
for i in it:
    y, x = it.multi_index
    print(f"Tree: {i} at index: {it.multi_index}")
    for dir in directions:
        scenicScores[y][x] *= scenicScore(treematrix, (y, x), dir)
    maxScore = max(maxScore, scenicScores[y][x])
    print(maxScore)
        

print(scenicScores)
print(maxScore)