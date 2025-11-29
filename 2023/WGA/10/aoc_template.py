# aoc_template.py

import pathlib
import sys

sys.setrecursionlimit(20000)

DIRECTIONS = [(-1, 0, ["J", "|", "L"]), (0, 1, ["L", "-", "F"]), (1, 0, ["F", "|", "7"]), (0, -1, ["7", "-", "J"])]

def get_path(tile, path, map):
    x, y, t = tile

    if tile in path:
        return path   

    paths = [path + [tile]]

    for i, (dx, dy, pipes) in enumerate(DIRECTIONS):
        nx, ny = x + dx, y + dy

        if nx >= 0 and nx < len(map) and ny >= 0 and ny < len(map[nx]):
            nt = map[nx][ny]

            if (t in pipes + ["S"]) and (nt in DIRECTIONS[(i+2)%4][2] + ["S"]):
                paths.append(get_path((nx, ny, nt), paths[0], map))

    return max(paths, key=lambda x: len(x))

def get_enclosed_tiles(path, map):
    enclosed_tiles = []

    for x, row in enumerate(map):
        intersection_counter = 0

        for y, cell in enumerate(row):
            step_indices = [i for i, (x_step, y_step, _) in enumerate(path) if (x_step == x and y_step == y)]

            if len(step_indices) == 1:
                x_prev, y_prev, _ = path[(step_indices[0]-1) % len(path)]
                x_next, y_next, _ = path[(step_indices[0]+1) % len(path)]

                if x == x_prev-1 and y == y_prev:
                    intersection_counter += 1
                elif x_next == x+1 and y_next == y:
                    intersection_counter -= 1
            elif intersection_counter != 0:
                enclosed_tiles.append((x, y, cell))

    return enclosed_tiles

def parse(puzzle_input):
    """Parse input."""
    map = [row for row in puzzle_input.splitlines()]

    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if cell == "S":
                return (x, y, "S"), map

    raise ValueError("No start position found")

def part1(data):
    """Solve part 1."""
    start_tile, map = data
    path = get_path(start_tile, [], map)

    return len(path) // 2

def part2(data):
    """Solve part 2."""
    start_tile, map = data
    path = get_path(start_tile, [], map)
    tiles = get_enclosed_tiles(path, map)

    return len(tiles)

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