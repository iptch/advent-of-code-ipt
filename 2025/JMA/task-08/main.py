import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def get_adjacents(diagram):
    solution = 0
    new_diagram = []
    windows = sliding_window_view(diagram, (3, 3))
    for window in windows:
        new_row_diagram = []
        for row in window:
            if row[1][1] == 1:
                window_sum = (row * np.asarray([[1, 1, 1], [1, 0, 1], [1, 1, 1]])).sum() * row[1][1]
                if window_sum < 4:
                    solution += 1
                    new_row_diagram.append(0)
                else:
                    new_row_diagram.append(1)
            else:
                new_row_diagram.append(0)
        new_diagram.append(new_row_diagram)
    return solution, new_diagram


def solve(input):
    diagram = []
    with open(input, 'r') as f:
        for line in f.readlines():
            row = []
            for c in line:
                if c == '.':
                    row.append(0)
                elif c == '@':
                    row.append(1)
                else:
                    continue
            diagram.append(row)
    diagram = np.asmatrix(diagram)
    solution = 0
    while True:
        diagram = np.pad(np.asmatrix(diagram), 1)
        removed, new_matrix = get_adjacents(diagram)
        if removed == 0:
            return solution
        solution += removed
        diagram = new_matrix


if __name__ == '__main__':
    print(solve("input.txt"))
