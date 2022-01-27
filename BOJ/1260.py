import sys
from collections import deque

input = sys.stdin.readline
graph = []
n, m, v = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

def dfs(node, visited):
    visited.append(node)

    for adj in graph[node]:
        if adj not in visited:
            dfs(adj, visited)

    return visited

def bfs(start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)

    return visited

print(dfs(v, graph))
print(bfs(v))
