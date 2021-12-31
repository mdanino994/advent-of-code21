import string
import copy
import sys
import os
from queue import PriorityQueue
os.chdir(os.path.dirname(__file__))

#lines = open('example.txt').read().splitlines()
#lines = open('example2.txt').read().splitlines()
lines = open('input.txt').read().splitlines()


class chiton:
    def __init__(self, risk, totalRisk):
        self.risk = risk # cost
        self.totalRisk = totalRisk # g score
        self.closed = False
    def __repr__(self):
        return self.risk
    def __str__(self):
        return self.risk
    

chitonArr = []
inf = sys.maxsize

for line in lines:
    tempArr = [int(i) for i in line.strip()]
    chitonArr.append(tempArr)

def printRisk():    
    for i in range(len(chitonArr)):
        for j in range(len(chitonArr[i])):
            print(chitonArr[i][j], end="")
        print()

def printTotalRisk():    
    for i in range(len(chitonArr)):
        for j in range(len(chitonArr[i])):
            print(chitonArr[i][j].totalRisk, end="")
        print()

def h(pos, end):
    x1, y1 = pos
    x2, y2 = end
    return abs(x1 - x2) + abs(y1 - y2)

# A Star alg based on https://www.youtube.com/watch?v=JtiK0DOeI4A
def AStar(start, end):
    global chitonArr
    count = 0
    openSet = PriorityQueue()
    openSet.put((0, count, start))
    gScore = {}
    fScore = {}
    gScore = {tuple((row, col)) : inf for row in range(len(chitonArr)) for col in range(len(chitonArr[0]))}
    fScore = {tuple((row, col)) : inf for row in range(len(chitonArr)) for col in range(len(chitonArr[0]))}
    offsets = ((1, 0), (-1, 0), (0, 1), (0, -1))
    gScore[start] = 0
    fScore[start] = h(start, end)
    openSetHash = {start}
    came_from = {}
    while not openSet.empty():
        current = openSet.get()[2]
        openSetHash.remove(current)
        if current == end:
            return gScore[current]
            
        for offset in offsets:
            neighbor = (current[0] + offset[0], current[1] + offset[1])
            #print("offset: " + str(offset))
            #print("curr pos: " + str(current))
            #print("neighbor: " + str(neighbor))
            if 0 <= neighbor[0] < len(chitonArr) and 0 <= neighbor[1] < len(chitonArr[0]):
                #print("entering check")
                tempGScore = gScore[current] + chitonArr[neighbor[0]][neighbor[1]]
                if tempGScore < gScore[neighbor]:
                    came_from[neighbor] = current
                    gScore[neighbor] = tempGScore
                    fScore[neighbor] = tempGScore + h(neighbor, end)
                    if neighbor not in openSetHash:
                        count += 1
                        openSet.put((fScore[neighbor], count, neighbor))
                        openSetHash.add(neighbor)
            

def extendCave():
    global chitonArr
    origWidth = len(chitonArr[0])
    origHeight = len(chitonArr)
    
    for i in range(4):
        for line in chitonArr:
            startingWidth = origWidth * i
            extendedPart = [x % 9 + 1 for x in line[startingWidth:]]
            line.extend(extendedPart)
        for line in chitonArr[origHeight * i: origHeight * (i + 1)]:
            line = [x % 9 + 1 for x in line]
            chitonArr.append(line)
    
startPos = (0, 0)    
endPos = (len(chitonArr) - 1, len(chitonArr[0]) - 1)

print(AStar(startPos, endPos))
#printRisk()
print()
extendCave()
#printRisk()
print()
endPos = (len(chitonArr) - 1, len(chitonArr[0]) - 1)
print(AStar(startPos, endPos))

#printTotalRisk()
print()
#print("inf: " + str(inf))
input()

