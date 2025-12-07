from timeit import default_timer as timer

from aocd import data

DAY = '07'
PART = 'b'


def solve(lines):
    grid = []
    for line in lines:
        grid.append([i for i in line])

    n_paths = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    for c in range(len(grid[0])):
        if grid[0][c] == 'S':
            n_paths[0][c] = 1

    for r in range(1, len(grid), 1):
        for c in range(len(grid[0])):
            if grid[r][c] == '^':
                n_paths[r][c-1] += n_paths[r-1][c]
                n_paths[r][c+1] += n_paths[r-1][c]
            else:
                n_paths[r][c] += n_paths[r-1][c]

    return sum(n_paths[-1])


def main():
    print(f'Advent of Code 2025 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()
    result = solve(lines)

    print(f'{str(result)}')


if __name__ == '__main__':
    start = timer()
    main()
    print(f"Completed in {timer() - start} sec")
