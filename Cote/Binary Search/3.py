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
            total += i - mid
    if total<m:
        end = mid-1
    else:
        h = mid
        start = mid +1
print(h)



"""
" 떡볶이 떡 만들기 "
서로 다른 길이의 떡 N개가 있다.
절단기에 높이(H)를 설정하여 떡을 자를 수 있다.
떡은 아래부터 H까지의 높이로 잘리게 되고 윗 부분에 잘리고 남은 떡의 총 길이 합은 M이다.

서로 다른 길이의 떡 N개와 잘리고 남은 떡의 총 길이 합 M이 주어지고
N개의 떡의 각 길이가 주어질 때 높이 H의 값을 구하여라
"""

"""
 로직 
이분탐색으로 푼다!

1. 자를 수 있는 길이의 경우의 수는 길이가 가장 긴 떡볶이와 같아욤 
=> max(array)

2. 이분탐색을 위해 자를 수 있는 길이의 가장 작은 값과 가장 큰 값을 구해욤 
=> start = 0, end = max(array)

3. start와 end의 중간점에서 시작해욤
=> mid = (start + end) // 2

4. array의 값들을 모두 mid로 빼주고 stack에 저장해욥

5. stack에 있는 값을 더해욥 
=> sum(stack)

반복문! 
sum(stack)이 M보다 작다면 end = mid - 1
sum(stack)이 M보다 크다면 end = start + 1
sum(stack)이 M과 같다면 정답!
"""
#
# # n, m = map(int, input().split())
# n, m = 4, 6
# print(n, m)
# # array = list(map(int, input().split()))
# array = [19, 15, 10, 17]
# print(array)
#
# start = 0
# end = max(array)
#
# result = 0
#
# while start <= end:
#     print('*' * 30)
#     print("while 시작!")
#     mid = (start + end) // 2
#     print(f"{mid} 만큼 자를꺼야!")
#     stack = []
#     for i in range(len(array)):
#         cut = array[i] - mid
#         if cut <= 0:
#             continue
#         else:
#             stack.append(cut)
#         i += 1
#     print("스택 :", stack)
#     tsum = sum(stack)
#     print("합계 : ",tsum)
#     if tsum == m:
#         print(f'{m}이랑 똑같넹!')
#         result = mid
#         break
#     elif tsum > m:
#         start = mid + 1
#         print(f"{m} 보다 크다!")
#     else:
#         end = mid - 1
#         print(f"{m} 보다 작다!")
#
# print("정답!!",result)