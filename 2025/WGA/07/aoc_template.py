# aoc_template.py

import pathlib
import sys

def count_splits(x, y, map):
    nx = x + 1

    if nx == len(map):
        return 0
    
    if map[nx][y] == "^":
        sum = 1

        for dy in [-1, 1]:
            ny = y + dy

            if map[nx][ny] == ".":
                map[nx][ny] = "|"
                sum += count_splits(nx, ny, map)

        return sum

    if map[nx][y] == ".":
        map[nx][y] = "|"

        return count_splits(nx, y, map)
    
    return 0

def count_timelines(x, y, map):
    nx = x + 1

    if nx == len(map):
        return 1
    
    if map[nx][y] == "^":
        sum = 0

        for dy in [-1, 1]:
            ny = y + dy

            if map[nx][ny] == ".":
                timelines = count_timelines(nx, ny, map)
                map[nx][ny] = timelines
                sum += timelines
            else:
                sum = map[nx][ny]

        return sum

    if map[nx][y] == ".":
        timelines = count_timelines(nx, y, map)
        map[nx][y] = timelines

        return timelines
    
    return map[nx][y]

def parse(puzzle_input):
    """Parse input."""

    return [list(row) for row in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""

    return count_splits(0, data[0].index("S"), [row[:] for row in data])

def part2(data):
    """Solve part 2."""

    return count_timelines(0, data[0].index("S"), [row[:] for row in data])

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