n = int(input())
coin = list(map(int, input().split()))

coin.sort()
target = 1
for c in coin:
    if target < c:
        break
    target += c

print(target)