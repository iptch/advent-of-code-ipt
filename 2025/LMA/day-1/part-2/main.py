rows = []

with open("input.txt", "r") as file:
    for line in file:
        row = line.strip()
        row = (row[0], int(row[1:]))
        rows.append(row)

start = 50
result = 0

for row in rows:
    x = 1 if row[0] == 'R' else -1

    for _ in range(row[1]):
        start = (start + x) % 100
        if start == 0:
            result += 1

print(result)

