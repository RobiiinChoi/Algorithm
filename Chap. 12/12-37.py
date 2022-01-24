# 모든 부분 집합을 리턴하라
# input nums = [1,2,3]
# output = [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
from collections import deque

# nums = list(map(int, input().split(',')))
def bfs_queue(nums):
    answer = []
    q = deque()
    for i in range(len(nums)): # range(3)
        q.append(([nums[i]], i+1)) #num[0], num[1], num[2]

    while q:
        tup = q.popleft() # num[0], num[1]
        l, idx = tup[0], tup[1] # l = num[0], idx = num[1]
        answer.append(l)
        if idx == len(nums):
            continue
        for i in range(idx, len(nums)):
            new_list = l + [nums[i]]
            q.append((new_list, i+1))

    return [[]]+answer #공집합 더하기

print(bfs_queue(['1','2','3']))