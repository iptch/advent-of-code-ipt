from timeit import default_timer as timer

from aocd import data

DAY = '05'
PART = 'a'


def solve(lines):
    fresh_ingredient_ranges_lines = [line for line in lines if '-' in line]
    fresh_ingredient_ranges = [tuple([int(n) for n in line.split('-')]) for line in fresh_ingredient_ranges_lines]

    id_lines = lines[len(fresh_ingredient_ranges)+1:]
    ids = [int(line) for line in id_lines]

    valid_ids = set([id for id in ids if any(id >= start and id <= end for start, end in fresh_ingredient_ranges)])
            
    return len(valid_ids)


def main():
    print(f'Advent of Code 2025 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()
    result = solve(lines)

    print(f'{str(result)}')


if __name__ == '__main__':
    start = timer()
    main()
    print(f"Completed in {timer() - start} sec")
