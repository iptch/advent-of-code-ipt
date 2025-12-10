class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]


    def find_parent(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.find_parent(self.parent[u])
        return self.parent[u]


    def unite(self, u, v):
        pu = self.find_parent(u)
        pv = self.find_parent(v)
        if pu == pv:
            return
        self.parent[pu] = pv


def parse_input():
    points = []
    with open("input.txt") as f:
        for line in f:
            line = line.rstrip("\n")
            x, y, z = line.split(",")
            points.append((int(x), int(y), int(z)))

    return points


def sort_points(points):
    n = len(points)
    edges = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i+1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            dist2 = dx * dx + dy * dy + dz * dz
            edges.append((dist2, i, j))
    edges.sort(key=lambda e: e[0])
    return edges


from collections import Counter
def solve_part1(points, edges):
    K = 1000
    n = len(points)
    dsu = DSU(n)

    for idx, (_, i, j) in enumerate(edges):
        if idx == K:
            break
        dsu.unite(i, j)

    counts = Counter()
    for i in range(n):
        root = dsu.find_parent(i)
        counts[root] += 1

    sizes = sorted(counts.values(), reverse=True)
    a, b, c = sizes[0], sizes[1], sizes[2]
    return a * b * c


def solve_part2(points, edges):
    n = len(points)
    dsu = DSU(n)

    remaining_unions = n - 1

    for _, i, j in edges:
        if dsu.find_parent(i) != dsu.find_parent(j):
            dsu.unite(i, j)
            remaining_unions -= 1

            if remaining_unions == 0:
                x1 = points[i][0]
                x2 = points[j][0]
                return x1 * x2

    return None


def main():
    points = parse_input()
    edges = sort_points(points)

    part1 = solve_part1(points, edges)
    print("part_one", part1)

    part2 = solve_part2(points, edges)
    print("part_two", part2)


if __name__ == "__main__":
    main()              