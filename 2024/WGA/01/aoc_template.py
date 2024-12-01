# aoc_template.py

import pathlib
import sys
import math

def parse(puzzle_input):
    """Parse input."""
    rows = puzzle_input.splitlines()

    col1 = [int(row.split()[0]) for row in rows]
    col2 = [int(row.split()[1]) for row in rows]
    
    return [col1, col2]

def part1(data):
    """Solve part 1."""

    sum = 0

    data_left = data[0].copy()
    data_right = data[1].copy()

    for i in range(len(data_left)):
        min_left = min(data_left)
        data_left[data_left.index(min_left)] = math.inf

        min_right = min(data_right)
        data_right[data_right.index(min_right)] = math.inf

        sum += abs(min_left - min_right)

    return sum

def part2(data):
    """Solve part 2."""

    sum = 0

    for x in data[0]:
        sum += x * data[1].count(x)

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