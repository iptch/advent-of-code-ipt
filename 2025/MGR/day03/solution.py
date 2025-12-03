import sys, math
from collections import defaultdict

file = open("/home/manuelgr/advent-of-code-ipt/2025/MGR/day03/input.txt", "r")

sequence = file.read().splitlines()
file.close()

total_score = 0
for line in sequence:
    max = 0
    idx = -1
    for i in range(0, len(line)-1):
        if int(line[i]) > max:
            max = int(line[i])
            idx = i
    max_j = 0
    for j in range(idx+1, len(line)):
        if int(line[j]) > max_j:
            max_j = int(line[j])
    total_score += int(str(max) + str(max_j))
    
print(total_score)

total_score = 0
for line in sequence:
    jolts = ''
    idx = -1
    for c in range(11, -1, -1):
        max = 0
        for i in range(idx+1, len(line)-c):
            if int(line[i]) > max:
                max = int(line[i])
                next_idx = i
        jolts = jolts + str(max)
        idx = next_idx
    total_score += int(jolts)
    
print(total_score)
