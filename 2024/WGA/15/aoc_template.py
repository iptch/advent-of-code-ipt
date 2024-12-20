# aoc_template.py

import pathlib
import sys
import copy

sys.setrecursionlimit(25000)

def get_gps(map):
    sum = 0

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] in ["O", "["]:
                sum += 100 * x + y

    return sum

def move(x, y, map, movements):
    if len(movements) == 0:
        return (x, y)
    
    new_x = x
    new_y = y
    
    if movements[0] == "^":
        for i in range(x-1, 0, -1):
            if map[i][y] == "#":
                break
            elif map[i][y] == ".":
                if i < x-1:
                    for j in range(i+1, x):
                        map[j-1][y] = map[j][y]

                new_x = x - 1
                break
    elif movements[0] == "v":
        for i in range(x+1, len(map)):
            if map[i][y] == "#":
                break
            elif map[i][y] == ".":
                if i > x+1:
                    for j in range(x+1, i):
                        map[j+1][y] = map[j][y]

                new_x = x + 1
                break
    elif movements[0] == "<":
        for i in range(y-1, 0, -1):
            if map[x][i] == "#":
                break
            elif map[x][i] == ".":
                if i < y-1:
                    map[x][i:y-1] = map[x][i+1:y]

                new_y = y - 1
                break
    else:
        for i in range(y+1, len(map[x])):
            if map[x][i] == "#":
                break
            elif map[x][i] == ".":
                if i > y+1:
                    map[x][y+2:i+1] = map[x][y+1:i]

                new_y = y + 1
                break

    map[x][y] = "."
    map[new_x][new_y] = "@"

    return move(new_x, new_y, map, movements[1:])

def parse(puzzle_input):
    """Parse input."""
    map, movements = puzzle_input.split("\n\n")
    map = [list(row) for row in map.splitlines()]

    return [map, movements.replace("\n","")]

def part1(data):
    """Solve part 1."""
    map = copy.deepcopy(data[0])
    movements = data[1]
    x_start = y_start = None

    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == "@":
                x_start = x
                y_start = y
                break

    move(x_start, y_start, map, movements)

    for row in map:
        print("".join(row))

    return get_gps(map)

def part2(data):
    """Solve part 2."""
    map = copy.deepcopy(data[0])
    movements = data[1]
    x_start = y_start = None

    for x in range(len(map)):
        map[x] = list("".join(map[x]).replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@."))

    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == "@":
                x_start = x
                y_start = y
                break

    move(x_start, y_start, map, movements)

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