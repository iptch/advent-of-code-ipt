# aoc_template.py

import pathlib
import sys
import re

def get_a(program, cursor, a):
    for i in range(8):
        new_a = (a << 3) + i

        if run_program(program, new_a, 0, 0) == program[cursor:]:
            if cursor == 0:
                return new_a
            
            result = get_a(program, cursor-1, new_a)

            if result is not None:
                return result
            
    return None

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

def run_program(program, a, b, c):
    pointer = 0
    output = []

    while pointer < len(program):
        instruction = program[pointer]
        operand = program[pointer+1]

        if instruction == 0:
            a >>= combo(operand, a, b, c)
        elif instruction == 1:
            b ^= operand
        elif instruction == 2:
            b = combo(operand, a, b, c) % 8
        elif instruction == 3:
            if a > 0:
                pointer = operand
                continue
        elif instruction == 4:
            b ^= c
        elif instruction == 5:
            output.append(combo(operand, a, b, c) % 8)
        elif instruction == 6:
            b = a >> combo(operand, a, b, c)
        else:
            c = a >> combo(operand, a, b, c)
            
        pointer += 2

    return output

def parse(puzzle_input):
    """Parse input."""
    registers, program = puzzle_input.split("\n\n")
    a, b, c = list(map(int, re.findall(r"\d+", registers)))
    program = list(map(int, re.findall(r"[0-7]", program)))

    return a, b, c, program

def part1(data):
    """Solve part 1."""
    a, b, c, program = data

    return ",".join([str(value) for value in run_program(program, a, b, c)])

def part2(data):
    """Solve part 2."""
    program = data[3]

    return get_a(program, len(program)-1, 0)

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