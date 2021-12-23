import string
import os
os.chdir(os.path.dirname(__file__))

lines = open('input.txt').read().splitlines()
ciphers = []
entries = []

for line in lines:
    modData = line.split("|")

    ciphers.append(modData[0].strip().split(" "))
    entries.append(modData[1].strip().split(" "))

def findUniqueDigitCount():
    uniqueCount = 0
    for i in range(len(ciphers)):
        for obj in entries[i]:
            if len(obj) == 2 or len(obj) == 3 or len(obj) == 4 or len(obj) == 7:
                uniqueCount += 1
    return uniqueCount

def findUniqueDigits(cipherKey, cipher):
    uniqueCount = 0
    for obj in cipher:
        if len(obj) == 2: 
            cipherKey[1] = ''.join(sorted(obj))
        elif len(obj) == 3: 
            cipherKey[7] = ''.join(sorted(obj))
        elif len(obj) == 4: 
            cipherKey[4] = ''.join(sorted(obj))
        elif len(obj) == 7: 
            cipherKey[8] = ''.join(sorted(obj))
        

def findIntersections(cipherKey, cipher):
    for obj in cipher:
        if len(obj) == 6:
            if len(set(cipherKey[4]).intersection(obj)) == 4: # full intersection
                cipherKey[9] = ''.join(sorted(obj))
            elif len(set(cipherKey[1]).intersection(obj)) == 2: # full intersection
                cipherKey[0] = ''.join(sorted(obj))
            else:
                cipherKey[6] = ''.join(sorted(obj)) # 6 doesn't overlap with 3 or 6
    for obj in cipher:
        if len(obj) == 5:
            if len(set(cipherKey[1]).intersection(obj)) == 2: # full intersection
                cipherKey[3] = ''.join(sorted(obj))
            elif len(set(cipherKey[6]).intersection(obj)) == 5: # full intersection
                cipherKey[5] = ''.join(sorted(obj))
            else:
                cipherKey[2] = ''.join(sorted(obj))

def decipher():
    total = 0
    for i, cipher in enumerate(ciphers):
        cipherKey = [""]*10
        findUniqueDigits(cipherKey, cipher)
        findIntersections(cipherKey, cipher)
        numStr = ""
        
        for entry in entries[i]:
            numStr += str(cipherKey.index(''.join(sorted(entry))))
        total += int(numStr)
    print(total)
        

decipher()        