import collections
import sys

input = sys.stdin.readline
maze=[]
n, m = map(int, input().split())
for _ in range(n):
    maze.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = collections.deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1 # 잘모르겠음
                queue.append((nx, ny))
    return maze[n-1][m-1]

print(bfs(0, 0))
