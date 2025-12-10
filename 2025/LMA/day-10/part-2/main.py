import numpy as np
from scipy.optimize import LinearConstraint, Bounds, milp

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

result = 0

for i in range(len(wiring)):
    k = len(wiring[i])
    c = np.array([1.0 for _ in range(k)])

    temp = [[0]*k for _ in range(len(joltage[i]))]

    for idx, x in enumerate(wiring[i]):
        for j in range(len(joltage[i])):
            if j in x:
                temp[j][idx] = 1

    A = np.array(temp,dtype=float)
    b_u = np.array(joltage[i],dtype=float)
    b_l = np.array(joltage[i],dtype=float)

    constraints = LinearConstraint(A, b_l, b_u)
    integrality = np.ones_like(c)
    bounds = Bounds(0, np.inf)

    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)

    result += int(np.round(np.sum(res.x)))

print(result)