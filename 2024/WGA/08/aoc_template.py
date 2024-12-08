# aoc_template.py

import pathlib
import sys
from string import ascii_letters

def is_on_map(location, map_size):
    return location[0] >= 0 and location[0] < map_size and location[1] >= 0 and location[1] < map_size

def get_antinodes(puzzle_part, locations, map_size):
    antinodes = []

    for i in range(len(locations)):
        for j in range(i+1, len(locations)):
            vector = (locations[i][0] - locations[j][0], locations[i][1] - locations[j][1])

            for k in [-2, 1] if puzzle_part == 1 else range(-map_size, map_size):
                antinode = (locations[i][0] + k * vector[0], locations[i][1] + k * vector[1])
                
                if antinode[0] >= 0 and antinode[0] < map_size and antinode[1] >= 0 and antinode[1] < map_size:
                    antinodes.append(antinode)

    return antinodes

def parse(puzzle_input):
    """Parse input."""
    map = puzzle_input.splitlines()
    
    locations = []

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != ".":
                locations.append((i, j, map[i][j]))

    return {
        "map": map,
        "locations": locations
    }

def part1(data):
    """Solve part 1."""
    map_size = len(data["map"])
    antinodes = []

    for letter in ascii_letters:
        locations = [location for location in data["locations"] if location[2] == letter]
        
        if len(locations) > 0:
            antinodes += get_antinodes(1, locations, map_size)

    for digit in range(10):
        locations = [location for location in data["locations"] if location[2] == str(digit)]
        
        if len(locations) > 0:
            antinodes += get_antinodes(1, locations, map_size)

    return len(list(dict.fromkeys(antinodes)))

def part2(data):
    """Solve part 2."""
    map_size = len(data["map"])
    antinodes = []

    for letter in ascii_letters:
        locations = [location for location in data["locations"] if location[2] == letter]
        
        if len(locations) > 0:
            antinodes += get_antinodes(2, locations, map_size)

    for digit in range(10):
        locations = [location for location in data["locations"] if location[2] == str(digit)]
        
        if len(locations) > 0:
            antinodes += get_antinodes(2, locations, map_size)

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