# aoc_template.py

import pathlib
import sys

def have_overlap(lock, key):
    for i, height in enumerate(lock):
        if height + key[i] > 5:
            return True
        
    return False

def parse(puzzle_input):
    """Parse input."""
    schematics = puzzle_input.split("\n\n")
    locks = []
    keys = []

    for schematic in schematics:
        schematic = schematic.splitlines()
        transposed = [[schematic[j][i] for j in range(len(schematic))] for i in range(len(schematic[0]))]

        if transposed[0][0] == "#":
            locks.append([len([x for x in row[1:] if x == "#"]) for row in transposed])
        else:
            keys.append([len([x for x in row[:-1] if x == "#"]) for row in transposed])

    return locks, keys

def part1(data):
    """Solve part 1."""
    locks, keys = data

    return sum([sum([0 if have_overlap(lock, key) else 1 for key in keys]) for lock in locks])

def part2(data):
    """Solve part 2."""

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