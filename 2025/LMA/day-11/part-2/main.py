from collections import defaultdict

rows = dict()
incoming = dict()

with open("input.txt", "r") as file:
    for line in file:
        start = line.strip().split(':')[0]
        ends = line.strip().split(':')[1].split()

        if start not in rows:
            rows[start] = ends
        else:
            for x in ends:
                rows[start].append(x)
                
        for x in ends:
            if x not in rows:
                rows[x] = []
            if x not in incoming:
                incoming[x] = []
            incoming[x].append(start)

# source https://llego.dev/posts/implementing-topological-sort-python/
def topological_sort_kahn(graph):
    indegree = defaultdict(int) # Track indegrees
    queue = [] #Initialize queue

    # Calculate indegrees
    for node in graph:
        if node in graph:
            for neighbour in graph[node]:
                indegree[neighbour] += 1

    # Add nodes with 0 indegree to queue
    for node in graph:
        if indegree[node] == 0:
            queue.append(node)

    topological_order = []

    # Process until queue is empty
    while queue:

        # Remove node from queue and add to topological order
        node = queue.pop(0)
        topological_order.append(node)

        # Reduce indegree for its neighbors
        if node in graph:
            for neighbour in graph[node]:
                indegree[neighbour] -= 1

                # Add new 0 indegree nodes to queue
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

    if len(topological_order) != len(graph):
        print("Cycle exists")

    return topological_order

order = topological_sort_kahn(rows)

source = "svr"
destination = "out"

n_paths = dict()
n_paths[source] = 1
n_paths_dac = dict()
n_paths_fft = dict()
n_paths_both = dict()

for s in order:
    if s not in n_paths:
        n_paths[s] = 0
    if s not in n_paths_dac:
        n_paths_dac[s] = 0
    if s not in n_paths_fft:
        n_paths_fft[s] = 0
    if s not in n_paths_both:
        n_paths_both[s] = 0
    
    if s in incoming:
        for i in incoming[s]:
            if s == "fft":
                n_paths_both[s] += n_paths_dac[i]
                n_paths_fft[s] += n_paths[i]
            elif s == "dac":
                n_paths_both[s] += n_paths_fft[i]
                n_paths_dac[s] += n_paths[i]
            else:
                n_paths[s] += n_paths[i]
                n_paths_dac[s] += n_paths_dac[i]
                n_paths_fft[s] += n_paths_fft[i]
                n_paths_both[s] += n_paths_both[i]

print(n_paths_both[destination])
