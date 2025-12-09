import sys


# Disjoint Set Union (DSU) class to manage connected components efficiently
class DSU:
    def __init__(self, n):
        # Initially, each node is its own parent
        self.parent = list(range(n))
        # We start with N disjoint sets (isolated junction boxes)
        self.num_sets = n

    def find(self, i):
        # Path compression: points directly to the root for O(1) avg time
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        # Find the roots of the sets that i and j belong to
        root_i = self.find(i)
        root_j = self.find(j)

        # If they are in different sets, merge them
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.num_sets -= 1
            return True  # A merge occurred
        return False  # Already in the same set


def solve():
    # 1. Parse Input
    # Assumes input is in a file named 'input.txt' or passed via stdin
    # You can replace this with sys.stdin.read() for pipe usage
    try:
        with open('input.txt', 'r') as f:
            raw_data = f.read().strip()
    except FileNotFoundError:
        print("Please provide an 'input.txt' file with the puzzle input.")
        return

    points = []
    for line in raw_data.split('\n'):
        if line.strip():
            # Parse "X,Y,Z" into a tuple of integers
            points.append(tuple(map(int, line.split(','))))

    n = len(points)
    edges = []

    # 2. Generate all possible edges
    # We use squared Euclidean distance to avoid costly sqrt() calls,
    # as it preserves the sort order perfectly.
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            # dist_sq = (x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2
            dist_sq = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2
            edges.append((dist_sq, i, j))

    # 3. Sort edges by distance (shortest first)
    edges.sort(key=lambda x: x[0])

    # 4. Process connections using DSU
    dsu = DSU(n)

    for _, u, v in edges:
        # Attempt to connect the two junction boxes
        if dsu.union(u, v):
            # If this connection reduced the number of sets to 1,
            # we have found the final link needed.
            if dsu.num_sets == 1:
                x1 = points[u][0]
                x2 = points[v][0]
                print(f"--- Connection Found ---")
                print(f"Connecting Point A: {points[u]}")
                print(f"Connecting Point B: {points[v]}")
                print(f"Part 2 Answer (Product of X coords): {x1 * x2}")
                return


if __name__ == "__main__":
    solve()
