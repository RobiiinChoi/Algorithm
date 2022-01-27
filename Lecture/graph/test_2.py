

def nqueen(n):

    visited = [-1] * n # 초기화
    count = 0
    answers = []

    # 수 검사 코드
    def is_ok_on(nth_row):
        for row in range(nth_row):
            # 무의미한 수 (백트래킹 진행할 수 )
            if visited[nth_row] == visited[row] or nth_row-row == abs(visited[nth_row] - visited[row]):
                return False
        return True

    # 퀸의 위치를 잡는 코드
    def dfs(row):
        # 범위 밖일 경우
        if row >=n:
            nonlocal count
            count+=1
            print("*"*80)
            print(f"{count}번째 답 - visited: {visited}")
            grid = [['.'] * n for _ in range(n)]
            for idx, value in enumerate(visited):
                grid[idx][value] = 'Q'
            result = []
            for row in grid:
                print(row)
                result.append(''.join(row))
            answers.append(result)
            return

        for col in range(n):
            visited[row] = col
            if is_ok_on(row):
                dfs(row+1)

    dfs(0)
    return answers

assert nqueen(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]



