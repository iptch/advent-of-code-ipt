import sys, math
from collections import defaultdict, deque

file = open("/home/manuelgr/advent-of-code-ipt/2025/MGR/day11/input.txt", "r")

input = file.read().splitlines()
file.close()

d = defaultdict(set)
for line in input:
    key = line.split(' ')[0][:-1]
    for e in line.split(' ')[1:]:
        d[key].add(e)

global total_score
total_score = 0

def traverse(point, end):
    global total_score
    if point == end:
        total_score += 1
        return
    
    for e in d[point]:
        traverse(e, end)
    return

traverse('you', 'out')

print(total_score)

global after_dac, after_fft
after_dac = set()
after_fft = set()
after_svr = set()

def check_svr(point):
    global after_svr
    if point in after_svr:
        return
    after_svr.add(point)
    
    if point == 'fft' or point == 'dac':
        return
    
    for e in d[point]:
        check_svr(e)
    return

def check_dac(point):
    global after_dac
    if point in after_dac:
        return
    after_dac.add(point)
    
    if point == 'fft':
        return
    
    for e in d[point]:
        check_dac(e)
    return

def check_fft(point):
    global after_fft
    if point in after_fft:
        return
    after_fft.add(point)
    
    if point == 'dac':
        return
    
    for e in d[point]:
        check_fft(e)
    return

check_dac('dac')
check_fft('fft')
check_svr('svr')

print(len(after_dac))
print(len(after_fft))
print(len(after_svr))

after_fft = after_fft - after_dac
after_fft.add('dac')

after_svr = after_svr - after_dac
after_svr = after_svr - after_fft
after_svr.add('fft')

print(len(after_dac))
print(len(after_fft))
print(len(after_svr))

total_score = 0
def traverse_dac(point, end):
    global total_score
    if point == end:
        total_score += 1
        return 1
    s = 0
    for e in d[point]:
        if e in after_dac:
            s += traverse_dac(e, end)
    return s

def traverse_fft(point, end):
    global total_score
    if point == end:
        total_score += 1
        return 1
    s = 0
    for e in d[point]:
        if e in after_fft:
            s += traverse_fft(e, end)
    return s

def traverse_svr(point, end):
    global total_score
    if point == end:
        total_score += 1
        return 1
    s = 0
    for e in d[point]:
        if e in after_svr:
            s += traverse_svr(e, end)
    return s

end_dac = 'fft' if 'fft' in after_dac else 'out'
end_fft = 'dac' if 'dac' in after_fft else 'out'

print(end_dac)
print(end_fft)

res_dac = traverse_dac('dac', 'out')
print(res_dac)
res_fft = traverse_fft('fft', 'dac')
print(res_fft)
res_svr = traverse_svr('svr', 'fft')
print(res_svr)

print(res_dac*res_fft*res_svr)
