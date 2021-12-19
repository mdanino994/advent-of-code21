import string
import os
os.chdir(os.path.dirname(__file__))

xData = []
yData = []
xMax = 0
yMax = 0
lines = open('input.txt').read().splitlines()
#get max x/y vals

def printDiag():
    for row in diagArr:
        for elem in row:
            if elem > 0:
                print(elem, end='')
            else:
                print(".", end='')
        print()

for line in lines:
    modData = line.replace(' -> ', ',').split(',')
    xData.append(int(modData[0]))
    yData.append(int(modData[1]))
    xData.append(int(modData[2]))
    yData.append(int(modData[3]))
    
xMax = max(xData) + 1
yMax = max(yData) + 1


diagArr = [[0] * xMax for _ in range(yMax)]

def findVents():
    for line in lines:
        modData = line.replace(' -> ', ',').split(',')
        x1 = int(modData[0])
        y1 = int(modData[1])
        x2 = int(modData[2])
        y2 = int(modData[3])
        if x1 == x2: # increment Y values
            start = min(y1, y2)
            stop = max(y1, y2) + 1
            for y in range(start, stop):
                diagArr[y][x1] += 1
        elif y1 == y2: # increment X vals
            start = min(x1, x2)
            stop = max(x1, x2) + 1
            for x in range(start, stop):
                diagArr[y1][x] += 1
        

def findDiagVents():
    for line in lines:
        modData = line.replace(' -> ', ',').split(',')
        x1 = int(modData[0])
        y1 = int(modData[1])
        x2 = int(modData[2])
        y2 = int(modData[3])
        
        if x1 != x2 and y1 != y2: #diagonal
            x = abs(x1 - x2)
            y = abs(y1 - y2)
            if x1 > x2 and y1 > y2:
                if x > y:
                    for i in range(x + 1):
                        diagArr[y1 - i][x1 - i] += 1
                else:
                    for i in range(y + 1):
                        diagArr[y1 - i][x1 - i] += 1
            if x1 < x2 and y1 < y2:
                if x > y:
                    for i in range(x + 1):
                        diagArr[y1 + i][x1 + i] += 1
                else:
                    for i in range(y + 1):
                        diagArr[y1 + i][x1 + i] += 1
            if x1 > x2 and y1 < y2:
                if x > y:
                    for i in range(x + 1):
                        diagArr[y1 + i][x1 - i] += 1
                else:
                    for i in range(y + 1):
                        diagArr[y1 + i][x1 - i] += 1
            if x1 < x2 and y1 > y2:
                if x > y:
                    for i in range(x + 1):
                        diagArr[y1 - i][x1 + i] += 1
                else:
                    for i in range(y + 1):
                        diagArr[y1 - i][x1 + i] += 1

findVents()    
counter = 0        
for row in diagArr:
    for elem in row:
        if elem > 1:
            counter += 1
            
print("Horizontal/vertical only:\t" + str(counter))
findDiagVents()
counter = 0        
for row in diagArr:
    for elem in row:
        if elem > 1:
            counter += 1

print("Including diagonal: \t\t" + str(counter))


