# aoc_template.py

import pathlib
import sys
import re

sys.setrecursionlimit(10000)

REGEX = r"\^|>|v|<"

def rmv_duplicate_positions(route):
    distict_positions = [route[0]]

    for i in range(1, len(route)):
        if (route[i][0], route[i][1]) in [(x[0], x[1]) for x in distict_positions]:
            continue
        else:
            distict_positions.append(route[i])

    return distict_positions

def patrol(route, map):
    position_u = (route[-1][0]-1, route[-1][1])
    position_r = (route[-1][0], route[-1][1]+1)
    position_d = (route[-1][0]+1, route[-1][1])
    position_l = (route[-1][0], route[-1][1]-1)

    if route[-1][2] == "^":
        if position_u[0] < 0:
            return False
        elif map[position_u[0]][position_u[1]] == "#":
            route.append((route[-1][0], route[-1][1], ">"))
            return patrol(route, map)
        else:
            if (position_u[0], position_u[1], "^") in route:
                return True
            else:
                route.append((position_u[0], position_u[1], "^"))
                return patrol(route, map)
    elif route[-1][2] == ">":
        if position_r[1] > len(map[0])-1:
            return False
        elif map[position_r[0]][position_r[1]] == "#":
            route.append((route[-1][0], route[-1][1], "v"))
            return patrol(route, map)
        else:
            if (position_r[0], position_r[1], ">") in route:
                return True
            else:
                route.append((position_r[0], position_r[1], ">"))
                return patrol(route, map)
    elif route[-1][2] == "v":
        if position_d[0] > len(map)-1:
            return False
        elif map[position_d[0]][position_d[1]] == "#":
            route.append((route[-1][0], route[-1][1], "<"))
            return patrol(route, map)
        else:
            if (position_d[0], position_d[1], "v") in route:
                return True
            else:
                route.append((position_d[0], position_d[1], "v"))
                return patrol(route, map)
    else:
        if position_l[1] < 0:
            return False
        elif map[position_l[0]][position_l[1]] == "#":
            route.append((route[-1][0], route[-1][1], "^"))
            return patrol(route, map)
        else:
            if (position_l[0], position_l[1], "<") in route:
                return True
            else:
                route.append((position_l[0], position_l[1], "<"))
                return patrol(route, map)

def find_start_position(map):
    for i in range(len(map)):
        res = re.search(REGEX, "".join(map[i]))

        if res:
            return (i, res.start(), map[i][res.start()])

    return None

def parse(puzzle_input):
    """Parse input."""
    return [list(row) for row in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""
    route = [find_start_position(data)]
    patrol(route, data)
    distinct_positions = rmv_duplicate_positions(route)

    return len(distinct_positions)

def part2(data):
    """Solve part 2."""
    route = [find_start_position(data)]
    patrol(route, data)
    distinct_positions = rmv_duplicate_positions(route)

    sum = 0

    for i in range(1, len(distinct_positions)):
        data[distinct_positions[i][0]][distinct_positions[i][1]] = "#"
        has_loop = patrol([distinct_positions[0]], data)

        if has_loop:
            sum += 1

        data[distinct_positions[i][0]][distinct_positions[i][1]] = "."

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