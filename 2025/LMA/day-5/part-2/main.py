import bisect

rows = []
ings = []

blank = False

with open("input.txt", "r") as file:
    for line in file:
        if len(line.strip()) == 0:
            blank = True
            continue
        
        if not blank:
            x, y = line.strip().split('-')
            rows.append((int(x), int(y)))
        else:
            ings.append(int(line.strip()))

rows = sorted(rows, key=lambda x: x[0])

ranges = []

left = rows[0][0]
right = rows[0][1]

for x, y in rows[1:]:
    if x > right:
        ranges.append([left,right])

        left = x
        right = y
    
    else:
        right = max([right, y])

ranges.append([left,right])

result = 0

for x,y in ranges:
    result += y - x + 1

print(result)
    

