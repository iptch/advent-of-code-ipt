# aoc_template.py

import pathlib
import sys

def map_ranges(in_ranges, mapping):
    out_ranges = []
    min_src_range_start = mapping[0][0]
    max_src_range_end = mapping[-1][1]

    for in_range_start, in_range_end in in_ranges:
        if in_range_start < min_src_range_start:
            out_ranges.append((in_range_start, min(in_range_end, min_src_range_start)))
        
        if in_range_end > max_src_range_end:
            out_ranges.append((max(in_range_start, max_src_range_end), in_range_end))

        for src_range_start, src_range_end, offset in mapping:
            if in_range_start < src_range_end and in_range_end > src_range_start:
                out_ranges.append((max(in_range_start, src_range_start)+offset, min(in_range_end, src_range_end)+offset))

    return out_ranges

def get_location_ranges(seed_range, mappings):
    ranges = [seed_range]
    
    for mapping in mappings:
        ranges = map_ranges(ranges, mapping)

    return ranges

def parse(puzzle_input):
    """Parse input."""
    almanac = puzzle_input.split("\n\n")
    seeds = [int(seed) for seed in almanac[0].split()[1:]]
    mappings = []

    for section in almanac[1:]:
        mapping = []

        for mapping_range in section.splitlines()[1:]:
            dest_range_start, src_range_start, range_length = [int(number) for number in mapping_range.split()]
            mapping.append((src_range_start, src_range_start+range_length, dest_range_start-src_range_start))

        mappings.append(sorted(mapping, key=lambda x: x[1]))

    return seeds, mappings

def part1(data):
    """Solve part 1."""
    seeds, mappings = data
    locations = []

    for seed in seeds:
        locations += [location_start for location_start, _ in get_location_ranges((seed, seed), mappings)]

    return min(locations)

def part2(data):
    """Solve part 2."""
    seeds, mappings = data
    seed_ranges = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]
    locations = []

    for seed_range in seed_ranges:
        locations += [location_start for location_start, _ in get_location_ranges(seed_range, mappings)]

    return min(locations)

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