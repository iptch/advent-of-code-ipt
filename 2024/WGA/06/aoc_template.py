# aoc_template.py

import pathlib
import sys
import sys
import re
import copy

sys.setrecursionlimit(10000)

REGEX = r"\^|>|v|<"

def patrol(position, map):
    direction = map[position[0]][position[1]]

    position_up = (position[0]-1, position[1])
    position_right = (position[0], position[1]+1)
    position_down = (position[0]+1, position[1])
    position_left = (position[0], position[1]-1)

    if direction == "^":
        if position_up[0] < 0:
            return False
        elif map[position_up[0]][position_up[1]] == "#":
            map[position[0]][position[1]] = ">"
            return patrol(position, map)
        else:
            if map[position_up[0]][position_up[1]] == "^":
                return True
            else:
                map[position_up[0]][position_up[1]] = "^"
                return patrol(position_up, map)
    elif direction == ">":
        if position_right[1] > len(map[0])-1:
            return False
        elif map[position_right[0]][position_right[1]] == "#":
            map[position[0]][position[1]] = "v"
            return patrol(position, map)
        else:
            if map[position_right[0]][position_right[1]] == ">":
                return True
            else:
                map[position_right[0]][position_right[1]] = ">"
                return patrol(position_right, map)
    elif direction == "v":
        if position_down[0] > len(map)-1:
            return False
        elif map[position_down[0]][position_down[1]] == "#":
            map[position[0]][position[1]] = "<"
            return patrol(position, map)
        else:
            if map[position_down[0]][position_down[1]] == "v":
                return True
            else:
                map[position_down[0]][position_down[1]] = "v"
                return patrol(position_down, map)
    else:
        if position_left[1] < 0:
            return False
        elif map[position_left[0]][position_left[1]] == "#":
            map[position[0]][position[1]] = "^"
            return patrol(position, map)
        else:
            if map[position_left[0]][position_left[1]] == "<":
                return True
            else:
                map[position_left[0]][position_left[1]] = "<"
                return patrol(position_left, map)

def get_start_position(map):
    for i in range(len(map)):
        res = re.search(REGEX, "".join(map[i]))

        if res:
            return (i, res.start())

    return None

def parse(puzzle_input):
    """Parse input."""
    return [list(row) for row in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""
    map = copy.deepcopy(data)
    patrol(get_start_position(map), map)

    sum = 0

    for row in map:
        sum += len(re.findall(REGEX, "".join(row)))

    return sum

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