import sys, math
from collections import defaultdict

file = open("/home/manuelgr/advent-of-code-ipt/2025/MGR/day08/input.txt", "r")

input = file.read().splitlines()
file.close()

stop = 1000

def distance(point1, point2):
    d = 0.0
    d = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)
    return d

junctions = []
for line in input:
    junctions.append((int(line.split(',')[0]), int(line.split(',')[1]), int(line.split(',')[2])))
    
distances = []
for i in range(0, len(junctions)-1):
    for j in range(i+1, len(junctions)):
        distances.append((distance(junctions[i], junctions[j]), junctions[i], junctions[j]))

sort_distances = sorted(distances)

d = defaultdict()
c = 0
for j in junctions:
    d[j] = c
    c += 1

added = 0
for elem in sort_distances:
    l, r = d[elem[1]], d[elem[2]]
    if l < r:
        for e in d:
            if d[e] == r:
                d[e] = l
    else:
        for e in d:
            if d[e] == l:
                d[e] = r
        
    added += 1
    if added == stop:
        break
#print(d)

circuits = []
for i in range(0, len(junctions)):
    circuits.append(0)
    for e in d:
        if d[e] == i:
            circuits[i] += 1

result = sorted(circuits, reverse=True)
#print(result)

print(math.prod(result[:3]))

junctions = []
for line in input:
    junctions.append((int(line.split(',')[0]), int(line.split(',')[1]), int(line.split(',')[2])))
    
distances = []
for i in range(0, len(junctions)-1):
    for j in range(i+1, len(junctions)):
        distances.append((distance(junctions[i], junctions[j]), junctions[i], junctions[j]))

sort_distances = sorted(distances)

d = defaultdict()
c = 0
for j in junctions:
    d[j] = c
    c += 1

added = 0
for elem in sort_distances:
    l, r = d[elem[1]], d[elem[2]]
    if l < r:
        for e in d:
            if d[e] == r:
                d[e] = l
    else:
        for e in d:
            if d[e] == l:
                d[e] = r
    if len(set(d.values())) == 1:
        print(elem[1][0] * elem[2][0])
        break
