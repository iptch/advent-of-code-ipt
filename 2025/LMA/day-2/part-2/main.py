import re

rows = []

def is_valid(x):
    regex = re.compile(r'^(\d+)\1+$')
    return not regex.match(x)

with open("input.txt", "r") as file:
    for line in file:
        rows = line.strip().split(',')
        rows = [(x.split('-')[0], x.split('-')[1]) for x in rows]

invalid = 0

for (start, end) in rows:
    for x in range(int(start), int(end)+1):
        if not is_valid(str(x)):
            invalid += x

print(invalid)

