import string

dist = 0
depth = 0
aim = 0
for line in open('input.txt'):
    num = (int(line.strip(string.ascii_letters)))
    
    if line.find('forward ') != -1:
        dist += num
        depth += aim * num
    elif line.find('down') != -1:
        aim += num
    elif line.find('up') != -1:
        aim -= num
print(str(depth * dist))
