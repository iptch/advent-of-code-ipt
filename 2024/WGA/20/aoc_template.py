# aoc_template.py

import pathlib
import sys
import heapq

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def manhattan_dist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    return abs(x2 - x1) + abs(y2 - y1)

def dijkstra(start, end, map):
    pq = [(0, start[0], start[1])]
    visited = []

    while pq:
        cost, x, y = heapq.heappop(pq)
        
        if (x, y) == end:
            visited.append((x, y))
            return cost, visited

        if (x, y) in visited:
            continue
        
        visited.append((x, y))

        for dir in DIRECTIONS:
            dx, dy = dir
            nx, ny = x + dx, y + dy

            if ny >= 0 and ny < len(map) and nx >= 0 and nx < len(map[nx]) and map[nx][ny] != '#':
                heapq.heappush(pq, (cost+1, nx, ny))

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

    return (start, end, [list(row) for row in puzzle_input.splitlines()])

def part1(data):
    """Solve part 1."""
    start, end, map = data
    t_limit = 2 if len(map) == 15 else 100
    visited = dijkstra(start, end, map)[1]
    cheats = 0

    for i, start in enumerate(visited):
        for j, end in enumerate(visited[i+t_limit:]):
            cheat_length = manhattan_dist(start, end)
            t_saved = j + t_limit - cheat_length

            if cheat_length <= 2 and t_saved >= t_limit:
                cheats += 1

    return cheats

def part2(data):
    """Solve part 2."""
    start, end, map = data
    t_limit = 50 if len(map) == 15 else 100
    visited = dijkstra(start, end, map)[1]
    cheats = 0

    for i, start in enumerate(visited):
        for j, end in enumerate(visited[i+t_limit:]):
            cheat_length = manhattan_dist(start, end)
            t_saved = j + t_limit - cheat_length

            if cheat_length <= 20 and t_saved >= t_limit:
                cheats += 1

    return cheats

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