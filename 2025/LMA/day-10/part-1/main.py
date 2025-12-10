import itertools

indicator = []
wiring = []
joltage = []

with open("input.txt", "r") as file:
    for line in file:
        wiring.append([])
        temp = line.strip().split()
        for x in temp:
            if x[0] == '[':
                indicator.append(list(x[1:-1]))
            if x[0] == '(':
                wiring[-1].append(list(map(lambda x:int(x), x[1:-1].split(','))))
            if x[0] == '{':
                joltage.append(list(map(lambda x:int(x), x[1:-1].split(','))))

def does_match(perm, i):
    result = [0 for _ in range(len(indicator[i]))]

    for x in perm:
        for y in wiring[i][x]:
            result[y] = (result[y] + 1) % 2

    for idx, x in enumerate(result):
        if (x == 1 and indicator[i][idx] == '.') or (x == 0 and indicator[i][idx] == '#'):
            return False
    
    return True

result = 0

for i in range(len(wiring)):
    k = len(wiring[i])
    has_found = False
    for j in range(1, 2*k):
        perms = list(itertools.permutations(range(0, k), j))
        for x in perms:
            if does_match(x, i):
                has_found = True
                result += j
                break
        if has_found:
            break

print(result)