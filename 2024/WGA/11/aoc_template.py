# aoc_template.py

import pathlib
import sys
from functools import lru_cache

@lru_cache(None)
def blink(number, iter):
    if iter > 0:
        s = str(number)
        no_of_digits = len(s)
        
        if number == 0:
            return blink(1, iter-1)
        elif no_of_digits % 2 == 0:
            half = 10 ** (no_of_digits // 2)

            return blink(number // half, iter-1) + blink(number % half, iter-1)
        
        return blink(number*2024, iter-1)
    
    return 1

def parse(puzzle_input):
    """Parse input."""
    return list(map(int, puzzle_input.split()))

def part1(data):
    """Solve part 1."""

    return sum(blink(number, 25) for number in data)

def part2(data):
    """Solve part 2."""

    return sum(blink(number, 75) for number in data)

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