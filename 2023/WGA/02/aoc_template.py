# aoc_template.py

import pathlib
import sys
import re

COLORS = ["red", "green", "blue"]

def parse_cubes(set):
    cubes = [0, 0, 0]

    for i, colors in enumerate(COLORS):
        match = re.findall(r"\d+ " + colors, set)
        
        if len(match) > 0:
            cubes[i] += int(match[0].split()[0])

    return cubes

def parse(puzzle_input):
    """Parse input."""
    return [[parse_cubes(set) for set in game.split("; ")] for game in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""
    red_max, green_max, blue_max = 12, 13, 14
    sum = 0

    for i, game in enumerate(data):
        red = max([set[0] for set in game])
        green = max([set[1] for set in game])
        blue = max([set[2] for set in game])

        if red <= red_max and green <= green_max and blue <= blue_max:
            sum += i + 1

    return sum

def part2(data):
    """Solve part 2."""
    sum = 0

    for game in data:
        red = max([set[0] for set in game])
        green = max([set[1] for set in game])
        blue = max([set[2] for set in game])

        sum += red * green * blue

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