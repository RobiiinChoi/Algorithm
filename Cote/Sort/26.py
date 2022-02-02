import sys
input = sys.stdin.readline

n = int(input())
result = []
for _ in range(n):
    result.append(int(input()))

result.sort()
sum = 0
for i in range(len(result)-1):
    sum += result[i] + result[i+1]
    result[i+1]=sum
print(sum)