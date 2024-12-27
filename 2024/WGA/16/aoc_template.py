# aoc_template.py

import pathlib
import sys
import heapq

DIRECTIONS = ["^", ">", "v", "<"]
MOVES = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

def dijkstra(start, end, map):
    pq = [(0, start[0], start[1], ">")]
    visited = set()

    while pq:
        cost, x, y, dir = heapq.heappop(pq)

        if (x, y) == end:
            return cost
        
        if (x, y, dir) in visited:
            continue
        
        visited.add((x, y, dir))

        dx, dy = MOVES[dir]
        nx, ny = x + dx, y + dy

        if map[nx][ny] != "#":
            new_cost = cost + 1
            heapq.heappush(pq, (new_cost, nx, ny, dir))

        for rotation in [-1, 1]:
            new_dir = DIRECTIONS[(DIRECTIONS.index(dir) + rotation) % 4]
            new_cost = cost + 1000
            heapq.heappush(pq, (new_cost, x, y, new_dir))
    
    return

def parse(puzzle_input):
    """Parse input."""
    start = end = None
    map = [list(row) for row in puzzle_input.splitlines()]

    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if cell == "S":
                start = (x, y)
            elif cell == "E":
                end = (x, y)
            elif start is not None and end is not None:
                break

    return start, end, [list(row) for row in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""
    start, end, map = data

    return dijkstra(start, end, map)

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