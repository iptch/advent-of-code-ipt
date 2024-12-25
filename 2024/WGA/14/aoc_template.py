# aoc_template.py

import pathlib
import sys
import re

sys.setrecursionlimit(20000)

def get_safety_factor(robots, x_limit, y_limit):
    safety_factor = len([x for x, y, _, _ in robots if x < x_limit/2-1 and y < y_limit/2-1])
    safety_factor *= len([x for x, y, _, _ in robots if x > x_limit/2 and y < y_limit/2-1])
    safety_factor *= len([x for x, y, _, _ in robots if x < x_limit/2-1 and y > y_limit/2])
    safety_factor *= len([x for x, y, _, _ in robots if x > x_limit/2 and y > y_limit/2])

    return safety_factor

def get_simulations(robots, x_limit, y_limit, t_limit):
    simulations = [None] * (t_limit+1)
    simulations[0] = (get_safety_factor(robots, x_limit, y_limit), robots)

    for i in range(1, len(simulations)):
        new_robots = []

        for robot in simulations[i-1][1]:
            x, y, dx, dy = robot
            nx = x + dx
            ny = y + dy
            
            new_robots.append((nx % x_limit, ny % y_limit, dx, dy))

        simulations[i] = (get_safety_factor(new_robots, x_limit, y_limit), new_robots)

    return simulations

def parse(puzzle_input):
    """Parse input."""
    return [tuple(map(int, re.findall(r"-?\d+", row))) for row in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""
    x_limit = max([x for x, _, _, _ in data]) + 1
    y_limit = max([y for _, y, _, _ in data]) + 1
    t_limit = 100

    return get_simulations(data, x_limit, y_limit, t_limit)[-1][0]

def part2(data):
    """Solve part 2."""
    x_limit = max([x for x, _, _, _ in data]) + 1
    y_limit = max([y for _, y, _, _ in data]) + 1
    t_limit = 10000

    simulations = get_simulations(data, x_limit, y_limit, t_limit)
    safety_factors = [simulation[0] for simulation in simulations]
    t_min = safety_factors.index(min(safety_factors))

    map = [["."] * x_limit for _ in range(y_limit)]
    
    for x, y, _, _ in simulations[t_min][1]:
        map[y][x] = "@"

    for row in map:
        print("".join(row))

    return t_min

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