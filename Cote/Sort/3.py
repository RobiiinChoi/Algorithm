n = int(input())
result = []
for _ in range(n):
    name, score = map(str, input().split())
    result.append((name, score))

result = sorted(result, key=lambda x:int(x[1]))

for i in range(n):
    print(result[i][0], end=' ')