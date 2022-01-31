'''
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다.
다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다.
연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.
0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.
벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.
연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

1. 아이디어
- 바이러스는 상하좌우 인접한 빈칸으로 이동 가능
- 바이러스의 좌표를 큐에 넣은 뒤에 BFS로 확장
- 벽의 경우 모든 경우의 수 확인해야 함 (최대값이 어떻게 될지 모름)
- 벽 만들고 BFS, 다시 벽 지우고 좌표 이동 후 벽 만들고 BFS, 벽 지우고 반복
2. 시간복잡도
3. 자료구조 - 너비우선, 브루트포스, 그래프
'''
import copy
import sys
from collections import deque

input = sys.stdin.readline

# bfs 탐색
def bfs():
    # 큐 생성 후 그래프와 동일한 모양의 그래프 카피
    q = deque()
    copy_graph = copy.deepcopy(graph)
    # 그래프 돌면서 바이러스인 좌표를 큐에 넣는다
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 2:
                q.append((i, j))

    # 큐가 차있을 때
    while q:
        # 큐에서 꺼내서 x, y 좌표에 넣고
        x, y = q.popleft()
        # 인접 노드로 순회
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 순회할 때 범위 밖이면 다시 돌고
            if nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue
            # 만약에 그래프 값이 0이면(빈칸), 2로 바꿔주고 (바이러스 확산 가능지역), 큐에 다시 넣는다
            if copy_graph[nx][ny] == 0:
                copy_graph[nx][ny]=2
                q.append((nx, ny))

    # 개수 전역변수 선언
    global answer
    # 안전영역 카운트 변수
    cnt = 0

    # 그래프 돌면서 값이 0이면 카운트
    for i in range(n):
        cnt += copy_graph[i].count(0)

    # 안전영역 카운트 변수와 answer 중에 더 큰 값을 답으로 대치한다
    answer = max(answer, cnt)

# 벽 만드는 함수
def makeWall(cnt):
        # 벽이 3개 다 세워졌으면
        if cnt == 3:
            # bfs 탐색
            bfs()
            return

        # 그래프 돌면서 (0, 0 ~ n-1, m-1)까지 다 돌아야함 (벽 다 쳐봐서 최대값 구해야되니)
        for i in range(n):
            for j in range(m):
                # 그래프 좌표가 0이면(비었으면)
                if graph[i][j] == 0:
                    # 벽치기
                    graph[i][j] = 1
                    # 벽 개수 올려서
                    makeWall(cnt+1)
                    # 다시 벽 부수기
                    graph[i][j] = 0


n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
makeWall(0)
print(answer)