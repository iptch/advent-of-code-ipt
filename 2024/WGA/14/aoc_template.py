# aoc_template.py

import pathlib
import sys
import re

def simulate(x, y, dx, dy, x_limit, y_limit, t):
    if t < 100:
        new_x = x + dx
        new_y = y + dy

        if new_x < 0:
            new_x += x_limit
        elif new_x >= x_limit:
            new_x -= x_limit

        if new_y < 0:
            new_y += y_limit
        elif new_y >= y_limit:
            new_y -= y_limit

        return simulate(new_x, new_y, dx, dy, x_limit, y_limit, t+1)

    return (x, y)

def parse(puzzle_input):
    """Parse input."""
    return [[int(i) for i in re.findall(r"-?\d+", row)] for row in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""
    x_limit = max([row[0] for row in data]) + 1
    y_limit = max([row[1] for row in data]) + 1

    end_positions = [simulate(row[0], row[1], row[2], row[3], x_limit, y_limit, 0) for row in data]

    safety_factor = len([i for i in end_positions if i[0] < x_limit/2-1 and i[1] < y_limit/2-1])
    safety_factor *= len([i for i in end_positions if i[0] > x_limit/2 and i[1] < y_limit/2-1])
    safety_factor *= len([i for i in end_positions if i[0] < x_limit/2-1 and i[1] > y_limit/2])
    safety_factor *= len([i for i in end_positions if i[0] > x_limit/2 and i[1] > y_limit/2])

    return safety_factor

def part2(data):
    """Solve part 2."""

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