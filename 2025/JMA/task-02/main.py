def count_zero_hits(start, direction, steps):
    """
    Count how many times the dial passes 0 during a single rotation.
    direction: +1 for R, -1 for L
    steps: number of clicks
    """
    steps = abs(steps)

    # Full cycles (every 100 steps) always hit 0 exactly once
    full_cycles = steps // 100
    extra = steps % 100

    hits = full_cycles

    # Check partial steps
    if direction == 1:
        # R: positions s+1, s+2, ..., s+extra
        # Solve (s + k) % 100 == 0 → k ≡ -s mod 100
        k = (-start) % 100
        if 1 <= k <= extra:
            hits += 1
    else:
        # L: positions s-1, s-2, ..., s-extra
        # Solve (s - k) % 100 == 0 → k ≡ s mod 100
        k = start % 100
        if 1 <= k <= extra:
            hits += 1

    return hits


def solve(filename):
    pos = 50
    password = 0

    with open(filename) as f:
        for line in f:
            line = line.strip()
            direction = 1 if line[0] == 'R' else -1
            n = int(line[1:])

            # Count hits from this rotation
            password += count_zero_hits(pos, direction, n)

            # Move dial to final position
            pos = (pos + direction * n) % 100

    return password


if __name__ == '__main__':
    print(solve("input.txt"))