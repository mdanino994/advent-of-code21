import string
import os
os.chdir(os.path.dirname(__file__))

lines = open('input.txt').read().splitlines()
crabArr = []

#get max x/y vals
for line in lines:
    modData = map(int, line.split(','))
    crabArr.extend(modData)

minDistArr = [0] * (max(crabArr) + 1)
print(len(minDistArr))

print(str(max(crabArr)))
print(str(len(crabArr)))

def findMinGas():
    for i in range(len(minDistArr)):
        fuelCount = 0
        for crab in crabArr:
            fuelCount += abs(crab - i)
        minDistArr[i] = fuelCount

def findMinGasP2():
    for i in range(len(minDistArr)):
            fuelCount = 0
            for crab in crabArr:
                n = abs(crab - i)
                if n > 0:
                    fuelCount += (n * (n+1)) / 2
            minDistArr[i] = fuelCount

findMinGas()        
print("min fuel needed: " + str(min(minDistArr)))
findMinGasP2()
print("min fuel needed: " + str(min(minDistArr)))
