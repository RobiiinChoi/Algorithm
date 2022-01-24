from collections import deque
# 7회차: https://teamsparta.notion.site/7-BFS-1ee648888f754c6497b3bdf4ca466ad4

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def bfs_queue(start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft() # queue에서 맨왼쪽을 빼서 정점으로 만듬
        for adj in graph[node]: # 해당 정점의 인접노드들을 방문한다
            if adj not in visited: # 방문하지 않았다면,
                q.append(adj) # 큐에 해당 노드를 붙인다 (인접노드들을 방문하려고)
                visited.append(adj) # 그리고 해당 노드를 방문처리한다

    return visited


assert bfs_queue(1) == [1, 2, 3, 4, 5, 6, 7]