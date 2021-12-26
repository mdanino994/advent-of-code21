import string
from collections import defaultdict
import re
import os
import copy
os.chdir(os.path.dirname(__file__))

#lines = open('example.txt').read().splitlines()
lines = open('input.txt').read().splitlines()

rules = []
template = ""
pairCounts = defaultdict(int)
elemCounts = defaultdict(int)
for line in lines:
    if line == "":
        continue
    if "->" in line:
        rules.append(line.strip().split(" -> "))
    else:
        template = line.strip()

for rule in rules:
    pairCounts[rule[0]] = template.count(rule[0])

rules = dict(rules)

for char in template:
    elemCounts[char] += 1

for k, v in pairCounts.items():
    print(k, end=" : ")
    print(v)

print()

for k, v in elemCounts.items():
            print(k, end=" : ")
            print(v)

print()

# for k, v in rules.items():
    # print(k, end=" : ")
    # print(v)

def polymerize(iters):
    global pairCounts
    global elemCounts
    global rules
    for i in range(iters):
        tmpdict = copy.deepcopy(pairCounts)
        for k, v in pairCounts.items():
            if v > 0:
                pair = list(k)
                pair.append(pair[1])
                pair[1] = rules[k] # apply the rule and get the new string (ex: NN -> NCN)
                elemCounts[rules[k]] += v # increment how many new elements were added to the polymer
                pair = ''.join(pair)
                tmpdict[pair[:2]] += v # split new string after rule applied into the new pairs (ex NCN -> NC, CN), increment counts of each, decrement original string count 
                tmpdict[pair[1:]] += v
                tmpdict[k] -= pairCounts[k]
        pairCounts = copy.deepcopy(tmpdict)
    minVal = -1
    maxVal = -1
    for k, v in elemCounts.items():
        if minVal == -1 or maxVal == -1:
            minVal = v
            maxVal = v
        if v < minVal:
            minVal = v
        if v > maxVal:
            maxVal = v
    print(maxVal - minVal)
        


print(template)
print()
#print(rules)
polymerize(40)
print("polymer size: " + str(sum(v for _, v in elemCounts.items())))
# for k, v in pairCounts.items():
            # print(k, end=" : ")
            # print(v)
for k, v in elemCounts.items():
            print(k, end=" : ")
            print(v)



input()

