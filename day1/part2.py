with open('input.txt') as f:
    lines = f.readlines() # read all lines from input file
    countOfSumsIncrease = 0
    prevSum = 0
    currSum = 0
    varToSubtract = -1
    count = 0
    f.close()
    for line in lines:
        if count < 3:
            currSum += int(line)
        
        if count >= 3:
            prevSum = currSum
            currSum += (int(line) - int(lines[count - 3]))
            if currSum > prevSum:
                countOfSumsIncrease += 1    

        count += 1
    print(str(countOfSumsIncrease))
