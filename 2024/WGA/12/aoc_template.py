# aoc_template.py

import pathlib
import sys

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIAGONALS = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

def is_on_map(x, y, map):
    return 0 <= x < len(map) and 0 <= y < len(map[x])

def get_inner_corners(x, y, map):
    plant = map[x][y]
    corners = 0

    for diag in DIAGONALS:
        dx, dy = diag
        nx, ny = x + dx, y + dy

        if (is_on_map(nx, ny, map) and plant != map[nx][ny] and
            is_on_map(x, ny, map) and plant == map[x][ny] and
            is_on_map(nx, y, map) and plant == map[nx][y]):
            corners += 1

    return corners

def get_outer_corners(x, y, map):
    plant = map[x][y]
    corners = 0

    for diag in DIAGONALS:
        dx, dy = diag
        nx, ny = x + dx, y + dy

        if ((not is_on_map(x, ny, map) or plant != map[x][ny]) and
            (not is_on_map(nx, y, map) or plant != map[nx][y])):
            corners += 1

    return corners

def get_region(x, y, map, visited):
    plant = map[x][y]
    visited[x][y] = True
    areas, perimeters, sides = 1, 0, 0

    for i in range(len(DIRECTIONS)):
        dx, dy = DIRECTIONS[i]
        nx, ny = x + dx, y + dy

        if is_on_map(nx, ny, map) and plant == map[nx][ny]:
            if not visited[nx][ny]:
                new_areas, new_perimeters, new_sides = get_region(nx, ny, map, visited)
                areas += new_areas
                perimeters += new_perimeters
                sides += new_sides
        else:
            perimeters += 1
    
    sides += get_inner_corners(x, y, map)
    sides += get_outer_corners(x, y, map)
    
    return (areas, perimeters, sides)

def parse(puzzle_input):
    """Parse input."""
    return [list(row) for row in puzzle_input.split()]

def part1(data):
    """Solve part 1."""
    sum = 0
    visited = [[False] * len(row) for row in data]

    for x, row in enumerate(visited):
        for y, cell in enumerate(row):
            if not cell:
                areas, perimeters, _ = get_region(x, y, data, visited)
                sum += areas * perimeters

    return sum

def part2(data):
    """Solve part 2."""
    sum = 0
    visited = [[None] * len(row) for row in data]

    for x, row in enumerate(visited):
        for y, cell in enumerate(row):
            if not cell:
                areas, _, sides = get_region(x, y, data, visited)
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