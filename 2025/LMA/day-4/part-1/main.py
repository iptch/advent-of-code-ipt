rows = []

def cnt(x, y):
    if rows[x][y] == '@':
        return 1
    return 0

def is_free(x, y):
    count = 0

    for i in [x-1,x,x+1]:
        for j in [y-1,y,y+1]:
            if not (i == x and j == y):
                if i >= 0 and i < len(rows) and j >= 0 and j < len(rows[i]):
                    count += cnt(i,j)

    return count < 4


with open("test.txt", "r") as file:
    for line in file:
        rows.append(list(str(line.strip())))

result = 0

for i in range(len(rows)):
    for j in range(len(rows[i])):
        if rows[i][j] == '@' and is_free(i,j):
            result += 1

print(result)

