from timeit import default_timer as timer

from aocd import data

DAY = '07'
PART = 'a'


def solve(lines):
    result = 0

    grid = []
    for line in lines:
        grid.append([i for i in line])

    for r in range(1, len(grid), 1):
        for c in range(len(grid[0])):
            if grid[r-1][c] in 'S|':
                if grid[r][c] == '.':
                    grid[r][c] = '|'
                elif grid[r][c] == '^':
                    grid[r][c-1] = '|'
                    grid[r][c+1] = '|'
                    result += 1

    return result


def main():
    print(f'Advent of Code 2025 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()
    result = solve(lines)

    print(f'{str(result)}')


if __name__ == '__main__':
    start = timer()
    main()
    print(f"Completed in {timer() - start} sec")
