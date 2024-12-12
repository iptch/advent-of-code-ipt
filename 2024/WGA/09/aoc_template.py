# aoc_template.py

import pathlib
import sys

FREE_SPACE_ID = -1

def get_checksum(blocks):
    sum = 0

    for i in range(len(blocks)):
        if blocks[i] > FREE_SPACE_ID:
            sum += i * blocks[i]

    return sum

def compact_blocks(blocks):
    compacted_blocks = blocks.copy()

    for i in range(len(compacted_blocks)):
        if compacted_blocks[i] == FREE_SPACE_ID:
            for j in range(len(compacted_blocks)-1, 0, -1):
                if compacted_blocks[j] > FREE_SPACE_ID:
                    if j == i-1:
                        return compacted_blocks
                    else:
                        compacted_blocks[i] = compacted_blocks[j]
                        compacted_blocks[j] = FREE_SPACE_ID
                        break

    return None

def compact_files(files):
    compacted_files = files.copy()

    for i in range(len(compacted_files)-1, 0, -1):
        if compacted_files[i][0] > FREE_SPACE_ID:
            for j in range(0, i):
                if compacted_files[j][0] == FREE_SPACE_ID and compacted_files[j][1] >= compacted_files[i][1]:
                    free_space = compacted_files[j][1] - compacted_files[i][1]
                    compacted_files[j] = (compacted_files[i][0], compacted_files[i][1])
                    compacted_files[i] = (FREE_SPACE_ID, compacted_files[i][1])
                    compacted_files.insert(j+1, (FREE_SPACE_ID, free_space))
                    break

    return compacted_files

def get_blocks(files):
    blocks = []

    for file in files:
        blocks += [file[0] for _ in range(file[1])]

    return blocks

def get_files(puzzle_input):
    files = []
    id = 0

    for i in range(0, len(puzzle_input), 2):
        files.append((id, int(puzzle_input[i])))

        if i+1 < len(puzzle_input):
            files.append((FREE_SPACE_ID, int(puzzle_input[i+1])))

        id += 1

    return files

def parse(puzzle_input):
    """Parse input."""
    return get_files(puzzle_input)

def part1(data):
    """Solve part 1."""
    return get_checksum(compact_blocks(get_blocks(data)))

def part2(data):
    """Solve part 2."""
    compacted_files = compact_files(data)

    blocks = []

    for file in compacted_files:
        blocks.extend([file[0] for _ in range(file[1])])

    return get_checksum(blocks)

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