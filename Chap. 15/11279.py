'''
널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 자연수는 2^31보다 작다.

1. 아이디어
- x가 자연수라면 배열에 x값을 넣는 연산
- x가 0이라면 배열에서 가장 큰 값을 출력, 그 값을 배열에서 제거

2. 시간복잡도 O(logN)
3. 자료구조 - 힙

'''
import heapq
import sys

input = sys.stdin.readline

n = int(input())
result = []

for i in range(n):
    arr = int(input())
    if arr == 0:
        if len(result) == 0:  # 힙에 아무것도 없을 때 0이 들어올 경우
            print(0)
        else:
            print(heapq.heappop(result)[1])
    else:
        heapq.heappush(result, (-arr, arr))
