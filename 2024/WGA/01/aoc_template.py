# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    rows = puzzle_input.splitlines()
    col1 = [int(row.split()[0]) for row in rows]
    col2 = [int(row.split()[1]) for row in rows]
    
    return col1, col2

def part1(data):
    """Solve part 1."""
    col1, col2 = data
    col1.sort()
    col2.sort()

    return sum([abs(x - col2[i]) for i, x in enumerate(col1)])

def part2(data):
    """Solve part 2."""
    col1, col2 = data

    return sum([x * col2.count(x) for x in col1])

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