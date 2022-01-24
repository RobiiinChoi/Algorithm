from structure import dfs_recursive, dfs_stack
# 6회차 https://teamsparta.notion.site/6-DFS-8d7f8495cd464534b5b72269af5221f1

assert dfs_recursive(1, []) == [1, 2, 5, 6, 7, 3, 4]
assert dfs_stack(1) == [1, 4, 3, 5, 7, 6, 2]

# def recursive_function(i):
#     if i==100:
#         return i
#     print(i, '번째 재귀함수에서' , i+1, '번째 재귀함수를 호출합니다')
#     recursive_function(i+1)
#     print(i,'번째 재귀함수를 종료합니다')
#
# recursive_function(1)

# DFS, BFS에서 중요한 점 (스택, 큐로 구현 시)
# 1. discovered (방문 노드 리스트) 생성 후 스택이나 큐에서 pop된 친구들을 visited로 이동시킨다.
# discovered = [], stack = [start] // queue = deque([start]) // while True: node = stack.pop() // node= queue.popleft() // visited.append(node)
# 2. 스택에서 꺼내서 해당 노드의 방문 이력을 확인한다.
# v = stack.pop() / if v not in visited
# 3. 방문한 노드가 아닐 시 해당 노드를 방문노드에 추가한다.
# if v not in visited: discovered.append(v)
# 4. 해당 노드를 방문해서 인접노드를 확인하고 스택에 올린다
# for w in graph[v]:stack.append(w)
