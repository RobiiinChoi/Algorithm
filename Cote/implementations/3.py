
n, m = map(int, input().split())
x, y, dir = map(int, input().split())
d = [[0]*m for _ in range(n)]

d[x][y]=1

array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global dir
    dir -=1
    if dir == -1:
        dir = 3

count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny]==0 and array[nx][ny]==0:
        d[nx][ny]=1
        x=nx
        y=ny
        count+=1
        turn_time=0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time+=1
        # 네 방향 모두 갈 수 없는 경우
    if turn_time==4:
        nx = x -dx[dir]
        ny = y -dy[dir]
        if array[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        turn_time = 0

print(count)

def path_finder(start, map, moves):
    x, y = start
    row = len(map)
    col = len(map[0])
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    visited = list()
    for move in moves:
        nx = x + dx[move]
        ny = y + dy[move]
        if nx < 0 or ny < 0 or nx >= row or ny >= col or move[nx][ny] != 1:
            continue
        else:
            x, y = nx, ny
            if (x, y) in visited:
                continue
            else:
                visited.append((x, y))
    return len(visited)