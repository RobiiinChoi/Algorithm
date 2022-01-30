from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

# dfs 재귀
def dfs_recursive(node, visited):
    # 정점 방문 처리
    visited.append(node)

    # 그래프(딕셔너리)에 있는 각 정점의 인접 노드를 방문
    for adj in graph[node]:
        # 해당 인접 노드에 방문한 적이 없다면
        if adj not in visited:
            # 다시 재귀를 호출합니다
            dfs_recursive(adj, visited)

    # 방문한 순서대로 노드 리스트 반환
    return visited

# dfs 반복 (스택사용)
def dfs_iterative(start):
    # 방문처리 변수 초기화
    visited = []
    # 스택에 최초 정점을 넣어줌
    stack = [start]

    # 스택이 차 있을 때 (방문해야 할 정점이 남아있을 때)
    while stack:
        # 하나씩 스택에서 꺼냄
        top = stack.pop()
        # 해당 노드를 방문한 적이 없다면
        if top not in visited:
            # 방문처리
            visited.append(top)
            # 방문 처리 후 노드의 인접 노드 방문하여
            for x in graph[top]:
                # 스택에 채움
                stack.append(x)
    # 방문한 순서대로 노드 리스트 반환
    return visited

# bfs 반복 (큐 사용)
def bfs_iterative(start):
    # 방문 처리 변수 초기화 (최초 노드 큐에 넣어줌)
    visited = [start]
    q = deque([start])

    # 방문할 노드가 남아있을 경우
    while q:
        # 제일 최근에 삽입된 노드를 큐에서 꺼내고
        node = q.popleft()
        # 해당 점점의 인접노드를 방문
        for adj in graph[node]:
            # 해당 노드를 방문한 적이 없으면
            if adj not in visited:
                # 큐에 해당 노드를 넣고
                q.append(adj)
                # 방문처리 한다
                visited.append(adj)
    # 방문한 순서대로 노드 리스트 반환
    return visited