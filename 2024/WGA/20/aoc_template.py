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

    t = dijkstra(start, end, map)
    cheats = []

    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if x > 0 and x < len(map)-1 and y > 0 and y < len(row)-1 and cell == "#":
                if [row[y] for row in map[x-1:x+2]] != "###" or map[x][y-1:y+2] != "###":
                    map[x][y] = "."
                    cheats.append(t - dijkstra(start, end, map))
                    map[x][y] = "#"

    return len([cheat for cheat in cheats if cheat >= (2 if len(map) == 15 else 100)])

def part2(data):
    """Solve part 2."""
    start, end, map = data

    t = dijkstra(start, end, map)
    cheats = []

    return len([cheat for cheat in cheats if cheat >= (50 if len(map) == 15 else 100)])

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