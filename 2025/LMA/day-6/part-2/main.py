rows = []

with open("input.txt", "r") as file:
    for line in file:
        rows.append(list(line)[:-1])

separator = [True for _ in range(len(rows[0]))]

for j in range(len(rows[0])):
    for i in range(0, len(rows[:-1])):
        if rows[i][j] != ' ':
            separator[j] = False
            break

count_blocks = sum(separator)+1

blocks = [[] for _ in range(count_blocks)]
blocks_ops = []

ctr_block = 0

for j in range(len(rows[0])):
    if separator[j]:
        ctr_block += 1
        continue

    number = ''
    for i in range(0, len(rows[:-1])):
        number += rows[i][j]

    blocks[ctr_block].append(int(number.strip()))

    if rows[-1][j] in ['+','*']:
        blocks_ops.append(rows[-1][j])

result = 0
for i in range(len(blocks)):
    if blocks_ops[i] == '+':
        result += sum(blocks[i])
    else:
        temp = 1
        for x in blocks[i]:
            temp *= x
        result += temp

print(result)