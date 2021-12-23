import string
import os
os.chdir(os.path.dirname(__file__))

#lines = open('example.txt').read().splitlines()
lines = open('input.txt').read().splitlines()

octArr = []

for line in lines:
    tempArr = []
    for elem in line:
        tempArr.append(int(elem))
    octArr.append(tempArr)
    
    

def printOctArr():
    for row in octArr:
        for elem in row:
            if elem > 9:
                print("x", end='')
            elif elem < 0:
                print("z", end='')
            else:
                print("%s" % str(elem), end='')
        print()
    


def flashOct(x, y):
    if y == 0:
        if x == 0: # top left, increment down and right
            #print("topleft")
            octArr[y + 1][ x] += 1 # increment down
            octArr[y][ x + 1] += 1 # increment right
            octArr[y + 1][ x + 1] += 1 # increment downright
                
        elif x == len(octArr[y]) - 1: # top right, increment down and left
            #print("topright")
            octArr[y + 1][ x] += 1 # increment down
            octArr[y][ x - 1] += 1 # increment left
            octArr[y + 1][ x - 1] += 1 # increment left
                
        else: # top edge, increment down, left and right
            #print("top")
            octArr[y + 1][ x] += 1 # increment down
            octArr[y][ x - 1] += 1 # increment left
            octArr[y][ x + 1] += 1 # increment right
            octArr[y+ 1][ x - 1] += 1 # increment downleft
            octArr[y+ 1][ x + 1] += 1 # increment downright
                
    elif y == len(octArr) - 1:
        if x == 0: # bottom left, increment up and right
            #print("botleft")
            octArr[y - 1][ x] += 1 # increment up
            octArr[y][ x + 1] += 1 # increment right
            octArr[y - 1][ x + 1] += 1 # increment upright
                
        elif x == len(octArr[y]) - 1: # bottom right, increment up and left
            #print("botright")
            octArr[y - 1][ x] += 1 # increment up
            octArr[y][ x - 1] += 1 # increment left
            octArr[y - 1][ x - 1] += 1 # increment upleft
                
        else: # bottom edge, increment up, left and right
            #print("bot")
            octArr[y - 1][ x] += 1 # increment up
            octArr[y][ x - 1] += 1 # increment left
            octArr[y - 1][ x - 1] += 1 # increment upleft
            octArr[y][ x + 1] += 1 # increment right
            octArr[y - 1][ x + 1] += 1 # increment upright
                
    elif x == 0: # left edge, increment right, up and down
        #print("left")
        octArr[y - 1][ x] += 1 # increment up
        octArr[y - 1][ x + 1] += 1 # increment upright
        octArr[y + 1][ x] += 1 # increment down
        octArr[y + 1][ x + 1] += 1 # increment downright
        octArr[y][ x + 1] += 1 # increment right
                
    elif x == len(octArr[y]) - 1: # right edge, increment left, up and down
        #print("right")
        octArr[y - 1][x] += 1 # increment up
        octArr[y + 1][x] += 1 # increment down
        octArr[y - 1][x - 1] += 1 # increment upleft
        octArr[y + 1][x - 1] += 1 # increment downleft
        octArr[y][ x - 1] += 1 # increment left
                
    else: # somewhere in the center, increment in all directions
        #print("mid")
        octArr[y - 1][ x] += 1 # increment up
        octArr[y - 1][ x - 1] += 1 # increment upleft
        octArr[y - 1][ x + 1] += 1 # increment upright
        octArr[y + 1][ x] += 1 # increment down
        octArr[y + 1][ x - 1] += 1 # increment downleft
        octArr[y + 1][ x + 1] += 1 # increment downright
        octArr[y][ x - 1] += 1 # increment left
        octArr[y][ x + 1] += 1 # increment right



def getFlashCount(cycles):
    flashCount = 0
    for i in range(cycles):
        for y, row in enumerate(octArr):
            for x, elem in enumerate(row):
                octArr[y][x] += 1
        newFlash = True
        while newFlash:
            newFlash = False
            for y, row in enumerate(octArr):
                for x, elem in enumerate(row):
                    if elem > 9 :
                        octArr[y][x] = -9 # set to negative, most flashes should happen are 8, so this should grow to -2 at most
                        newFlash = True
                        flashOct(x, y)
                    
            
        for y, row in enumerate(octArr):
            for x, elem in enumerate(row):
                if elem > 9:
                    octArr[y][x] = 0
        
        for y, row in enumerate(octArr):
            for x, elem in enumerate(row):
                if elem < 0:
                    flashCount += 1
                    octArr[y][x] = 0
        
    return flashCount
    

def allZeroes():
    for row in octArr:
        for elem in row:
            if elem != 0:
                return False
    return True

def getSyncFlashCycle():
    cycleCount = 0
    while not allZeroes():
        for y, row in enumerate(octArr):
            for x, elem in enumerate(row):
                octArr[y][x] += 1
        newFlash = True
        while newFlash:
            newFlash = False
            for y, row in enumerate(octArr):
                for x, elem in enumerate(row):
                    if elem > 9 :
                        octArr[y][x] = -9 # set to negative, most flashes should happen are 8, so this should grow to -2 at most
                        newFlash = True
                        flashOct(x, y)
                    
            
        for y, row in enumerate(octArr):
            for x, elem in enumerate(row):
                if elem > 9:
                    octArr[y][x] = 0
        
        for y, row in enumerate(octArr):
            for x, elem in enumerate(row):
                if elem < 0:
                    octArr[y][x] = 0
        cycleCount += 1
    return cycleCount





print()
#print(getFlashCount(100))
print(getSyncFlashCycle())
print()

input()