# aoc_template.py

import pathlib
import sys
import heapq
from collections import defaultdict

DIRECTIONS = ["^", ">", "v", "<"]
MOVES = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

def dijkstra(start, end, map):
    pq = [(0, start[0], start[1], ">")]
    visited = set()
    costs = defaultdict(lambda: float('inf'))
    costs[start] = 0
    prev_tiles = defaultdict(list)

    while pq:
        cost, x, y, dir = heapq.heappop(pq)
        
        if (x, y, dir) in visited:
            continue
        
        visited.add((x, y, dir))

        dx, dy = MOVES[dir]
        nx, ny = x + dx, y + dy

        if map[nx][ny] != "#":
            new_cost = cost + 1

            if new_cost <= costs[(nx, ny, dir)]:
                if new_cost < costs[(nx, ny, dir)]:
                    prev_tiles[(nx, ny, dir)] = []
                    costs[(nx, ny, dir)] = new_cost
                
                prev_tiles[(nx, ny, dir)].append((x, y, dir))
                heapq.heappush(pq, (new_cost, nx, ny, dir))

        for rotation in [-1, 1]:
            new_dir = DIRECTIONS[(DIRECTIONS.index(dir) + rotation) % 4]
            new_cost = cost + 1000

            if new_cost <= costs[(x, y, new_dir)]:
                if new_cost < costs[(x, y, new_dir)]:
                    prev_tiles[(x, y, new_dir)] = []
                    costs[(x, y, new_dir)] = new_cost
                
                prev_tiles[(x, y, new_dir)].append((x, y, dir))
                heapq.heappush(pq, (new_cost, x, y, new_dir))

    def backtrack_paths(tile):
        if tile == start:
            return [[start]]

        paths = []

        for prev_tile in prev_tiles[tile]:
            for path in backtrack_paths(prev_tile):
                paths.append(path + [tile])

        return paths
    
    end_costs = [costs[(end[0], end[1], dir)] for dir in DIRECTIONS]
    min_dir = DIRECTIONS[end_costs.index(min(end_costs))]

    shortest_paths = backtrack_paths((end[0], end[1], min_dir))

    best_tiles = [[(x, y) for x, y, _ in path] for path in shortest_paths]
    best_tiles = list({inner for outer in best_tiles for inner in outer})

    return costs[(end[0], end[1], min_dir)], shortest_paths, best_tiles

def parse(puzzle_input):
    """Parse input."""
    start = end = None
    map = [list(row) for row in puzzle_input.splitlines()]

    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if cell == "S":
                start = (x, y, ">")
            elif cell == "E":
                end = (x, y)
            elif start is not None and end is not None:
                break

    return start, end, [list(row) for row in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""
    start, end, map = data

    return dijkstra(start, end, map)[0]

def part2(data):
    """Solve part 2."""
    start, end, map = data

    return len(dijkstra(start, end, map)[2])

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