# aoc_template.py

import pathlib
import sys
import re
from collections import defaultdict

def bron_kerbosch(r, p, x, cliques, graph):
    if not p and not x:
        cliques.append(r)

        return 
    
    for v in list(p):
        bron_kerbosch(r | {v}, p & graph[v], x & graph[v], cliques, graph)
        p.remove(v)
        x.add(v)

def get_triangles(graph):
    triangles = []

    for computer1 in graph:
        for computer2 in graph[computer1]:
            if computer2 > computer1:
                for computer3 in graph[computer2]:
                    if computer3 > computer2 and computer3 in graph[computer1]:
                        triangles.append({computer1, computer2, computer3})

    return triangles

def parse(puzzle_input):
    """Parse input."""
    connections = [row.split("-") for row in puzzle_input.splitlines()]

    graph = defaultdict(set)

    for computer1, computer2 in connections:
        graph[computer1].add(computer2)
        graph[computer2].add(computer1)
    
    return graph

def part1(data):
    """Solve part 1."""
    triangles = [",".join(triangle) for triangle in get_triangles(data)]

    return len([triangle for triangle in triangles if re.search("t[a-z]", triangle) != None])

def part2(data):
    """Solve part 2."""
    cliques = []
    bron_kerbosch(set(), set(data.keys()), set(), cliques, data)
    largest_clique = max(cliques, key=len)

    return ','.join(sorted(largest_clique))

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