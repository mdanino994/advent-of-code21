import string
import os
os.chdir(os.path.dirname(__file__))

lines = open('input.txt').read().splitlines()
fishArr = []
#get max x/y vals
for line in lines:
    modData = map(int, line.split(','))
    fishArr.extend(modData)


def multiplyFish(cycles):
    counter = 0
    for day in range(cycles):
        #printDay(day)
        counter = 0
        for i in  range(len(fishArr)):
            if fishArr[i] == 0:
                counter += 1
                fishArr[i] = 6
            else:
                fishArr[i] -= 1
        for i in range(counter):
            fishArr.append(8)
        #print("day: " + str(day))
    #printDay(cycles)
            
def printDay(day):
    if day == 0:
        print("Initial state:", end=' ')
        
    elif day == 1:
        print("After " + str(day) + " day:  ", end='')
    else:
        print("After " + str(day) + " days: ", end='')
        
    print(*fishArr, sep=',')

printDay(0)
multiplyFish(80)

print("Number of fish: " + str(len(fishArr)))