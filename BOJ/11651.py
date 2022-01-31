'''
좌표 정렬하기 2
2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다.
(-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

1. 아이디어 : x, y 좌표 바꿔서 솔팅하려다 안되서 걍 람다식 사용
2. 시간 복잡도 : O(n)
3. 자료구조 : 리스트

Input:
5
0 4
1 2
1 -1
2 2
3 3
Output:
1 -1
1 2
2 2
3 3
0 4
'''
import sys

input = sys.stdin.readline

n = int(input())
location = []
for i in range(n):
    x, y = map(int, input().split())
    location.append([x,y])

n_location = sorted(location, key=lambda x: (x[1], x[0]))
for i in range(len(n_location)):
    print(n_location[i][0], n_location[i][1])