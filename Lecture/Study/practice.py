'''
N개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때, 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 'YES'를 출력하고,
그렇지 않으면 'NO'를 출력하는 프로그램을 작성해라. 둘로 나뉘는 두 부분집합은 서로소 집합이며, 두 부분집합을 합하면 입력으로 주어진 원래의 집합이 되어야 한다.

첫째 줄에 자연수 N(1 <= N <= 10)이 주어진다.
둘째 줄에 집합의 원소 N개가 주어진다. 각 원소는 중복되지 않는다.

Input :
6
1 3 5 6 7 10
Output :
YES

1. 아이디어
- 인덱스 번호, 방문처리 파라미터 2개 가져오기
- 인덱스 번호가 n이랑 같고, 방문처리 값의 합과 전체에서 방문처리 한 값 차이가 같을 경우, YES 프린트해주기
2. 시간복잡도
3. 자료구조
'''

n = int(input())
arr = list(map(int, input().split()))
visited = []
idx = 0
def dfs(idx, visited):
    if sum(visited) > sum(arr) // 2:
        return print("NO")
    if idx == n:
        if sum(visited) == sum(arr)-sum(visited):
            return print("YES")
        else:
            return print("NO")

    for adj in arr:
        if adj not in visited:
            visited.append(adj)
            idx += 1
            dfs(idx, visited)
            print(all)

dfs(idx,visited)

# cnt = int(input())
# numbers = list(map(map(int, input().split())))
# accum = sum(numbers)
# flag = False
#
# def dfs(L, res):
#     global flag
#
#     if flag == True:
#         return True
#
#     if L ==cnt or res > accum // 2:
#         if accum - res == res:
#             flag = True
#             return True
#         return False
#
#     return dfs(L+1, res+numbers[L])+dfs(L+1, res)
#
# result = dfs(0, 0)
# if result:
#     print("YES")
# else:
#     print("NO")