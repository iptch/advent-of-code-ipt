import heapq

rows = []

N = 1000

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2) + ((p1[2] - p2[2]) ** 2)

class Node(object):
    def __init__(self, dist: int, i1, i2):
        self.dist = dist
        self.i1 = i1
        self.i2 = i2

    def __repr__(self):
        return f'Node value: {self.dist}'

    def __lt__(self, other):
        return self.dist < other.dist
    
# DSU class (source: https://www.geeksforgeeks.org/dsa/connected-components-in-an-undirected-graph/)
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # Each node is its own parent initially

    # Find with path compression
    def find_parent(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.find_parent(self.parent[u])
        return self.parent[u]

    # Union the sets of u and v
    def unite(self, u, v):
        pu = self.find_parent(u)
        pv = self.find_parent(v)
        if pu == pv:
            return
        self.parent[pu] = pv

def getComponents(adj):
    V = len(adj)
    dsu = DSU(V)

    # unite components on the basis of edges
    for i in range(V):
        for nxt in adj[i]:
            dsu.unite(i, nxt)

    res_map = {}
    for i in range(V):
        par = dsu.find_parent(i)
        res_map.setdefault(par, []).append(i)

    res = list(res_map.values())
    return res

with open("input.txt", "r") as file:
    for line in file:
        rows.append(list(map(lambda x: int(x), line.strip().split(','))))

heap = []

for i in range(len(rows)):
    for j in range(i+1, len(rows)):
        p1 = rows[i]
        p2 = rows[j]
        heap.append(Node(distance(p1,p2), i, j))

heapq.heapify(heap)

dsu = DSU(len(rows))

unions = len(rows) - 1

while True:
    node = heapq.heappop(heap)
    i1 = node.i1
    i2 = node.i2

    parent1 = dsu.find_parent(i1)
    parent2 = dsu.find_parent(i2)

    if parent1 != parent2 or True:
        if dsu.find_parent(i1) != dsu.find_parent(i2): # again for compression
            unions -= 1
        dsu.unite(i1, i2)

    if unions == 0:
        print(rows[i1][0] * rows[i2][0])
        break
