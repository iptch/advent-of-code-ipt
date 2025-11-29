# aoc_template.py

import pathlib
import sys
import re

sys.setrecursionlimit(10000)

DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

def get_distinct_positions(route):
    distinct_positions = {}

    for x, y, dir in route:
        if (x, y) not in distinct_positions:
            distinct_positions[(x, y)] = (x, y, dir)

    return list(distinct_positions.values())

def patrol(route, map):
    x, y, dir = route[-1]
    dx, dy = DIRECTIONS[dir]
    nx, ny = x + dx, y + dy
    ndir = list(DIRECTIONS)[(list(DIRECTIONS).index(dir)+1)%4]

    if nx < 0 or nx >= len(map) or ny < 0 or ny >= len(map[nx]):
        return (route, False)
    elif map[nx][ny] == "#":
        return patrol(route + [(x, y, ndir)], map)
    else:
        if (nx, ny, dir) in route:
            return (route, True)
        else:
            return patrol(route + [(nx, ny, dir)], map)

def parse(puzzle_input):
    """Parse input."""
    map = [row for row in puzzle_input.splitlines()]
    x_start = y_start = dir_start = None

    for i, row in enumerate(map):
        match = re.search(r"\^|>|v|<", row)
        map[i] = list(row)

        if match:
            x_start, y_start, dir_start = i, match.start(), row[match.start()]

    return map, (x_start, y_start, dir_start)

def part1(data):
    """Solve part 1."""
    map, start = data

    return len(get_distinct_positions(patrol([start], map)[0]))

def part2(data):
    """Solve part 2."""
    map, start = data
    distinct_positions = get_distinct_positions(patrol([start], map)[0])
    sum = 0

    for i, (x, y, dir) in enumerate(distinct_positions[1:]):
        map[x][y] = "#"

        if patrol([distinct_positions[i-1]], map)[1]:
            sum += 1

        map[x][y] = "."

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