import string

dist = 0
depth = 0
for line in open('input.txt'):
    num = (int(line.strip(string.ascii_letters)))
    
    if line.find('forward ') != -1:
        dist += num
    elif line.find('down') != -1:
        depth += num
    elif line.find('up') != -1:
        depth -= num

print(str(depth * dist))
