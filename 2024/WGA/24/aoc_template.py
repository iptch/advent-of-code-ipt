# aoc_template.py

import pathlib
import sys
import re
from collections import defaultdict

def parse(puzzle_input):
    """Parse input."""
    values = defaultdict(bool)
    initial_values, gates = puzzle_input.split("\n\n")

    for initial_value in initial_values.splitlines():
        values[initial_value[:3]] = True if initial_value[-1] == "1" else False

    gates = [tuple(re.findall("AND|OR|XOR", gate) + re.findall("[a-z|0-9]{3}", gate)) for gate in gates.splitlines()]

    return values, gates

def part1(data):
    """Solve part 1."""
    values, gates = data
    counter = len(gates)

    while counter > 0:
        for gate, input1, input2, output in gates:
            if output not in values and input1 in values and input2 in values:
                if gate == "AND":
                    values[output] = values[input1] and values[input2]
                elif gate == "OR":
                    values[output] = values[input1] or values[input2]
                else:
                    values[output] = values[input1] != values[input2]

                counter -= 1

    output = "".join(["1" if values[x] else "0" for x in sorted(values, reverse=True) if x[0] == "z"])

    return int(output, 2)

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