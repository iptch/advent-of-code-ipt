# aoc_template.py

import pathlib
import sys

def get_areas_perimeters(prev_plant, i, j, map, local_path, global_path):
    plant = map[i][j]
    
    if (i, j) not in local_path:
        if plant == prev_plant:
            local_path.append((i, j))
            global_path.append((i, j))

            areas = 1
            perimeters = 0

            if i-1 >= 0:
                res = get_areas_perimeters(plant, i-1, j, map, local_path, global_path)
                areas += res[0]
                perimeters += res[1]
            else:
                perimeters += 1
            
            if i+1 < len(map):
                res = get_areas_perimeters(plant, i+1, j, map, local_path, global_path)
                areas += res[0]
                perimeters += res[1]
            else:
                perimeters += 1

            if j-1 >= 0:
                res = get_areas_perimeters(plant, i, j-1, map, local_path, global_path)
                areas += res[0]
                perimeters += res[1]
            else:
                perimeters += 1

            if j+1 < len(map[i]):
                res = get_areas_perimeters(plant, i, j+1, map, local_path, global_path)
                areas += res[0]
                perimeters += res[1]
            else:
                perimeters += 1
            
            return (areas, perimeters)

        return (0, 1)
    
    return (0, 0)

def parse(puzzle_input):
    """Parse input."""
    return [list(row) for row in puzzle_input.split()]

def part1(data):
    """Solve part 1."""
    sum = 0

    global_path = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i, j) not in global_path:
                local_path = []
                areas_perimeters = get_areas_perimeters(data[i][j], i, j, data, local_path, global_path)
                sum += areas_perimeters[0] * areas_perimeters[1]

    return sum

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