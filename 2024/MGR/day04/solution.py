import sys, math, re
from collections import defaultdict

file = open("/home/manuelgr/advent-of-code-ipt/2024/MGR/day04/input.txt", "r")

def diagonalOrderUp(matrix):
    ROW = len(matrix)
    COL = len(matrix[-1])
    
    matrix_diagonal = []
    for line in range(1, (ROW + COL)): 
        start_col = max(0, line - ROW) 
        count = min(line, (COL - start_col), ROW) 

        l = []
        for j in range(0, count):
            l.append(matrix[min(ROW, line) - j - 1][start_col + j])
        matrix_diagonal.append(list(l))    
  
    return matrix_diagonal

def diagonalOrderDown(matrix):
    ROW = len(matrix)
    COL = len(matrix[-1])
    
    d = defaultdict(list)
    for y in range(ROW):
        for x in range(COL):
            d[x-y].append(matrix[y][x])
    return d

matrix = []
sum = 0

while True:
    line = file.readline()
    if not line:
        break
    
    xmas_horizontal = re.findall('XMAS', line)
    xmas_backwards = re.findall('SAMX', line)
    #print(line + " - " + str(xmas_horizontal) + " - " + str(len(xmas_horizontal)))
    sum += len(xmas_horizontal)
    sum += len(xmas_backwards)
    
    matrix.append(list(line))

file.close()

zip_matrix = list(zip(*matrix))
for line in zip_matrix:
    line_string = ''.join(line)
    xmas_vertical = re.findall('XMAS', line_string)
    xmas_vertical_upside_down = re.findall('SAMX', line_string)
    sum += len(xmas_vertical)
    sum += len(xmas_vertical_upside_down)

#diagonal

matrix_diagonal_up = diagonalOrderUp(matrix)
for line in matrix_diagonal_up:
    line_string = ''.join(line)
    xmas_diagonal_up = re.findall('XMAS', line_string)
    xmas_diagonal_up_backwards = re.findall('SAMX', line_string)
    sum += len(xmas_diagonal_up)
    sum += len(xmas_diagonal_up_backwards)

matrix_diagonal_down = diagonalOrderDown(matrix)
for _, v in matrix_diagonal_down.items():
    line_string = ''.join(v)
    xmas_diagonal_down = re.findall('XMAS', line_string)
    xmas_diagonal_down_backwards = re.findall('SAMX', line_string)
    sum += len(xmas_diagonal_down)
    sum += len(xmas_diagonal_down_backwards)

sum_xmas = 0
for i in range(1, len(matrix)-1):
    for j in range(1, len(matrix[-1])-1):
        #print(str(len(matrix)-2) + " - " + str(len(matrix[0])-2))
        #print(str(i) + " - " + str(j))
        if matrix[i][j] == 'A':
            if matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M' \
                or matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S':
                    if matrix[i+1][j-1] == 'S' and matrix[i-1][j+1] == 'M' \
                        or matrix[i+1][j-1] == 'M' and matrix[i-1][j+1] == 'S':
                            sum_xmas += 1

print(sum)
print(sum_xmas)