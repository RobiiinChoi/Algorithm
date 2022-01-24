"""
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라.
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고, 대각선으로 연결된 것은
떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.
Input
첫째 줄에 도화지의 세로크기와 가로크기가 차례로 주어진다
두 번째 줄부터 n+1 줄까지 그림의 정보가 주어진다.
(그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분)
Output
첫째 줄에는 그림의 개수,
둘째 줄에는 가장 넓은 그림의 넓이 (단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다
1. 아이디어
- (0, 0)부터 지나가면서 1을 만나면 넒이 카운트에 1을 추가
- 지나간 자리는 방문기록에 추가, 0을 만든다
- 2중 for => 값1 && 방문X -> bfs
- bfs 돌면서 그림 개수 +1, 최대값을 갱신
2. 시간복잡도
 - BFS: 0(V+E)
 - V : 500* 500
 - E : 4*500*500
 - V+E : 5*250000 = 100만 < 2억 >> 가능!
3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue (BFS)
"""
# from collections import deque
# import sys
#
# input = sys.stdin.readline
# n, m = map(int, input().split())
# map = [list(map(int, input().split())) for _ in range(n)]
# check = [[False] * m for _ in range(n)]
#
# # 오른쪽 아래쪽 왼쪽 윗쪽
# dy = [0,1,0,-1]
# dx = [1,0,-1,0]
# def bfs(y, x):
#     result = 1
#     q = deque()
#     q.append((y,x))
#     while q:
#         ey, ex = q.popleft()
#         for k in range(4):
#             ny = ey + dy[k]
#             nx = ex + dx[k]
#             if 0<=ny<n and 0<=nx<m:
#                 if map[ny][nx]==1 and check[ny][nx] == False:
#                     result += 1
#                     check[ny][nx]=True
#                     q.append((ny, nx))
#     return result
#
# count = 0
# maxValue = 0
# for i in range(n):
#     for j in range(m):
#         if map[i][j]==1 and check[i][j] == False:
#             # 방문 처리 진행
#             check[i][j] = True
#             # 전체 그림 개수 + 1
#             count += 1
#             # BFS > 그림 크기 구하기
#             maxValue = max(maxValue, bfs(i,j))
#             # 최대값 갱신
#
# print(count)
# print(maxValue)

from collections import deque

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

# 오른쪽 아래쪽 왼쪽 윗쪽
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def bfs(y, x):
    rs = 1
    q = deque()
    q.append((y, x))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)