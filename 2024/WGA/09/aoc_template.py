# aoc_template.py

import pathlib
import sys

FREE_SPACE_ID = -1

def get_checksum(blocks):
    return sum([i * block for i, block in enumerate(blocks) if block > FREE_SPACE_ID])

def compact_blocks(blocks):
    for i, free_block in enumerate(blocks):
        if free_block == FREE_SPACE_ID:
            for j, file_block in reversed(list(enumerate(blocks))):
                if file_block > FREE_SPACE_ID:
                    if j == i-1:
                        return blocks
                    
                    blocks[i], blocks[j] = file_block, free_block
                    break

    return None

def compact_files(files):
    for i in range(len(files)-1, 0, -1):
        file_id, file_space = files[i]
        
        if file_id > FREE_SPACE_ID:
            for j, (free_id, free_space) in enumerate(files[:i]):
                if free_id == FREE_SPACE_ID and free_space >= file_space:
                    files[i], files[j] = (free_id, file_space), (file_id, file_space)
                    files.insert(j+1, (free_id, free_space - file_space))
                    break

    return files

def get_blocks(files):
    blocks = []

    for id, free_space in files:
        blocks += [id for _ in range(free_space)]

    return blocks

def get_files(puzzle_input):
    files = []

    for i in range(0, len(puzzle_input), 2):
        files.append((i // 2, int(puzzle_input[i])))

        if i+1 < len(puzzle_input):
            files.append((FREE_SPACE_ID, int(puzzle_input[i+1])))

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