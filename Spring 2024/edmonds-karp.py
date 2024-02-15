import numpy as np

# Edmonds-Karp Algorithm

"""
Takes in three inputs:
    - C: The Capacity Matrix with which you want to find the max flow of
    - s: The node where your source is (entry)
    - t: The node where your sink is (exit)
"""
def edmonds_karp(C, s, t):
    n = len(C)
    F = np.empty((n,n))
    path = bfs(C, F, s, t)
    while path != None:
        flow = min(C[u][v] - F[u][v] for u, v in path)
        for u, v in path:
            F[u][v] += flow
            F[v][u] -= flow
        path = bfs(C, F, s, t)
    return sum(F[s][i] for i in range(n))


"""
Takes in four inputs:
    - C: The Capacity Matrix
    - F: Temporary Adjacency Matrix
    - s: The node where your source is (entry)
    - t: the node where your sink is (exit)
"""
def bfs(C, F, s, t):
    queue = [s]
    paths = {s: []}
    if s == t:
        return paths[s]
    while queue:
        u = queue.pop(0)
        for v in range(len(C)):
            if (C[u][v] - F[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                if v == t:
                    return paths[v]
                queue.append(v)

size = 5
C = np.random.rand(size,size)
for r in range(0,size):
    for c in range(0,size):
        C[c][r] = 0 if r < c else int(C[c][r] * 10) 

print()
print(C)
print("\n")

source = 0
sink = 5
max_flow_value = edmonds_karp(C, source, sink)
print("Edmonds-Karp algorithm")
print("Max Flow: ", max_flow_value)
print()