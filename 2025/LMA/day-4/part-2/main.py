rows = []
queue = []

def cnt(x, y):
    if rows[x][y] == '@':
        return 1
    return 0

def is_free(x, y):
    global queue
    count = 0

    if rows[x][y] == '.':
        return False

    candidates = []

    for i in [x-1,x,x+1]:
        for j in [y-1,y,y+1]:
            if not (i == x and j == y):
                if i >= 0 and i < len(rows) and j >= 0 and j < len(rows[i]):
                    count += cnt(i,j)
                    if rows[i][j] == '@':
                        candidates.append((i,j))

    if count < 4:
        queue = queue + candidates
        return True
    else:
        return False

with open("input.txt", "r") as file:
    for line in file:
        rows.append(list(str(line.strip())))

result = 0

for i in range(len(rows)):
    for j in range(len(rows[i])):
        if rows[i][j] == '@' and is_free(i,j):
            rows[i][j] = '.'
            result += 1

while len(queue) > 0:
    (x,y) = queue.pop(0)
    if is_free(x,y):
        rows[x][y] = '.'
        result += 1

print(result)

