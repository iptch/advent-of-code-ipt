import sys, math
from collections import defaultdict

file = open("/home/manuelgr/advent-of-code-ipt/2025/MGR/day02/input.txt", "r")
line = file.readline()
file.close()

ranges = []
for r in line.split(','):
    start = int(r.split('-')[0])
    end = int(r.split('-')[1])
    ranges.append((start, end))
    
def isSilly(number):
    l = len(str(number))
    if l %2 != 0:
        return False
    
    front, back = str(number)[:math.ceil(l/2)], str(number)[l//2:]
    if int(front) == int(back):
        return True
    return False
    
total_score = 0

print(ranges)

maximum = 0
for range_r in ranges:
    r = range_r[1]
    if r > maximum:
        maximum = r
        
counter = 1

while int(str(counter) + str(counter)) < maximum:
    for range_r in ranges:
        if int(str(counter) + str(counter)) >= range_r[0] and int(str(counter) + str(counter)) <= range_r[1]:
            total_score += int(str(counter) + str(counter))
    counter += 1

print(total_score)       

def mul_counter(multiplicator, number):
    result = ''
    for i in range(multiplicator):
        result += str(number)
    return int(result)


counter = 1
multiplicator = 2
d = defaultdict(set)
while mul_counter(multiplicator, counter) < maximum:
    curr = mul_counter(multiplicator, counter)
    for range_r in ranges:
        if curr >= range_r[0] and curr <= range_r[1]:
            d[range_r].add(curr)
    if mul_counter(multiplicator+1, counter) > maximum:
        multiplicator = 2
        counter += 1
    else:
        multiplicator += 1

total_score = 0
for s in d.values():
    for elem in s:
        total_score += elem

print(total_score)
