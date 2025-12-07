def solve(filename):
    res = 0
    manifold = []
    with open(filename) as f:
        manifold = [list(line.replace("\n", "")) for line in f.readlines()]

    # Beam Start
    start_pos = manifold[0].index("S")
    beam_pos = {start_pos}
    splits = 0

    # Beam propagation
    for row_idx,row in enumerate(manifold[2:-1:2]):
        for col_idx, col in enumerate(row):
            if col == "^" and col_idx in beam_pos:
                splits += 1
                beam_pos.remove(col_idx)
                beam_pos.add(col_idx - 1)
                beam_pos.add(col_idx + 1)
    print(beam_pos)

    return splits

if __name__ == "__main__":
    print(solve("sample.txt"))
