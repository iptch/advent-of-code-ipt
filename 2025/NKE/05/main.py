def parse_input():
    with open("input.txt") as f:
        raw = f.read().strip()

    parts = raw.split("\n\n")
    ranges_part = parts[0]
    ids_part = parts[1]

    ranges = []

    for line in ranges_part.splitlines():
        a, b = line.split("-")
        start = int(a)
        end = int(b)
        ranges.append((start, end))

    ingredients_ids = []
    for line in ids_part.splitlines():
        ingredients_ids.append(int(line))

    return ranges, ingredients_ids


def is_fresh(ranges, x):
    for start, end in ranges:
        if start <= x <= end:
            return True
    return False


def calc_fresh(ranges, ingredients_ids):
    fresh_count = 0
    for x in ingredients_ids:
        if is_fresh(ranges, x):
            fresh_count += 1
    return fresh_count


def calc_total_fresh_ids(ranges):

    sorted_ranges = sorted(ranges, key=lambda range: range[0])
    merged = []
    current_start, current_end = sorted_ranges[0]

    i = 1
    while i < len(sorted_ranges):
        start, end = sorted_ranges[i]

        if start <= current_end:
            if end > current_end:
                current_end = end
        else:
            merged.append((current_start, current_end))
            current_start = start
            current_end = end

        i += 1

    merged.append((current_start, current_end))

    total = 0

    for start, end in merged:
        total += (end - start + 1)

    return total


def main():
    ranges, ingredients_ids = parse_input()
    fresh_count = calc_fresh(ranges, ingredients_ids)
    print("fresh_count: ", fresh_count)
    ranges, _ = parse_input()
    total_fresh = calc_total_fresh_ids(ranges)
    print("total fresh ids:", total_fresh)


if __name__ == "__main__":
    main()