# N x M 크기의 얼음 틀이 있다. 구멍이 있는 부분은 0, 칸막이가 존재하는 부분은 1
# 구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어 있는 것으로 간주
# 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램

from collections import deque

N, M = map(int, input().split())
graph = []
# 얼음틀 받아오기
for i in range(N):
    graph.append(list(map(int, input())))

# 남, 북, 동, 서 // 방향은 통일성있게 마음대로 (어짜피 다 돌게됨)
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(x,y):
    q = deque()
    q.append((x, y)) # (0,0)부터 좌표 돌기

    if graph[x][y]==1: # 값이 1이면 리턴 False
        return False

    while q: # (0,0) 위치를 기준으로 bfs탐색
        x, y = q.popleft() # x, y 값 큐에서 빼서 1로 변경시킴 (재방문 x)
        graph[x][y]=1
        for i in range(4): # 4방향으로 돌기
            nx = x + dx[i] # 상하좌우 맞춰서 돌아야 되므로 인덱스 값 같게함
            ny = y + dy[i]
            if 0 <= nx < N and 0<= ny < M and graph[nx][ny]==0: # nx와 ny가 범위 내에 있고 0인 경우에는 큐에 추가
                    q.append((nx, ny))
    return True

# 아이스크림 개수
count = 0
for i in range(N):
    for j in range(M):
        if bfs(i, j) == True:
            count += 1 # 아이스크림 1개가 만들어질 경우 True 리턴 -> 1 추가

print(count)



