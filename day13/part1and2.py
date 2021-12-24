import string
import os
os.chdir(os.path.dirname(__file__))

#lines = open('example.txt').read().splitlines()
lines = open('input.txt').read().splitlines()

paper = []
coords = []
folds = []


for line in lines:
    if line == "":
        continue
    if "fold along " in line:
        folds.append(line.replace("fold along ", "").strip().split("="))
    else:
        coords.append(line.strip().split(","))

coords = [[int(j) for j in i] for i in coords]

    


print(coords)

def fillPaper():
    xMax = 0
    yMax = 0
    for coord in coords:
        if xMax < int(coord[0]):
            xMax = int(coord[0])
        if yMax < int(coord[1]):
            yMax = int(coord[1])
    xMax += 1
    yMax += 1
    paper = [["."] * xMax for _ in range(yMax)]
    
    for coord in coords:
        paper[int(coord[1])] [int(coord[0])] = "#"
    return paper

def printPaper(paper):
    for row in paper:
        for elem in row:
            print(elem, end='')
        print()

def updateCoords():
    for fold in folds:
        if fold[0] == "y":
            foldLine = int(fold[1])
            for coord in coords:
                if foldLine < coord[1]:
                    tmp = 2 * (coord[1] - foldLine)
                    coord[1] -= tmp
        else: # fold along x
            foldLine = int(fold[1])
            for coord in coords:
                if foldLine < coord[0]:
                    tmp = 2 * (coord[0] - foldLine)
                    coord[0] -= tmp
        paper = fillPaper()
        printPaper(paper)
        print("num dots: " + str(countDots(paper)))
        print()
        
    
def countDots(paper):
    count = 0
    for row in paper:
        for elem in row:
            if elem == "#":
                count += 1
    return count
print(folds)
paper = fillPaper()
print()
#printPaper(paper)
print()
print()

updateCoords()

input()


