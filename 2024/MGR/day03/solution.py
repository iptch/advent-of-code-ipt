import re, sys, math

file = open("/home/manuelgr/advent-of-code-ipt/2024/MGR/day03/input.txt", "r")

def mull_it(line):
    findall_list = re.findall('mul\(([0-9]{1}|[0-9]{2}|[0-9]{3}),([0-9]{1}|[0-9]{2}|[0-9]{3})\)', line)

    mull = 0
    for elem in findall_list:
        left = int(elem[0])
        right = int(elem[1])
        mull += left * right
    
    return mull

def mull_it_advanced(line):
    mull = 0
    
    line = 'do()' + line
    
    s = len(line)
    while len(line) > 0:
        finditer = re.finditer('do\(\)((?!don\'t\(\)).)*mul\(([0-9]{1,3}),([0-9]{1,3})\)', line)
        
        count = 0
        for elem in finditer:
            count += 1
            findall_list = re.findall('mul\(([0-9]{1}|[0-9]{2}|[0-9]{3}),([0-9]{1}|[0-9]{2}|[0-9]{3})\)', elem.group()[-13:])
            
            for e in findall_list:
                left = int(e[0])
                right = int(e[1])
                mull += left * right

            line = line[0:elem.end()-12]
        if count == 0:
            line = line[0:0]
    
    return mull

mull = 0
mull_advanced = 0
while True:
    line = file.readline()
    
    mull += mull_it(line)
    mull_advanced += mull_it_advanced(line)
    
    if not line:
        break

print(mull)
print(mull_advanced)

file.close()