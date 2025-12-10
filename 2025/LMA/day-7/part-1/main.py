rows = []

with open("input.txt", "r") as file:
    for line in file:
        rows.append(list(line.strip()))

beams = [[False for _ in range(len(rows[0]))] for _ in range(len(rows))]

for i in range(len(rows[0])):
    if rows[0][i] == 'S':
        beams[0][i] = True

split = 0

for i in range(1, len(rows)):
    for j in range(len(rows[i])):
        if rows[i][j] == '^' and beams[i-1][j]:
            has_split = False
            if j > 0 and rows[i][j-1] != '^':
                beams[i][j-1] = True
                has_split = True
            if j < len(rows[i])-1 and beams[i][j+1] != '^':
                beams[i][j+1] = True
                has_split = True
            if has_split:
                split += 1
        if rows[i][j] == '.' and beams[i-1][j]:
            beams[i][j] = True

print(split)