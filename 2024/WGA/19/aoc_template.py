# aoc_template.py

import pathlib
import sys
import re
from functools import lru_cache

@lru_cache(None)
def get_arrangements(design, patterns):
    if design == "":
        return 1
    
    arrangements = 0

    for pattern in patterns:
        if design.startswith(pattern):
            arrangements += get_arrangements(design[len(pattern):], patterns)

    return arrangements

def reduce_patterns(patterns):
    reduced_patterns = []

    for i, pattern in enumerate(patterns):
        regex = "(" + "|".join(patterns[:i] + patterns[i+1:]) + ")*"

        if re.fullmatch(regex, pattern) == None:
            reduced_patterns.append(pattern)

    return reduced_patterns

def parse(puzzle_input):
    """Parse input."""
    patterns, designs = puzzle_input.split("\n\n")
    patterns = tuple(patterns.split(", "))
    designs = designs.splitlines()

    return (patterns, designs)

def part1(data):
    """Solve part 1."""
    patterns, designs = data
    regex = "(" + "|".join(reduce_patterns(patterns)) + ")*"

    return sum(re.fullmatch(regex, design) != None for design in designs)

def part2(data):
    """Solve part 2."""
    patterns, designs = data

    return sum(get_arrangements(design, patterns) for design in designs)

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