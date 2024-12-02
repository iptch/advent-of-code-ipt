import sys, math

file = open("/home/manuelgr/advent-of-code-ipt/2024/MGR/day02/input.txt", "r")

left_list = []
right_list = []

def is_increasing(input):
    for i in range(1, len(input)):
        diff = input[i] - input[i-1]
        if diff < 1 or diff > 3:
            return False, i
    return True, 0

def is_decreasing(input):
    for i in range(1, len(input)):
        diff = input[i-1] - input[i]
        if diff < 1 or diff > 3:
            return False, i
    return True, 0

def is_increasing_damp(input):
    b, i = is_increasing(input)
    if b:
        return True
    else:
        return is_increasing(input[:i] + input[i+1:])[0] or is_increasing(input[:i-1] + input[i:])[0]

def is_decreasing_damp(input):
    b, i = is_decreasing(input)
    if b:
        return True
    else:
        return is_decreasing(input[:i] + input[i+1:])[0] or is_decreasing(input[:i-1] + input[i:])[0]

safe_reports = 0
dampened_safe_reports = 0
while True:
    line = file.readline()
    if not line:
        break
    
    split_line = [int(x) for x in line.split(" ")]
    if is_increasing(split_line)[0] or is_decreasing(split_line)[0]:
        safe_reports += 1
    if is_increasing_damp(split_line) or is_decreasing_damp(split_line):
        dampened_safe_reports += 1

file.close()

print(safe_reports)
print(dampened_safe_reports)
