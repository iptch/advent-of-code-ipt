rows = []

with open("input.txt", "r") as file:
    for line in file:
        rows.append(list(line.strip()))

timelines = [[1 if rows[i][j] == 'S' else 0 for j in range(len(rows[0]))] for i in range(len(rows))]

for i in range(1, len(rows)):
    for j in range(len(rows[i])):
        if rows[i][j] == '^':
            if j > 0 and rows[i][j-1] != '^':
                timelines[i][j-1] += timelines[i-1][j]
            if j < len(rows[i])-1 and rows[i][j+1] != '^':
                timelines[i][j+1] += timelines[i-1][j]
        if rows[i][j] == '.':
            timelines[i][j] += timelines[i-1][j]

print(sum(timelines[-1]))