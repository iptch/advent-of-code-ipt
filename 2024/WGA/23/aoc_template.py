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

    for node1 in graph:
        for node2 in graph[node1]:
            if node2 > node1:
                for node3 in graph[node2]:
                    if node3 > node2 and node3 in graph[node1]:
                        triangles.append({node1, node2, node3})

    return triangles

def parse(puzzle_input):
    """Parse input."""
    connections = [row.split("-") for row in puzzle_input.splitlines()]

    graph = defaultdict(set)

    for node1, node2 in connections:
        graph[node1].add(node2)
        graph[node2].add(node1)
    
    return graph

def part1(data):
    """Solve part 1."""
    triangles = [",".join(triangle) for triangle in get_triangles(data)]

    return len([1 for triangle in triangles if re.search("t[a-z]", triangle) != None])

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