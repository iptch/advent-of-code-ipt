# aoc_template.py

import pathlib
import sys
import re

LIMIT = 100
OFFSET = 10000000000000

def get_tokens(a, b):
    return 3 * a + b

def parse(puzzle_input):
    """Parse input."""
    machines = []

    for machine in puzzle_input.split("\n\n"):
        lines = machine.splitlines()
        button_a = list(map(int, re.findall(r"\d+", lines[0])))
        button_b = list(map(int, re.findall(r"\d+", lines[1])))
        prize = list(map(int, re.findall(r"\d+", lines[2])))

        machines.append((
            (button_a[0], button_a[1]),
            (button_b[0], button_b[1]),
            (prize[0], prize[1])
        ))

    return machines

def part1(data):
    """Solve part 1."""
    sum = 0
    
    for machine in data:
        button_a, button_b, prize = machine
        button_a_x, button_a_y = button_a
        button_b_x, button_b_y = button_b
        prize_x, prize_y = prize

        a = (button_b_y * prize_x - prize_y * button_b_x) / (button_b_y * button_a_x - button_a_y * button_b_x)
        b = (prize_y - a * button_a_y) / button_b_y

        if int(a) == a and a <= LIMIT and int(b) == b and b <= LIMIT:
            sum += int(get_tokens(a, b))

    return sum

def part2(data):
    """Solve part 2."""
    sum = 0
    
    for machine in data:
        button_a, button_b, prize = machine
        button_a_x, button_a_y = button_a
        button_b_x, button_b_y = button_b
        prize_x, prize_y = (prize[0] + OFFSET, prize[1] + OFFSET)

        a = (button_b_y * prize_x - prize_y * button_b_x) / (button_b_y * button_a_x - button_a_y * button_b_x)
        b = (prize_y - a * button_a_y) / button_b_y

        if int(a) == a and int(b) == b:
            sum += int(get_tokens(a, b))

    return sum

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