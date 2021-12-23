import string
import os
os.chdir(os.path.dirname(__file__))

lines = open('input.txt').read().splitlines()
heightMap = []
lowPoints = []
basinSizes = []


for line in lines:
    lineArr = []
    for obj in line:
        lineArr.append(int(obj))
    heightMap.append(lineArr)


def checkUp(y, x):
    return heightMap[y][x] < heightMap[y - 1][x]

def checkLeft(y,x):
    return heightMap[y][x] < heightMap[y][x - 1]

def checkRight(y,x):
    return heightMap[y][x] < heightMap[y][x + 1]

def checkDown(y,x):
    return heightMap[y][x] < heightMap[y + 1][x]

def getRisk():
    risk = 0
    for y in range(len(heightMap)):
        for x in range(len(heightMap[y])):
            if y == 0:
                if x == 0: # top left
                    if checkDown(y, x) and checkRight(y, x):
                        risk += heightMap[y][x] + 1
                        lowPoints.append((x, y))
                elif x == len(heightMap[y]) - 1: # top right
                    if checkDown(y, x) and checkLeft(y, x):
                        risk += heightMap[y][x] + 1
                        lowPoints.append((x, y))
                else: # top edge
                    if checkDown(y, x) and checkLeft(y, x) and checkRight(y, x):
                        risk += heightMap[y][x] + 1
                        lowPoints.append((x, y))
            elif y == len(heightMap) - 1:
                if x == 0: # bottom left
                    if checkUp(y, x) and checkRight(y, x):
                        risk += heightMap[y][x] + 1
                        lowPoints.append((x, y))
                elif x == len(heightMap[y]) - 1: # bottom right
                    if checkUp(y, x) and checkLeft(y, x):
                        risk += heightMap[y][x] + 1
                        lowPoints.append((x, y))
                else: # bottom edge
                    if checkUp(y, x) and checkLeft(y, x) and checkRight(y, x):
                        risk += heightMap[y][x] + 1
                        lowPoints.append((x, y))
            elif x == 0: # left edge
                if checkUp(y, x) and checkDown(y, x) and checkRight(y, x):
                        risk += heightMap[y][x] + 1
                        lowPoints.append((x, y))
            elif x == len(heightMap[y]) - 1: # right edge
                if checkUp(y, x) and checkDown(y, x) and checkLeft(y, x):
                        risk += heightMap[y][x] + 1
                        lowPoints.append((x, y))
            else: # somewhere in the center
                if checkUp(y, x) and checkDown(y, x) and checkLeft(y, x) and checkRight(y, x):
                        risk += heightMap[y][x] + 1
                        lowPoints.append((x, y))
    print(risk)

def findBasins():
    for lowPoint in lowPoints:
        x = lowPoint[0]
        y = lowPoint[1]
        basinSize = traverseBasin(y, x)
        
        if basinSize > 0:
            basinSizes.append(basinSize)

def traverseBasin(y, x):
    #print("x: " + str(x) + " y: " + str(y))
        
    if heightMap[y][x] == -1 or heightMap[y][x] == 9:
        #print("hit -1 or 9, returning")
        return 0
    
    heightMap[y][x] = -1
    basinSize = 1
    if y == 0:
        if x == 0: # top left, traverse down and right
            #print("topleft")
            basinSize += traverseBasin(y + 1, x) # traverse down
            basinSize += traverseBasin(y, x + 1) # traverse right
                
        elif x == len(heightMap[y]) - 1: # top right, traverse down and left
            #print("topright")
            basinSize += traverseBasin(y + 1, x) # traverse down
            basinSize += traverseBasin(y, x - 1) # traverse left
                
        else: # top edge, traverse down, left and right
            #print("top")
            basinSize += traverseBasin(y + 1, x) # traverse down
            basinSize += traverseBasin(y, x - 1) # traverse left
            basinSize += traverseBasin(y, x + 1) # traverse right
                
    elif y == len(heightMap) - 1:
        if x == 0: # bottom left, traverse up and right
            #print("botleft")
            basinSize += traverseBasin(y - 1, x) # traverse up
            basinSize += traverseBasin(y, x + 1) # traverse right
                
        elif x == len(heightMap[y]) - 1: # bottom right, traverse up and left
            #print("botright")
            basinSize += traverseBasin(y - 1, x) # traverse up
            basinSize += traverseBasin(y, x - 1) # traverse left
                
        else: # bottom edge, traverse up, left and right
            #print("bot")
            basinSize += traverseBasin(y - 1, x) # traverse up
            basinSize += traverseBasin(y, x - 1) # traverse left
            basinSize += traverseBasin(y, x + 1) # traverse right
                
    elif x == 0: # left edge, traverse right, up and down
        #print("left")
        basinSize += traverseBasin(y - 1, x) # traverse up
        basinSize += traverseBasin(y + 1, x) # traverse down
        basinSize += traverseBasin(y, x + 1) # traverse right
                
    elif x == len(heightMap[y]) - 1: # right edge, traverse left, up and down
        #print("right")
        basinSize += traverseBasin(y - 1, x) # traverse up
        basinSize += traverseBasin(y + 1, x) # traverse down
        basinSize += traverseBasin(y, x - 1) # traverse left
                
    else: # somewhere in the center, traverse in all directions
        #print("mid")
        basinSize += traverseBasin(y - 1, x) # traverse up
        basinSize += traverseBasin(y + 1, x) # traverse down
        basinSize += traverseBasin(y, x - 1) # traverse left
        basinSize += traverseBasin(y, x + 1) # traverse right
        
    return basinSize

getRisk()
findBasins()
basinSizes.sort()
basinLen = len(basinSizes)

largestBasins = 1
for i in range(basinLen - 3, basinLen):
    largestBasins *= basinSizes[i]
print(largestBasins)