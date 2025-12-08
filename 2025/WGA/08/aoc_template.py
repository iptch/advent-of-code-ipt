# aoc_template.py

import pathlib
import sys
import math
import networkx as nx

def dist(position_1, position_2):
    x_1, y_1, z_1 = position_1
    x_2, y_2, z_2 = position_2

    return (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 + (z_1 - z_2) ** 2

def get_pairs(positions):
    pairs = [0] * (math.factorial(len(positions)) // (2 * math.factorial(len(positions) - 2)))

    k = 0

    for i, position_1 in enumerate(positions):        
        for j, position_2 in enumerate(positions[i+1:]):
            pairs[k] = ([i, j+i+1], dist(position_1, position_2))
            k += 1

    return [x[0] for x in sorted(pairs, key=lambda x: x[1])]

def multiply(numbers):
    prod = 1

    for number in numbers:
        prod *= number

    return prod

def parse(puzzle_input):
    """Parse input."""

    return [[int(x) for x in row.split(",")] for row in puzzle_input.split("\n")]

def part1(data):
    """Solve part 1."""
    limit = 10 if len(data) == 20 else 1000 # Use 10 for example input, 1000 for real input
    pairs = get_pairs(data)

    G = nx.Graph(pairs[:limit])
    circuits = list(nx.connected_components(G))

    return multiply(sorted([len(circuit) for circuit in circuits], reverse=True)[:3])

def part2(data):
    """Solve part 2."""
    pairs = get_pairs(data)

    G = nx.Graph()

    for pair in pairs:
        position_1, position_2 = pair
        
        G.add_edge(position_1, position_2)
        circuits = list(nx.connected_components(G))
        
        if len(circuits[0]) == len(data):
            return data[position_1][0] * data[position_2][0]
        
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