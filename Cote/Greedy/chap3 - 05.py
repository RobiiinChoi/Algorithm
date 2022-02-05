from collections import Counter

n, m =map(int, (input().split()))
ball = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(i+1, n):
        if ball[i] == ball[j]:
            continue
        else:
            count+=1
print(count)

# counter = Counter(k)
# answer = 0
# for num in range(1, m+1):
#     n-= counter[num]
#     answer+=n*counter[num]
# print(answer)