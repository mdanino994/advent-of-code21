import string
import os
os.chdir(os.path.dirname(__file__))

def getGammaEpsilon():
    ones = [0] * 12
    zeroes = [0] * 12

    for line in open('input.txt'):
        for i in range(12):
            if line[i] == '0':
                zeroes[i] += 1
            else:
                ones[i] += 1
    epsilon = ''
    gamma = ''
    for i in range(12):
        if ones[i] > zeroes[i]:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
                
    print('power consumption: ' + str(int(gamma, 2) * int(epsilon, 2)))

def getOxyCo2():
    onesArr = []
    zeroArr = []
    onesCounter = 0
    zeroCounter = 0
    oxy = ''
    co2 = ''
    lines = open('input.txt').readlines()
    for line in lines:
        if line[0] == '1':
            onesArr.append(line.strip())
            onesCounter += 1
        else:
            zeroArr.append(line.strip())
            zeroCounter += 1
    if onesCounter >= zeroCounter:
        oxy = getOxy(onesArr, 1, True)
        co2 = getOxyCo2Recur(zeroArr, 1, False)
    else:
        oxy = getOxyCo2Recur(zeroArr, 1, True)
        co2 = getOxyCo2Recur(onesArr, 1, False)
    print('life support rating: ' + str(int(oxy, 2) * int(co2, 2)))
    
def getOxyCo2Recur(arr, pos, checkOxy):
    onesArr = []
    zeroArr = []
    onesCounter = 0
    zeroCounter = 0
    if len(arr) == 1 :
        return arr[0]
    else:
        for line in arr:
            if line[pos] == '1':
                onesCounter += 1
                onesArr.append(line)
            else:
                zeroArr.append(line)
                zeroCounter += 1
        if onesCounter >= zeroCounter and checkOxy:
            return getOxyCo2Recur(onesArr, pos + 1, checkOxy)
        elif onesCounter < zeroCounter and checkOxy:
            return getOxyCo2Recur(zeroArr, pos + 1, checkOxy)
        elif onesCounter >= zeroCounter and not checkOxy: # check co2
            return getOxyCo2Recur(zeroArr, pos + 1, checkOxy)
        elif onesCounter < zeroCounter and not checkOxy: # check co2
            return getOxyCo2Recur(onesArr, pos + 1, checkOxy)
        
getGammaEpsilon()
getOxyCo2()
k=input("")