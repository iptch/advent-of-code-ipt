# aoc_template.py

import pathlib
import sys
import re
from numpy import array, flipud

def parse(puzzle_input):
    """Parse input."""
    return array([list(row) for row in puzzle_input.splitlines()])

def part1(data):
    """Solve part 1."""
    REGEX = "(?=(XMAS|SAMX))"
    sum = 0

    for row in data:
        sum += len(re.findall(REGEX, "".join(row)))

    for row in data.transpose():
        sum += len(re.findall(REGEX, "".join(row)))

    for i in range(-len(data[0])+1, len(data[0])):
        main_diag = data.diagonal(i)
        sum += len(re.findall(REGEX, "".join(main_diag)))

    flipped = flipud(data)

    for i in range(-len(data[0])+1, len(data[0])):
        main_diag = flipped.diagonal(i).tolist()
        sum += len(re.findall(REGEX, "".join(main_diag)))

    return sum

def part2(data):
    """Solve part 2."""
    REGEX = "MAS|SAM"
    sum = 0

    for i in range(len(data[0]) - 2):
        for j in range(len(data[0]) - 2):
            a = data[i:i+3, j:j+3]

            if re.search(REGEX, "".join(a.diagonal())) and re.search(REGEX, "".join(flipud(a).diagonal())):
                sum += 1

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