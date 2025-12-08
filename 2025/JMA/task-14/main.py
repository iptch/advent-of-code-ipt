def solve(filename):
    with open(filename) as f:
        manifold = [list(line.rstrip('\n')) for line in f]

    H = len(manifold)
    W = len(manifold[0])

    # Find start
    start_col = manifold[0].index("S")

    # DP map: (row, col) -> count of timelines
    from collections import defaultdict
    curr = {(0, start_col): 1}

    for r in range(1, H):
        nxt = defaultdict(int)
        for (rr, cc), count in curr.items():
            # Beam always moves downward
            nr = rr + 1
            if nr >= H:
                continue

            cell = manifold[nr][cc]

            if cell == "." or cell == "S":
                nxt[(nr, cc)] += count

            elif cell == "^":
                # Split into left and right
                if cc - 1 >= 0:
                    nxt[(nr, cc - 1)] += count
                if cc + 1 < W:
                    nxt[(nr, cc + 1)] += count

        curr = nxt

    # Sum all surviving timelines
    return sum(curr.values())


if __name__ == "__main__":
    print(solve("input.txt"))
