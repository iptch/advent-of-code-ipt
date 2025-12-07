import sys, math
from collections import defaultdict

file = open("/home/manuelgr/advent-of-code-ipt/2025/MGR/day07/input.txt", "r")

input = file.read().splitlines()
file.close()

start = 0
for i in range(0, len(input[0])):
    if input[0][i] == 'S':
        start = i

global total_score
global state

state = dict()
total_score = set()
def beam(idx, row):
    if state.get((idx, row), False):
        return
    else:
        state[(idx, row)] = True
    global total_score
    for r in range(row+1, len(input)):
        if input[r][idx] == '.':
            continue
        elif input[r][idx] == '^':
            total_score.add((idx, r))
            if idx < len(input[0])-1:
                beam(idx+1, r)
            if idx > 1:
                beam(idx-1, r)
            break
        else:
            print('Error')
    
beam(start, 0)

print(len(total_score))

state = dict()
def beam(idx, row):
    if (idx, row) in state:
        return state[(idx, row)]
    score = 0
    for r in range(row+1, len(input)):
        if input[r][idx] == '.':
            continue
        elif input[r][idx] == '^':
            if idx < len(input[0])-1:
                tmp = beam(idx+1, r)
                state[(idx+1, r)] = tmp
                score += tmp
            if idx > 1:
                tmp = beam(idx-1, r)
                state[(idx-1, r)] = tmp
                score += tmp
            state[(idx, r)] = score
            return score
        else:
            print('Error')
    return 1
    
result = beam(start, 0)

print(result+1)