rows = []

with open("input.txt", "r") as file:
    for line in file:
        rows.append(line.strip().split())
        
for i in range(len(rows[:-1])):
    rows[i] = list(map(lambda x: int(x), rows[i]))

result = 0
for j in range(len(rows[0])):
    temp = rows[0][j]
    for i in range(1, len(rows[:-1])):
        if rows[-1][j] == '+':
            temp += rows[i][j]
        else:
            temp *= rows[i][j]
    result += temp

print(result)