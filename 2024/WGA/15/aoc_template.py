# aoc_template.py

import pathlib
import sys
import copy

sys.setrecursionlimit(25000)

DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

def get_start(map):
    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if cell == "@":
                return x, y
    
    raise ValueError("No start position found")

def get_gps(map):
    sum = 0

    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if cell in ["O", "["]:
                sum += 100 * x + y

    return sum

def push_slim_boxes(x, y, dx, dy, map):
    nx, ny = x + dx, y + dy

    if map[nx][ny] == "#":
        return False
    elif map[nx][ny] == "." or map[nx][ny] in ["O", "[", "]"] and push_slim_boxes(nx, ny, dx, dy, map):
        map[nx][ny], map[x][y] = map[x][y], map[nx][ny]
        return True
    
    return False

def push_wide_boxes(x, y, dx, map):
    nx = x + dx
    ny1 = y
    ny2 = y + 1 if map[x][y] == "[" else y - 1

    if map[nx][ny1] == "#" or map[nx][ny2] == "#":
        return False
    
    elif (map[nx][ny1] == "." and map[nx][ny2] == "." or
          map[nx][ny1] == map[x][ny1] and map[nx][ny2] == map[x][ny2] and push_wide_boxes(nx, ny1, dx, map) or
          map[nx][ny1] == map[x][ny2] and map[nx][ny2] == map[x][ny1] and push_wide_boxes(nx, ny1, dx, map) and push_wide_boxes(nx, ny2, dx, map) or
          map[nx][ny1] == map[x][ny2] and map[nx][ny2] == "." and push_wide_boxes(nx, ny1, dx, map) or
          map[nx][ny2] == map[x][ny1] and map[nx][ny1] == "." and push_wide_boxes(nx, ny2, dx, map)):
        map[nx][ny1], map[x][ny1] = map[x][ny1], map[nx][ny1]
        map[nx][ny2], map[x][ny2] = map[x][ny2], map[nx][ny2]
        return True
    
    return False

def move(x, y, map, movements):
    if len(movements) == 0:
        return
    
    dx, dy = DIRECTIONS[movements[0]]
    nx, ny = x + dx, y + dy
    
    if (map[nx][ny] == "." or
        map[nx][ny] == "O" and push_slim_boxes(nx, ny, dx, dy, map) or
        map[nx][ny] in ["[", "]"] and dx == 0 and push_slim_boxes(nx, ny, dx, dy, map) or
        map[nx][ny] in ["[", "]"] and dy == 0 and push_wide_boxes(nx, ny, dx, map)):
        map[nx][ny], map[x][y] = map[x][y], map[nx][ny]
        return move(nx, ny, map, movements[1:])

    return move(x, y, map, movements[1:])

def parse(puzzle_input):
    """Parse input."""
    map, movements = puzzle_input.split("\n\n")
    map = [list(row) for row in map.splitlines()]

    return map, movements.replace("\n","")

def part1(data):
    """Solve part 1."""
    map, movements = data
    map = copy.deepcopy(map)

    x_start, y_start = get_start(map)

    move(x_start, y_start, map, movements)

    return get_gps(map)

def part2(data):
    """Solve part 2."""
    map, movements = data
    map = copy.deepcopy(map)

    for x, row in enumerate(map):
        map[x] = list("".join(row).replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@."))

    x_start, y_start = get_start(map)

    move(x_start, y_start, map, movements)

    # Works with example but not with input
    for row in map:
        print("".join(row))

    return get_gps(map)

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