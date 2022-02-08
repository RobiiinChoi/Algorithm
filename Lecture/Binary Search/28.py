'''
인덱스와 해당 인덱스의 값이 일치할 경우 인덱스 값
그게 아닐 경우 -1 리턴

인덱스 중간을 기준으로 그 값이 인덱스 value와 동일할 경우를 찾는게 키포인트
mid의 인덱스 값과 값을 비교해서 인덱스 값이 더 크면 스타트 지점을 옮기고, 반대이면 엔드 지점을 내리는게 포인트

시간 복잡도 O(logN)

자료구조 : 리스트
'''

n = int(input())
arr = list(map(int, input().split()))

start = 0
end = len(arr) - 1

def search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(search(arr, start, end))