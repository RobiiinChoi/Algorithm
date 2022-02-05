

import sys

input = sys.stdin.readline
n = int(input())
requested_budget = list(map(int, input().split()))
m = int(input())

start = 1
end = max(requested_budget)

while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in requested_budget:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)