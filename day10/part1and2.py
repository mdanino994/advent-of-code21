import string
import os
os.chdir(os.path.dirname(__file__))

#lines = open('example.txt').read().splitlines()
lines = open('input.txt').read().splitlines()
openVals = "([{<"
closeVals = ")]}>"
errorScore = 0
incompleteLines = []
for line in lines:
    
    symbolStack = []
    broke = False
    for elem in line:
        if elem in openVals:
            symbolStack.append(elem)
        else: # not an opening symbol, see if line is incomplete 
            if len(symbolStack) == 0:
                broke = True
                break
            if elem == ")":
                val = symbolStack.pop()
                if val != "(":
                    errorScore += 3
                    broke = True
                    break
            if elem == "]":
                val = symbolStack.pop()
                if val != "[":
                    errorScore += 57
                    broke = True
                    break
            if elem == "}":
                val = symbolStack.pop()
                if val != "{":
                    errorScore += 1197
                    broke = True
                    break
            if elem == ">":
                val = symbolStack.pop()
                if val != "<":
                    errorScore += 25137
                    broke = True
                    break
    if len(symbolStack) > 0 and not broke:
        incompleteLines.append(line)


incScores = []
print(errorScore)
for line in incompleteLines:
    
    incompleteScore = 0
    
    stack = []
    for elem in line:
        if elem in openVals:
            stack.append(elem)
        elif elem in closeVals:
            stack.pop()
    for elem in reversed(stack):
        incompleteScore *= 5
        if elem == "(":
            incompleteScore += 1
        if elem == "[":
            incompleteScore += 2
        if elem == "{":
            incompleteScore += 3
        if elem == "<":
            incompleteScore += 4
    incScores.append(incompleteScore)
    
    
incScores.sort()
mid = incScores[int(len(incScores)/2)]
print(mid)
