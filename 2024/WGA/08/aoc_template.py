# aoc_template.py

import pathlib
import sys
from string import ascii_letters

FREQUENCIES = ascii_letters + "0123456789"

def get_antinodes(puzzle_part, locations, map_size):
    antinodes = []

    for i, (x1, y1) in enumerate(locations):
        for x2, y2 in locations[i+1:]:
            dx, dy = x1 - x2, y1 - y2

            for k in [-2, 1] if puzzle_part == 1 else range(-map_size, map_size):
                nx, ny = x1 + k * dx, y1 + k * dy
                
                if nx >= 0 and nx < map_size and ny >= 0 and ny < map_size:
                    antinodes.append((nx, ny))

    return antinodes

def parse(puzzle_input):
    """Parse input."""
    map = puzzle_input.splitlines()
    locations = []

    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if cell != ".":
                locations.append((x, y, cell))

    return map, locations

def part1(data):
    """Solve part 1."""
    map, locations = data
    antinodes = []

    for frequency in FREQUENCIES:
        locations_filtered = [(x, y) for x, y, f in locations if f == frequency]
        antinodes += get_antinodes(1, locations_filtered, len(map))

    return len(list(dict.fromkeys(antinodes)))

def part2(data):
    """Solve part 2."""
    map, locations = data
    antinodes = []

    for frequency in FREQUENCIES:
        locations_filtered = [(x, y) for x, y, f in locations if f == frequency]
        antinodes += get_antinodes(2, locations_filtered, len(map))

    return len(list(dict.fromkeys(antinodes)))

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