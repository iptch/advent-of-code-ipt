import sys, math
from collections import defaultdict, deque

file = open("/home/manuelgr/advent-of-code-ipt/2025/MGR/day12/input.txt", "r")

input = file.read().splitlines()
file.close()

shapes = []
regions = []
count_hash, count_dot = 0, 0
for line in input:
    if len(line) == 2:
        shapes.append((count_hash, count_dot))
        count_hash, count_dot = 0, 0
    count_hash += line.count('#')
    count_dot += line.count('.')
    
    if 'x' in line:
        regions.append((int(line.split(':')[0].split('x')[0]), int(line.split(':')[0].split('x')[1]), [int(x) for x in line.split(':')[1][1:].split(' ')]))
shapes.append((count_hash, count_dot))
shapes.pop(0)

print(shapes)
print(regions)

total_score = 0
for r in regions:
    size = r[0] * r[1]
    wanted = 0
    for idx, s in enumerate(r[2]):
        wanted += s*shapes[idx][0]
    
    if wanted <= size:
        print(r)
        total_score += 1
        
print(total_score)


