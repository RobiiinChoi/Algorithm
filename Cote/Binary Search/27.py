'''
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬.
이 수열에서 x가 등장하는 횟수 계산. 수열 {1,1,2,2,2,2,3}이 있을 때 x = 2라면,
현재 수열에서 값이 2인 원소가 4개이므로 4를 출력

시간복잡도는 O(logN)으로 설정
'''
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = len(arr)-1

def count(arr, left, right):
    L_idx = bisect_left(arr, left)
    R_idx = bisect_right(arr, right)
    return R_idx - L_idx

result = count(arr, x, x)
if result == 0:
    print(-1)
else:
    print(result)



