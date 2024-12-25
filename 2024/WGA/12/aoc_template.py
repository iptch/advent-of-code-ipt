# aoc_template.py

import pathlib
import sys

DIRECTIONS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

def get_region(x, y, map, search_log):
    plant = map[x][y]
    search_log[x][y] = plant

    areas = 1
    perimeters = 0
    sides = 0

    for dx, dy in DIRECTIONS.values():
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(map) and 0 <= ny < len(map[nx]) and plant == map[nx][ny]:
            if search_log[nx][ny] == None:
                new_areas, new_perimeters, new_sides = get_region(nx, ny, map, search_log)
                areas += new_areas
                perimeters += new_perimeters
                sides += new_sides
        else:
            perimeters += 1
    
    return (areas, perimeters, sides)

def parse(puzzle_input):
    """Parse input."""
    return [list(row) for row in puzzle_input.split()]

def part1(data):
    """Solve part 1."""
    sum = 0
    search_log = [[None] * len(row) for row in data]

    for x, row in enumerate(search_log):
        for y, cell in enumerate(row):
            if cell == None:
                areas, perimeters, _ = get_region(x, y, data, search_log)
                sum += areas * perimeters

    return sum

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