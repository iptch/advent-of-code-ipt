import sys, math
from collections import defaultdict

file = open("/home/manuelgr/advent-of-code-ipt/2025/MGR/day05/input.txt", "r")

input = file.read().splitlines()
file.close()

ranges = []
ids = []
for line in input:
    if '-' in line:
        curr = line.split('-')
        ranges.append((int(curr[0]), int(curr[1])))
    else:
        if line == '':
            continue
        ids.append(int(line))

total_score = 0
for id in ids:
    for (start, end) in ranges:
        if id <= end and id >= start:
            total_score += 1
            break
    
print(total_score)

total_score = 0
ranges = sorted(ranges)
last_start, last_end = -1, -1
for (start, end) in ranges:
    if end < last_end:
        continue
    if start <= last_end:
        total_score += end - last_end
    else:
        total_score += end - start + 1

    last_start, last_end = start, end

print(total_score)
