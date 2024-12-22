# aoc_template.py

import pathlib
import sys
import heapq

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dijkstra(start, end, map):
    pq = [(0, start[0], start[1])]
    visited = set()

    while pq:
        cost, x, y = heapq.heappop(pq)
        if (x, y) == end:
            return cost

        if (x, y) in visited:
            continue
        
        visited.add((x, y))

        for dir in DIRECTIONS:
            dx, dy = dir
            nx, ny = x + dx, y + dy

            if ny >= 0 and ny < len(map) and nx >= 0 and nx < len(map[ny]) and map[ny][nx] != '#':
                heapq.heappush(pq, (cost+1, nx, ny))

    return

def parse(puzzle_input):
    """Parse input."""
    bytes = [tuple(int(i) for i in row.split(",")) for row in puzzle_input.splitlines()]
    x_limit = max([x for x, _ in bytes]) + 1
    y_limit = max([y for _, y in bytes]) + 1

    return (bytes, x_limit, y_limit)

def part1(data):
    """Solve part 1."""
    bytes, x_limit, y_limit = data
    map = [["."] * (x_limit) for _ in range(y_limit)]

    for i, byte in enumerate(bytes):
        if i < (12 if x_limit == 7 else 1024):
            x, y = byte
            map[y][x] = "#"

    for row in map:
        print("".join(row))

    return dijkstra((0, 0), (y_limit-1, x_limit-1), map)

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