def do_intersect(p1, p2, l):
    x1,y1 = p1
    x2,y2 = p2
    min_x,max_x = min(x1, x2),max(x1, x2)
    min_y,max_y = min(y1, y2),max(y1, y2)
    x3,y3,x4,y4 = l

    # vertical
    if x3 == x4:
        x = x3
        if not (min_x < x < max_x):
            return False
        min_l,max_l = sorted((y3,y4))
        return max(min_l,min_y) < min(max_l,max_y)

    # horizontal
    elif y3 == y4:
        y = y3
        if not (min_y < y < max_y):
            return False
        min_l,max_l = sorted((x3,x4))
        return max(min_l,min_x) < min(max_l,max_x)

rows = []

with open("input.txt", "r") as file:
    for line in file:
        rows.append(list(map(lambda x: int(x), line.strip().split(','))))

result = -1

lines = []

for i in range(len(rows)-1):
    lines.append([rows[i][0],rows[i][1],rows[i+1][0],rows[i+1][1]])

lines.append([rows[0][0],rows[0][1],rows[len(rows)-1][0],rows[len(rows)-1][1]])

for i in range(len(rows)):
    for j in range(i+1, len(rows)):
        x1,y1 = rows[i]
        x2,y2 = rows[j]

        line_within = False
        for l in lines:
            if do_intersect(rows[i],rows[j],l):
                line_within = True
                break

        if line_within:
            continue

        space = (abs(x1-x2)+1) * (abs(y1-y2)+1)

        result = max(result, space)

print(result)