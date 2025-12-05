def solve(input_file):
    ranges = []

    # Read only the fresh ranges (before the blank line)
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            if not line:
                break
            a, b = map(int, line.split("-"))
            ranges.append([a, b])

    # Sort by starting point
    ranges.sort()

    # Merge overlapping or touching intervals
    merged = []
    cur_start, cur_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= cur_end + 1:       # overlap or adjacency
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end

    merged.append((cur_start, cur_end))

    # Count total fresh IDs (inclusive)
    total = sum(end - start + 1 for start, end in merged)
    return total


if __name__ == "__main__":
    print(solve("input.txt"))