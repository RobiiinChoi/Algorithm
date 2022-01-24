def addressnum(houses):
    # 동서남북 비교할 좌표
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(houses), len(houses[0])
    danji = []

    for row in range(rows):
        for col in range(cols):
            # 만약 해당 위치에 집이 없다면 패스
            if houses[row][col] != '1':
                continue
            # 단지 번호 부여
            danjihouse = 0
            # 집 좌표 담아줄 스택 생성
            stack = [(row, col)]

            # 스택에 좌표가 담겨 있는 동안
            while stack:
                # 마지막에 담긴 집의 좌표를 가져옵니다
                x, y = stack.pop()
                # 해당 좌표의 집은 1 -> 0으로 처리해줍니다
                houses[x][y] = '0'
                danjihouse += 1
                # 해당 좌표의 집 동서남북을 돌며 주변에 빈집이 있는지, 지도를 벗어나진 않았는지 확인합니다.
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or houses[nx][ny] != '1':
                        continue
                    # 그렇게 동서남북을 돌며 주변에 집이 있다면, 스택에 이미 있는 집인지 확인합니다.
                    if stack.count((nx,ny)) > 0:
                        continue
                    # 스택에도 없다면 이제 좌표를 추가합니다.
                    stack.append((nx, ny))
            # 만들어뒀던 리스트에 이번 단지에 몇 집 있었는지 추가합니다.
            danji.append(danjihouse)
    # 단지 리스트를 오름차순 정렬해줍니다
    danji.sort()
    print (len(danji))
    for i in danji:
        print (i)


mapsize = int(input())
houses = []

for i in range(mapsize):
    houses.append(list(map(str, input())))

addressnum(houses)