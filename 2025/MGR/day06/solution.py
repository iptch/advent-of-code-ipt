import sys, math
from collections import defaultdict

file = open("/home/manuelgr/advent-of-code-ipt/2025/MGR/day06/input.txt", "r")

input = file.read().splitlines()
file.close()

sequence = []
operators = []
for idx, line in enumerate(input):
    if idx == len(input)-1:
        for e in line.split(' '):
            if e != '':
                operators.append(e)
    else:
        s = []
        for e in line.split(' '):
            if e != '':
                s.append(int(e))
        sequence.append(s)

total_score = 0
for i in range(0, len(operators)):
    if operators[i] == '*':
        total_score += math.prod([row[i] for row in sequence])
    else:
        total_score += sum([row[i] for row in sequence])

print(total_score)

total_score = 0
s = []
for j in range(len(input[0])-1, -1, -1):
    n = ''
    for i in range(0, len(input)-1):
        if input[i][j] != ' ':
            n += input[i][j]
    if n != '':
        s.append(int(n))
    if input[len(input)-1][j] in '+':
        total_score += sum(s)
        s = []
    if input[len(input)-1][j] in '*':
        total_score += math.prod(s)
        s = []
    
print(total_score)
