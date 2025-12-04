import sys, math
from collections import defaultdict

file = open("/home/manuelgr/advent-of-code-ipt/2025/MGR/day04/input.txt", "r")

input = file.read().splitlines()
sequence = list()
for line in input:
    sequence.append(list(line))

file.close()

def check_surroundings(s, i, j):
    c = 0
    if (i+1, j) in s:
        c += 1
    if (i+1, j-1) in s:
        c += 1
    if (i+1, j+1) in s:
        c += 1
    if (i-1, j) in s:
        c += 1
    if (i-1, j+1) in s:
        c += 1
    if (i-1, j-1) in s:
        c += 1
    if (i, j+1) in s:
        c += 1
    if (i, j-1) in s:
        c += 1

    return c

s = set()
for i in range(len(sequence)):
    for j in range(len(sequence[0])):
        curr = sequence[i][j]
        if curr == '@':
            s.add((i, j))

total_score = 0
to_remove = set()
for i in range(len(sequence)):
    for j in range(len(sequence[0])):
        curr = sequence[i][j]
        if curr == '@':
            c = check_surroundings(s, i, j)
            if c < 4:
                total_score += 1

                
print(total_score)

total_score = 0
old_total_score = -1
while (total_score != old_total_score):
    old_total_score = total_score
    s = set()
    for i in range(len(sequence)):
        for j in range(len(sequence[0])):
            curr = sequence[i][j]
            if curr == '@':
                s.add((i, j))
    
    to_remove = set()
    for i in range(len(sequence)):
        for j in range(len(sequence[0])):
            curr = sequence[i][j]
            if curr == '@':
                c = check_surroundings(s, i, j)
                if c < 4:
                    to_remove.add((i, j))
                    total_score += 1
    for (l, r) in to_remove:
        sequence[l][r] = 'x'

                
print(total_score)
