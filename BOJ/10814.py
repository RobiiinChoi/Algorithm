import sys

input = sys.stdin.readline
age_list = []
n = int(input())
for i in range(n):
    age_list.append(list(input().split()))

answer = sorted(age_list, key=lambda x:int(x[0]))
for i in range(n):
    print(answer[i][0], answer[i][1])