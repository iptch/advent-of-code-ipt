# aoc_template.py

import pathlib
import sys

DIRECTIONS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

def get_region(prev_plant, x, y, map, path, visited):
    plant = map[x][y]
    
    if (x, y) not in path:
        sides = 0

        if plant == prev_plant:
            path.append((x, y))
            visited[x][y] = True

            areas = 1
            perimeters = 0

            for dx, dy in DIRECTIONS.values():
                nx, ny = x + dx, y + dy

                if 0 <= nx < len(map) and 0 <= ny < len(map[nx]):
                    res = get_region(plant, nx, ny, map, path, visited)
                    areas += res[0]
                    perimeters += res[1]
                else:
                    perimeters += 1
            
            return (areas, perimeters, sides)

        return (0, 1, sides)
    
    return (0, 0, 0)

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
                areas, perimeters, _ = get_region(cell, x, y, data, [], visited)
                sum += areas * perimeters

    return sum

def part2(data):
    """Solve part 2."""
    sum = 0
    visited = [[False] * len(row) for row in data]

    for x, row in enumerate(data):
        for y, cell in enumerate(row):
            if not visited[x][y]:
                areas, _, sides = get_region(cell, x, y, data, [], visited)
                sum += areas * sides

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