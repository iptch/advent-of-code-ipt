# aoc_template.py

import pathlib
import sys

def get_number_of_options(time, distance):
    options = 0

    for j in range(1, time):
        if j * (time - j) > distance:
            options += 1

    return options

def parse(puzzle_input):
    """Parse input."""

    lines = puzzle_input.splitlines()

    maps = {"time": [], "distance": []}

    maps["time"] = [int(x) for x in lines[0].split()[1:]]
    maps["distance"] = [int(x) for x in lines[1].split()[1:]]

    return maps

def part1(data):
    """Solve part 1."""

    result = 1

    for i, time in enumerate(data["time"]):
        result *= get_number_of_options(time, data["distance"][i])

    return result

def part2(data):
    """Solve part 2."""

    time = int(''.join(map(str, data["time"])))
    distance = int(''.join(map(str, data["distance"])))

    return get_number_of_options(time, distance)

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