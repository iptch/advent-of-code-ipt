import math

rows = []

with open("input.txt", "r") as file:
    for line in file:
        rows.append(list(map(lambda x: int(x), line.strip().split(','))))

result = -1

for i in range(len(rows)):
    for j in range(i+1, len(rows)):
        x1,y1 = rows[i]
        x2,y2 = rows[j]

        space = (abs(x1-x2)+1) * (abs(y1-y2)+1)

        result = max(result, space)

print(result)