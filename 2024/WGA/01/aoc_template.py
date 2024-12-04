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

    data[0].sort()
    data[1].sort()

    for i in range(len(data[0])):
        sum += abs(data[0][i] - data[1][i])

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