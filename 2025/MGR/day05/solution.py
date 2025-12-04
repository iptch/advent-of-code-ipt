import sys, math
from collections import defaultdict

file = open("/home/manuelgr/advent-of-code-ipt/2025/MGR/day05/input.txt", "r")

input = file.read().splitlines()
# sequence = file.read().splitlines()
sequence = list()
for line in input:
    sequence.append(list(line))
file.close()


