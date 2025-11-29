# aoc_template.py

import pathlib
import sys

def get_x_expansion_pts(map):
    x_expanstion_pts = []

    for x, row in enumerate(map):
        if all(cell == "." for cell in row):
            x_expanstion_pts.append(x)

    return x_expanstion_pts

def get_y_expansion_pts(map):
    y_expansion_pts = []

    for y in range(len(map[0])):
        if all(cell == "." for cell in [row[y] for row in map]):
            y_expansion_pts.append(y)

    return y_expansion_pts

def get_galaxies(map):
    galaxies = []
    
    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if cell == "#":
                galaxies.append((x, y))

    return galaxies

def get_galaxy_pairs(galaxies):
    pairs = []

    for i, g1 in enumerate(galaxies[:-1]):
        for g2 in galaxies[i+1:]:
            pairs.append([g1, g2])

    return pairs

def get_shortest_dist(g1, g2, x_expansion_pts, y_expansion_pts, expansion_factor):
    x1, y1 = g1
    x2, y2 = g2

    x = [x for x in x_expansion_pts if x in range(x1 + 1, x2) or x in range(x2 + 1, x1)]
    y = [y for y in y_expansion_pts if y in range(y1 + 1, y2) or y in range(y2 + 1, y1)]

    return abs(x1 - x2) + abs(y1 - y2) + (expansion_factor - 1) * (len(x) + len(y))

def parse(puzzle_input):
    """Parse input."""
    map = puzzle_input.splitlines()
    
    return get_galaxy_pairs(get_galaxies(map)), get_x_expansion_pts(map), get_y_expansion_pts(map)

def part1(data):
    """Solve part 1."""
    pairs, x_expansion_pts, y_expansion_pts = data

    return sum([get_shortest_dist(g1, g2, x_expansion_pts, y_expansion_pts, 2) for g1, g2 in pairs])

def part2(data):
    """Solve part 2."""
    pairs, x_expansion_pts, y_expansion_pts = data

    return sum([get_shortest_dist(g1, g2, x_expansion_pts, y_expansion_pts, 1000000) for g1, g2 in pairs])

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