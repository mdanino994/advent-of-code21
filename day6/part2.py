import string
import os
os.chdir(os.path.dirname(__file__))

lines = open('input.txt').read().splitlines()
fishArr = []
fishCycleArr = []
#get max x/y vals
for line in lines:
    modData = map(int, line.split(','))
    fishArr.extend(modData)

for i in range(9):
    count = 0
    for fish in fishArr:
        if fish == i:
            count += 1
    fishCycleArr.append(count)

print(fishCycleArr)

def multiplyFish(cycles):
    counter = 0
    for i in range(cycles):
        temp = fishCycleArr[0]
        
        for j in range(8):
            fishCycleArr[j] = fishCycleArr[j + 1]
        fishCycleArr[8] = temp
        fishCycleArr[6] += temp
        print(fishCycleArr)
        

multiplyFish(256)
print(fishCycleArr)
print(str(sum(fishCycleArr)))