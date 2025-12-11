import itertools

rows = dict()

# source: geeks for geeks
def dfs(node, dest, visited, count):
    if node == dest:
        count[0] += 1
        return
    if node not in visited:
        visited[node] = False
    
    visited[node] = True
    for neighbor in rows[node]:
        if neighbor not in visited or not visited[neighbor]:
            dfs(neighbor, dest, visited, count)
    visited[node] = False

with open("input.txt", "r") as file:
    for line in file:
        start = line.strip().split(':')[0]
        if start not in rows:
            ends = line.strip().split(':')[1].split()
            rows[start] = ends

visited = dict()
for x in rows:
    visited[x] = False
count = [0]

source = "you"
destination = "out"

dfs(source, destination, visited, count)

print(count)