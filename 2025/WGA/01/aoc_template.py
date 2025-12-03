# aoc_template.py

import pathlib
import sys

MAX_POS = 100

def dial(old_pos, rotation):    
    dir = 1 if rotation[0] == "R" else -1
    dist = int(rotation[1:])

    new_pos = old_pos + dir * dist
    quotient, remainder = divmod(new_pos, MAX_POS)
    
    if dir == -1:
        if old_pos == 0:
            quotient += 1
        if remainder == 0:
            quotient -= 1
    
    return remainder, abs(quotient)

def parse(puzzle_input):
    """Parse input."""
    
    return puzzle_input.splitlines()

def part1(data):
    """Solve part 1."""

    res = 0
    pos = 50

    for rotation in data:
        pos, _ = dial(pos, rotation)

        if pos == 0:
            res += 1

    return res

def part2(data):
    """Solve part 2."""

    res = 0
    pos = 50

    for rotation in data:
        pos, clicks = dial(pos, rotation)
        res += clicks

    return res

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