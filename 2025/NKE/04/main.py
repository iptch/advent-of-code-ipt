def parse_input():
    grid = []
    with open("input.txt") as f:
        for line in f:
            line = line.rstrip("\n")
            grid.append(list(line))                           
    return grid

DIRECTIONS = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1)
]

def count_accessible(grid):

    rows = len(grid)
    cols = len(grid[0])

    total = 0

    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            neighbor = 0

            for dr, dc in DIRECTIONS:
                ar, ac = r + dr, c + dc
                if ar >= 0 and ar < rows and ac >= 0 and ac < cols:
                    if grid[ar][ac] == '@':
                        neighbor += 1

            if neighbor < 4:
                accessible += 1

    return accessible


def count_total_removed(grid):

    #grid = [row[:] for row in grid]

    rows = len(grid)
    cols = len(grid[0])
    total_removed = 0

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '@':
                    continue

                neighbor = 0
                for dr, dc, in DIRECTIONS:
                    ar, ac = r + dr, c + dc
                    if 0 <= ar < rows and 0 <= ac < cols:
                        if grid[ar][ac] == '@':
                            neighbor += 1

                if neighbor < 4:
                    to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = '.'

        total_removed += len(to_remove)

    return total_removed


def main():
    grid = parse_input()
    num_accessible = count_accessible(grid)
    num_total_removed = count_total_removed(grid)
    print("count_accessible", num_accessible)
    print("count_total_removed", num_total_removed)


if __name__ == "__main__":
    main()