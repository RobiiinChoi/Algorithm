graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

# 재귀함수
def dfs_recursive(node, visited):
    # 방문처리
    visited.append(node)
    print("방문처리 : " , node, visited)

    # 인접 노드 방문
    for adj in graph[node]:
        print("node :" , node)
        print("element : ",adj)
        if adj not in visited:
            dfs_recursive(adj, visited)
            print("노드끝: ", adj, "방문: ",
                  visited)
    print("final : ", visited)
    return visited

# # 스택
# def dfs_stack(start):x
#     visited = []
#     # 방문할 순서를 담아두는 용도
#     stack = [start]
#
#     # 방문할 노드가 남아있는 한 아래 로직을 반복한다.
#     while stack:
#         # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
#         top = stack.pop()
#         visited.append(top)
#         # 인접 노드를 방문한다.
#         for adj in graph[top]:
#             if adj not in visited:
#                 stack.append(adj)
#
#     return visited

#스택
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

