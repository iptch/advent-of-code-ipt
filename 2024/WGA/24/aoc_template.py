# aoc_template.py

import pathlib
import sys
import re

def simulate(gate, input1, input2):
    if gate == "AND":
        return input1 and input2
    elif gate == "OR":
        return input1 or input2
    elif gate == "XOR":
        return input1 != input2
    
    raise ValueError(f"Unknown gate: {gate}")

def parse(puzzle_input):
    """Parse input."""
    values = {}
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
                values[output] = simulate(gate, values[input1], values[input2])
                counter -= 1

    output = "".join(["1" if values[x] else "0" for x in sorted(values, reverse=True) if x[0] == "z"])

    return int(output, 2)

def part2(data):
    """Solve part 2."""
    gates = data[1]
    z_msb = max([output for _, _, _, output in gates if output[0] == "z"])
    wrong_outputs = set()

    # Ripple-carry adder constraints
    for gate, input1, input2, output in gates:
        # z outputs mut be connected to XOR gates (except for MSB)
        if gate != "XOR" and output[0] == "z" and output != z_msb:
            wrong_outputs.add(output)

        # XOR gates not connected to z outputs must have x and y inputs
        if gate == "XOR" and output[0] != "z" and input1[0] not in ["x", "y"]:
            wrong_outputs.add(output)

        # XOR gates not connected to z outputs must be connected to other XOR gates
        if gate == "XOR" and output[0] != "z" and len([1 for g, i1, i2, _ in gates if g == "XOR" and output in [i1, i2]]) != 1:
            wrong_outputs.add(output)

        # AND gate outputs must be connected to OR gates (except for LSB)
        if gate == "AND" and input1 not in ["x00", "y00"] and len([1 for g, i1, i2, _ in gates if g == "OR" and output in [i1, i2]]) != 1:
            wrong_outputs.add(output)

    return ",".join(sorted(wrong_outputs))

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