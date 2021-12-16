import string

ones = [0] * 12
zeroes = [0] * 12
    
for line in open('input.txt'):
    #print(line)
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
            
print('multi: ' + str(int(gamma, 2) * int(epsilon, 2)))
