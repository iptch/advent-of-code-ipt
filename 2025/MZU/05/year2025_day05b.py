from timeit import default_timer as timer

from aocd import data

DAY = '05'
PART = 'b'

def overlap(s1, e1, s2, e2):
    return s1 <= s2 <= e1 or s1 <= e2 <= e1 or s2 <= s1 <= e2 or s2 <= e1 <= e2


def solve(lines):
    fresh_ingredient_ranges_lines = [line for line in lines if '-' in line]
    fresh_ingredient_ranges = [tuple([int(n) for n in line.split('-')]) for line in fresh_ingredient_ranges_lines]
    
    is_cleaned_up = False
    while not is_cleaned_up:
        is_cleaned_up = True
        for s1, e1 in fresh_ingredient_ranges[:]:
            for s2, e2 in fresh_ingredient_ranges[:]:
                if s1 == s2 and e1 == e2 or (s1,e1) not in fresh_ingredient_ranges or (s2,e2) not in fresh_ingredient_ranges:
                    continue
                elif overlap(s1, e1, s2, e2):
                    is_cleaned_up = False
                    fresh_ingredient_ranges.remove((s1,e1))
                    fresh_ingredient_ranges.remove((s2,e2))
                    fresh_ingredient_ranges.append((min(s1,s2),max(e1,e2)))
                
    return sum(e-s+1 for s,e in set(fresh_ingredient_ranges))


def main():
    print(f'Advent of Code 2025 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()
    result = solve(lines)

    print(f'The result is: {str(result)}')


if __name__ == '__main__':
    start = timer()
    main()
    print(f"Completed in {timer() - start} sec")
