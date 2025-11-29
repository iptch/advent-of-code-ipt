# aoc_template.py

import pathlib
import sys
import re
import math

def get_step_count(instructions, nodes, start_element, stop_regex):
    element = start_element
    step_count = 0

    while re.match(stop_regex, element) is None:
        instruction = instructions[step_count % len(instructions)]
        element = next((e, l ,r) for e, l, r in nodes if e == element)[1 if instruction == "L" else 2]
        step_count += 1
        
    return step_count

def lcm(steps):
    result = steps[0]

    for step in steps[1:]:
        result = math.lcm(result, step)

    return result

def parse(puzzle_input):
    """Parse input."""
    instructions, nodes = puzzle_input.split("\n\n")
    nodes = [re.findall("[A-Z|1-9]{3}", node) for node in nodes.splitlines()]

    return instructions, nodes

def part1(data):
    """Solve part 1."""
    instructions, nodes = data

    return get_step_count(instructions, nodes, "AAA", "ZZZ")

def part2(data):
    """Solve part 2."""
    instructions, nodes = data
    start_elements = [e for e, _, _ in nodes if e.endswith("A")]
    steps = [get_step_count(instructions, nodes, start_element, "[A-Z|1-9]{2}Z") for start_element in start_elements]
        
    return lcm(steps)

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