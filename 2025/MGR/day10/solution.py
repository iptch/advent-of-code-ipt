import sys, math
from collections import defaultdict, deque

file = open("/home/manuelgr/advent-of-code-ipt/2025/MGR/day10/input.txt", "r")

input = file.read().splitlines()
file.close()

config_lights = []
config_buttons = []
config_joltages = []
for line in input:
    indicators = line.split(' ')[0]
    lights = ''
    for e in indicators[1:-1]:
        if e == '.':
            lights += '0'
        elif e == '#':
            lights += '1'
        else:
            print('Nope')
    config_lights.append(lights)
    js = line.split(' ')[-1][1:-1]
    joltages = [int(x) for x in js.split(',')]
    config_joltages.append(joltages)
    buttons = []
    for e in line.split(' ')[1:-1]:
        presses = []
        for k in e[1:-1].split(','):
            presses.append(int(k))
        buttons.append(presses)
    config_buttons.append(buttons)

global state
def press(button, lights):
    #print(button, lights)
    result = list(lights)
    for p in button:
        result[p] = (int(result[p])+1)%2
    result = ''.join(str(x) for x in result)
    state[result] = min(state[result], state[lights]+1)
    #print(button, lights, result)
    return result
  
#print(config_lights)
#print(config_buttons)
#print(config_joltages)

config_count = len(config_buttons)
""" total_score = 0

for i in range(0, config_count):
    print(i, config_count)
    state = defaultdict(lambda:1000)
    buttons = config_buttons[i]
    possible_states = set()
    start = ''.join(str(x) for x in [0] * len(config_lights[i]))
    possible_states.add(start)
    state[start] = 0
    #print(possible_states, buttons)
    count = 0
    while count < 100:
        for s in list(possible_states):
            for b in buttons:
                r = press(b, s)
                possible_states.add(r)
        count += 1
    #print(state)
    total_score += state[config_lights[i]]

print(total_score) """

total_score = 0
for i in range(0, config_count):
    print(i)
    print(config_buttons[i])
    print(config_joltages[i])
    buttons = config_buttons[i]
    seen = set()
    states = deque()
    start = ','.join(str(x) for x in [0] * len(config_joltages[i]))
    states.append((start, 0))
    seen.add(start)
    going = True
    target = ','.join([str(x) for x in config_joltages[i]])
    while len(states) > 0 and going:
        curr_elem = states.popleft()
        curr = [int(x) for x in curr_elem[0].split(',')]
        count = curr_elem[1]
        for b in buttons:
            res = curr.copy()
            for e in b:
                res[e] += 1
            res = ','.join([str(x) for x in res])
            if target == res:
                print(count)
                total_score += count + 1
                going = False
            else:
                if res not in seen:
                    c = [int(x) for x in res.split(',')]
                    valid = True
                    if all(a <= b for a, b in zip(config_joltages[i], c)):
                        valid = False
                    if valid:
                        seen.add(res)
                        states.append((res, count+1))

print(total_score)