# aoc_template.py

import pathlib
import sys

def is_safe(row):
    diff = [j-i for i, j in zip(row[:-1], row[1:])]

    return all(i >= 1 and i <= 3 for i in diff) or all(i <= -1 and i >= -3 for i in diff)

def parse(puzzle_input):
    """Parse input."""

    return [[int(item) for item in row.split()] for row in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""

    return sum([1 if is_safe(row) else 0 for row in data])

def part2(data):
    """Solve part 2."""

    count = 0

    for row in data:
        if is_safe(row):
            count += 1
        else:
            for n in range(len(row)):
                tmp = row.copy()
                tmp.pop(n)

                if is_safe(tmp):
                    count += 1
                    break

    return count

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