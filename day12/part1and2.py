import string
import os
os.chdir(os.path.dirname(__file__))

#lines = open('example.txt').read().splitlines()
lines = open('input.txt').read().splitlines()

caveLinks = {}

for line in lines:
    vals = line.split("-")
    if vals[0] in caveLinks:
        caveLinks[vals[0]].append(vals[1])
    else:
        lst = []
        lst.append(vals[1])
        caveLinks[vals[0]] = lst
    
    if vals[1] in caveLinks:
        caveLinks[vals[1]].append(vals[0])
    else:
        lst = []
        lst.append(vals[0])
        caveLinks[vals[1]] = lst
        
    

def findPathsRec(orig, visited, canVisitAgain):
    if orig.islower():
        visited = visited.union({orig}) # add this cave to set of visited caves
    numPaths = 0
    for nextCave in caveLinks[orig]: # iterate through all targets from this cave
        if nextCave == "start":
            continue
        if nextCave == "end": # got to the end, increment number of paths
            numPaths += 1
        elif nextCave not in visited:
            numPaths += findPathsRec(nextCave, visited, canVisitAgain)
        elif canVisitAgain: # 2nd time, don't visit a 3rd
            numPaths += findPathsRec(nextCave, visited, False)
    return numPaths

def findPaths(caveLinks, canVisitAgain):
    return findPathsRec("start", set(), canVisitAgain)


    

print(caveLinks)
print(findPaths(caveLinks, False))
print(findPaths(caveLinks, True))
print()
input()