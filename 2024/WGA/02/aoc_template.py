# aoc_template.py

import pathlib
import sys
import statistics

def parse(puzzle_input):
    """Parse input."""
    rows = puzzle_input.splitlines()

    for i in range(len(rows)):
        rows[i] = [int(item) for item in rows[i].split()]
    
    return rows

def part1(data):
    """Solve part 1."""

    count = 0

    for row in data:
        diff = [j-i for i, j in zip(row[:-1], row[1:])]

        if all(i >= 1 and i <= 3 for i in diff) or all(i <= -1 and i >= -3 for i in diff):
            count += 1

    return count

def part2(data):
    """Solve part 2."""

    count = 0

    for row in data:
        diff = [j - i for i, j in zip(row[:-1], row[1:])]

        if all(i >= 1 and i <= 3 for i in diff) or all(i <= -1 and i >= -3 for i in diff):
            count += 1
        else:
            for n in range(len(row)):
                tmp = row.copy()
                tmp.pop(n)

                diff = [j - i for i, j in zip(tmp[:-1], tmp[1:])]

                if all(i >= 1 and i <= 3 for i in diff) or all(i <= -1 and i >= -3 for i in diff):
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