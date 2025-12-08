def parse_input():
    grid = []
    with open("input.txt") as f:
        for line in f:
            line = line.rstrip("\n")
            if line:
                grid.append(line)
        return grid


def count_splits(grid):
    height, width = len(grid), len(grid[0])

    start_row = start_col = None

    for r, row in enumerate(grid):
        c = row.find('S')
        if c != -1:
            start_row, start_col = r, c
            break

    current = set()
    if start_row + 1 < height:
        current.add((start_row + 1, start_col))

    seen_beam = set()
    seen_split = set()

    while current:
        next_positions = set()

        for r, c in current:
            
            if not (0 <= r < height and 0 <= c < width):
                continue

            if (r, c) in seen_beam:
                continue

            seen_beam.add((r, c))
            cell = grid[r][c]
            
            if cell == '^':
                seen_split.add((r, c))

                if c - 1 >= 0:
                    next_positions.add((r, c - 1))
                if c + 1 < width:
                    next_positions.add((r, c + 1))

            else:
                nr = r + 1
                if nr < height:
                    next_positions.add((nr, c))

        current = next_positions

    return len(seen_split)


from collections import defaultdict

def count_timelines(grid):
    height, width = len(grid), len(grid[0])

    for r, row in enumerate(grid):
        c = row.find('S')
        if c != -1:
            start_row, start_col = r, c
            break
    
    current = {}
    if start_row + 1 < height:
        current[(start_row + 1, start_col)] = 1

    total_finished = 0

    while current:
        next_counts = defaultdict(int)

        for (r, c), count in current.items():
            if not (0 <= r < height and 0 <= c < width):
                total_finished += count
                continue
            
            cell = grid[r][c]

            if cell == '^':
                if c - 1 >= 0:
                    next_counts[(r, c - 1)] += count
                else:
                    total_finished += count

                if c + 1 < width:
                    next_counts[(r, c + 1)] += count
                else:
                    total_finished += count

            else:
                nr = r + 1
                if nr < height:
                    next_counts[(nr, c)] += count
                else:
                    total_finished += count

        current = dict(next_counts)
    
    return total_finished


def main():
    grid = parse_input()
    count_part_one = count_splits(grid)
    print("count_part_one", count_part_one)
    count_part_two = count_timelines(grid)
    print("count_part_two", count_part_two)


if __name__ == "__main__":
    main()