# aoc_template.py

import pathlib
import sys

def get_joltage(bank, n):
    idx = 0
    joltage = ""

    for i in range(n):
        search_window = bank[idx:len(bank)-n+1+i]
        val = max(search_window)
        idx = search_window.index(val) + idx + 1
        joltage += str(val)

    return int(joltage)

def parse(puzzle_input):
    """Parse input."""

    return [[int(i) for i in list(row)] for row in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""

    return sum([get_joltage(row, 2) for row in data])

def part2(data):
    """Solve part 2."""

    return sum([get_joltage(row, 12) for row in data])

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