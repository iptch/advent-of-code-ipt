from math import sqrt, pow


def solve(filename):
    points = []
    with open(filename) as f:
        points = [[int(p) for p in point.replace("\n", "").split(",")] for point in f.readlines()]

    # Get all distances
    distances = []
    for idy, p in enumerate(points):
        for idx, q in enumerate(points):
            if idx == points.index(p): continue
            distances.append([idy, idx, sqrt(
                pow(p[0] - q[0], 2) +
                pow(p[1] - q[1], 2) +
                pow(p[2] - q[2], 2)
            )])
    distances.sort(key=lambda x: x[2])

    ## Sort by nearest neighbour
    ## We make 10 passes
    connections = [distances[n] for n in range(0, 2000, 2)]
    print(connections)

    paths = []
    for a, b, _ in connections:

        placed = False

        # Try to merge into existing path
        for path in paths:
            if a in path or b in path:
                path.extend([a, b])
                placed = True
                break

        if placed:
            # after extending, also check if this merges two existing paths
            for p1 in paths:
                for p2 in paths:
                    if p1 is p2:
                        continue
                    if any(x in p1 for x in p2):
                        p1.extend(p2)
                        paths.remove(p2)
                        break
            continue

        # Otherwise make new path
        paths.append([a, b])

    # Deduplicate nodes inside each path
    paths = [list(set(path)) for path in paths]
    paths.sort(key=lambda x: len(x), reverse=True)
    print(paths)
    res = 1
    for p in paths[:3]:
        res *= len(p)

    return res


if __name__ == "__main__":
    print(solve("input.txt"))
