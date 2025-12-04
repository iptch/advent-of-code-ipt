from timeit import default_timer as timer

from aocd import data

DAY = '04'
PART = 'a'


def solve(lines):
    result = 0

    grid = []
    for line in lines:
        grid.append([i for i in line])
    
    for ri, r in enumerate(grid):
        for ci, c in enumerate(r):
            if c == '@':
                adjacent_indexes = [
                    (ri-1,ci-1), 
                    (ri-1,ci), 
                    (ri-1,ci+1), 
                    (ri,ci-1),
                    (ri,ci+1),
                    (ri+1,ci-1),
                    (ri+1,ci),
                    (ri+1,ci+1)
                ]
                valid_adjacent_indexes = [(ri, ci) for ri, ci in adjacent_indexes if ri >= 0 and ci >= 0 and ri < len(grid) and ci < len(grid[0])]
                adjacent_items = [grid[ri][ci] for ri, ci in valid_adjacent_indexes]
                if len([item for item in adjacent_items if item == '@']) < 4:
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
