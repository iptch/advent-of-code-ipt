rows = []

def find_joltage(s):
    count = 12
    start = 0
    result = ""

    while count > 0:
        end = len(s) - count
        best = max(s[start:end+1])
        pos = s.index(best, start, end+1)
        result += best
        start = pos + 1
        count -= 1

    return int(result)

with open("input.txt", "r") as file:
    for line in file:
        rows.append(str(line.strip()))

sum = 0

for row in rows:
    x = find_joltage(row)
    sum += x

print(sum)



