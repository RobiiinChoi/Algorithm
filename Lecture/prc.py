def DFS(level, res):
    if level == n:
        print(res)
        return
    DFS(level+1, res + str(level+1))
    DFS(level+1, res)

n = int(input())
DFS(0, "")
#
# def DFS2(level, res):
#     if level == n:
#         print(res)
#         return
#     DFS(level+1, res + str(n[level]))
#     DFS(level+1, res)
#
# n = int(input())
# DFS(0, "")
#
# def DFS3(level, res):
#     if level == n:
#         print(res)
#         return
#     DFS(level+1, res + [N[L]])
#     DFS(level+1, res)
#
# n = int(input())
# DFS(0, [])
#
# n, t = map(int, input().split())
# def dfs_prac(level, res):
#     if level == t:
#         print(res)
#         return
#
#     for i in range(n):
#         dfs_prac(level+1, res+str(i+1))
#
# dfs_prac(0, "")
#

# def factorial(n):
#     result = 1
#     for i in range(n):
#         result *= n-i
#     print(result)
#
# factorial(5)


# def rec_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n*rec_factorial(n-1)
#
# print(rec_factorial(5))
