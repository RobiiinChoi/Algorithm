# 이진 탐색 함수 만들기 : target을 찾아서 인덱스 값 반환
# start, end, mid 포인트 3개로 이진탐색 진행하는 함수

def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid]<target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

n, target = map(int, input().split())
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n-1)
if result == None:
    print("타겟이 없습니다")
else:
    print(result+1)