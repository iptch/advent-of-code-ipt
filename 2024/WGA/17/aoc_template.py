# aoc_template.py

import pathlib
import sys
import re

def combo(operand, a, b, c):
    if operand < 4:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    
    raise ValueError("Invalid combo operand")

def run_program(program, register_a, register_b, register_c):
    pointer = 0
    output = []

    while pointer < len(program):
        instruction = program[pointer]
        operand = program[pointer+1]

        if instruction == 0: # adv
            register_a = register_a >> combo(operand, register_a, register_b, register_c)
        elif instruction == 1: # bxl
            register_b ^= operand
        elif instruction == 2: # bst
            register_b = combo(operand, register_a, register_b, register_c) % 8
        elif instruction == 3: # jnz
            if register_a > 0:
                pointer = operand
                continue
        elif instruction == 4: # bxc
            register_b ^= register_c
        elif instruction == 5: # out
            output.append(str(combo(operand, register_a, register_b, register_c) % 8))
        elif instruction == 6: # bdv
            register_b = register_a >> combo(operand, register_a, register_b, register_c)
        else: # cdv
            register_c = register_a >> combo(operand, register_a, register_b, register_c)
            
        pointer += 2

    return ",".join(output)

def parse(puzzle_input):
    """Parse input."""
    registers, program = puzzle_input.split("\n\n")
    register_a, register_b, register_c = list(map(int, re.findall(r"\d+", registers)))
    program = list(map(int, re.findall(r"[0-7]", program)))

    return register_a, register_b, register_c, program

def part1(data):
    """Solve part 1."""
    register_a, register_b, register_c, program = data

    return run_program(program, register_a, register_b, register_c)

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