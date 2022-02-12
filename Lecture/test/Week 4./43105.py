

def solution(triangle):
    # triangle의 최상단은 누적합을 구할 필요가 없으므로 1 - len(triangle)까지 돌림
    # 별도의 메모이제이션 없이 현재 좌표의 값의 누적값을 구하는 방식으로 했습니다
    for i in range(1, len(triangle)):
        # j는 항상 1보다 한개 더 원소가 많기 때문에 i+1로 정해놨습니다. (1일 때 2개, 2일 때 3개)
        # memo[r][c] = tri[r][c] + max(dp(r - 1, c - 1), dp(r - 1, c)) 이 부분을 각 인덱스 별로 쪼개놨다고 보시면 됩니다.
        for j in range(i + 1):
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j == i:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j], triangle[i-1][j-1])
    return max(triangle[-1])

tri = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(tri))
