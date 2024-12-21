# aoc_template.py

import pathlib
import sys

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_areas_perimeters(prev_plant, x, y, map, path, visited):
    plant = map[x][y]
    
    if (x, y) not in path:
        if plant == prev_plant:
            path.append((x, y))
            visited[x][y] = True

            areas = 1
            perimeters = 0

            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy

                if 0 <= nx < len(map) and 0 <= ny < len(map[nx]):
                    res = get_areas_perimeters(plant, nx, ny, map, path, visited)
                    areas += res[0]
                    perimeters += res[1]
                else:
                    perimeters += 1
            
            return (areas, perimeters)

        return (0, 1)
    
    return (0, 0)

def parse(puzzle_input):
    """Parse input."""
    return [list(row) for row in puzzle_input.split()]

def part1(data):
    """Solve part 1."""
    sum = 0
    visited = [[False] * len(row) for row in data]

    for x, row in enumerate(data):
        for y, cell in enumerate(row):
            if not visited[x][y]:
                path = []
                areas_perimeters = get_areas_perimeters(cell, x, y, data, path, visited)
                sum += areas_perimeters[0] * areas_perimeters[1]

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