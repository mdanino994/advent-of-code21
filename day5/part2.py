import string
import os
os.chdir(os.path.dirname(__file__))

xData = []
yData = []
xMax = 0
yMax = 0
diagCounter = 0
xCounter = 0
yCounter = 0
lines = open('input.txt').read().splitlines()
#get max x/y vals
for line in lines:
    modData = line.replace(' -> ', ',').split(',')
    xData.append(int(modData[0]))
    yData.append(int(modData[1]))
    xData.append(int(modData[2]))
    yData.append(int(modData[3]))
    

xMax = max(xData)
yMax = max(yData)

print(xMax)
print(yMax)

diagArr = [[0] * yMax for _ in range(xMax)]

for line in lines:

    modData = line.replace(' -> ', ',').split(',')
    x1 = int(modData[0])
    y1 = int(modData[1])
    x2 = int(modData[2])
    y2 = int(modData[3])
    if x1 == x2: # increment Y values
        yCounter += 1
        start = min(y1, y2) -1
        stop = max(y1, y2)
        for y in range(start, stop):
            diagArr[x1-1][y] += 1
    elif y1 == y2: # increment X vals
        xCounter += 1
        start = min(x1, x2) -1
        stop = max(x1, x2)
        for x in range(start, stop):
            diagArr[x][y1-1] += 1
    else: #diagonal
        diagCounter += 1
        
        diagArr[x1-1][y1-1] += 1
        diagArr[x2-1][y2-1] += 1
        x = abs(x1 - x2)
        y = abs(y1 - y2)
        if x1 > x2 and y1 > y2:
            if x > y:
                for i in range(1, x):
                    diagArr[x1 - i][y1 - i] += 1
            else:
                for i in range(1, y):
                    diagArr[x1 - i][y1 - i] += 1
        if x1 < x2 and y1 < y2:
            if x > y:
                for i in range(1, x):
                    diagArr[x1 + i][y1 + i] += 1
            else:
                for i in range(1, y):
                    diagArr[x1 + i][y1 + i] += 1
        if x1 > x2 and y1 < y2:
            if x > y:
                for i in range(1, x):
                    diagArr[x1 - i][y1 + i] += 1
            else:
                for i in range(1, y):
                    diagArr[x1 - i][y1 + i] += 1
        if x1 < x2 and y1 > y2:
            if x > y:
                for i in range(1, x):
                    diagArr[x1 + i][y1 - i] += 1
            else:
                for i in range(1, y):
                    diagArr[x1 + i][y1 - i] += 1
        
counter = 0        
for row in diagArr:
    for elem in row:
        if elem > 1:
            counter += 1
            
print(xCounter)
print(yCounter)
print(diagCounter)
print(counter)