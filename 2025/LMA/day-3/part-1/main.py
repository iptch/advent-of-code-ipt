import re

rows = []

def find_joltage(input):
    max = -1
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            x = int(input[i]+input[j])
            if x > max:
                max = x
    return max

with open("input.txt", "r") as file:
    for line in file:
        rows.append(str(line.strip()))
sum = 0

for row in rows:
    sum += find_joltage(row)

print(sum)

