## 시간초과


import sys

input= sys.stdin.readline

n, m = map(int, (input().split()))
tree = list(map(int, input().split()))

start = 0
end = max(tree)
height = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in tree:
        if i>mid:
            total += i-mid
    if total<m:
        end = mid-1
    else:
        height = mid
        start = mid+1
print(height)

N,M,*T=map(int,open(0).read().split());a=[0,77**5]
while N:c=sum(a)//2;z=sum(i-c for i in T if i>c);N=a[0]+1<a[z!=M];a[z<M]=c
print(c)