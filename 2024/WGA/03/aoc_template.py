# aoc_template.py

import pathlib
import sys
import re

def parse(puzzle_input):
    """Parse input."""

    return puzzle_input

def part1(data):
    """Solve part 1."""
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", data)

    sum = 0

    for match in matches:
        num = re.findall("\d{1,3}", match)
        sum += int(num[0]) * int(num[1])

    return sum

def part2(data):
    """Solve part 2."""
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data)

    sum = 0
    do_multiply = True

    for match in matches:
        if match == "do()":
            do_multiply = True
        elif match == "don't()":
            do_multiply = False
        elif do_multiply:
            num = re.findall("\d{1,3}", match)
            sum += int(num[0]) * int(num[1])

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