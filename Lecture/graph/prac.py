from collections import deque
# 큐로 BFS 구현

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

# assert bfs_queue('A') == ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 스택
def dfs_stack(start):
    visited=[]
    stack = [start]

    while stack:
        top=stack.pop()
        visited.append(top)
        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)

    return visited



