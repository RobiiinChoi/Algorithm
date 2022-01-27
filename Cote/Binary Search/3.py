'''
    절단기에 높이를 지정하면 줄지어진 떡을 한 번에 절단한다.
    높이가 H보다 긴 떡은 H 위의 부분이 잘리고, 낮은 떡은 잘리지 않는다
    19 14 10 17 -> H: 15 => 4 0 0 2 (손님이 6 가져간다)
    손님이 왔을 때 요청한 총 길이가 M, 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값

    1. 아이디어
    - H의 크기는 0에서 가장 긴 떡의 크기 사이이다
    - 최소한 손님이 필요한 떡 M 이상은 남아야 한다
    - H의 크기를 조절하면서 M 이상의 떡을 남길 수 있는 최댓값을 찾는다
    2. 시간복잡도
    3. 자료구조
    - 이진 탐색

'''

n, m = map(int, input().split())
array = list(map(int, input().split()))
start = 0
end = max(array)
h = 0
while start<= end:
    total = 0
    mid = (start+end)//2
    for i in array:
        if i>mid:
            total += i - mid # 궁금한 부분 : mid 보다 작은 i 역시 total에 합쳐야되는데 해당떡은 어디감? total>m인 경우는 따로 조건을 안붙여주는건가?
    if total<m:
        end = mid-1
    else:
        h = mid
        start = mid +1
print(h)
