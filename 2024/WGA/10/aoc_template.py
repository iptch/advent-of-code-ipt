# aoc_template.py

import pathlib
import sys

def get_peaks(i, j, data, prev_height):
    curr_height = data[i][j]

    if curr_height == prev_height + 1:
        if curr_height == 9:
            return [(i, j)]
        else:
            score = []

            if i-1 >= 0:
                score += get_peaks(i-1, j, data, curr_height)
            if i+1 < len(data):
                score += get_peaks(i+1, j, data, curr_height)
            if j-1 >= 0:
                score += get_peaks(i, j-1, data, curr_height)
            if j+1 < len(data[i]):
                score += get_peaks(i, j+1, data, curr_height)

            return score

    return []

def parse(puzzle_input):
    """Parse input."""
    return [[int(x) for x in row] for row in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""
    sum = 0

    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell == 0:
                sum += len(list(dict.fromkeys(get_peaks(i, j, data, -1))))

    return sum

def part2(data):
    """Solve part 2."""
    sum = 0

    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell == 0:
                sum += len((get_peaks(i, j, data, -1)))

    return sum

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))