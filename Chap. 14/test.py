
n = int(input())
fibo = [0,1]
for i in range(2, n+1):
    num = fibo[i-1]+fibo[i-2]
    fibo.append(num)
print(fibo[n])

# 재귀함수
# def fibo(num):
#     if num<=1:
#         return num
#     return fibo(num-1)+fibo(num-2)
#
# n = int(input())
# print(fibo(n))