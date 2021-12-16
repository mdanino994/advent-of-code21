countOfDepthIncrease = 0
prevDepth = -1
currDepth = -1
for line in open('input.txt'):
    currDepth = int(line)

    if prevDepth != -1 and currDepth > prevDepth:
        countOfDepthIncrease += 1
        
    prevDepth = currDepth
print(str(countOfDepthIncrease))
