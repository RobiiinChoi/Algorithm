import sys

k, n = map(int, input().split())
lan_list = [int(sys.stdin.readline()) for _ in range(k)]

start = 1
end = max(lan_list)
while start <= end:
    total = 0
    mid = (start+end)//2
    for i in lan_list:
        total += i // mid

    if total>=n:
        start = mid+1
    else:
        end = mid-1
print(end)

