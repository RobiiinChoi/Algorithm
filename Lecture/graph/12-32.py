# def island_dfs_stack(grid):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     rows, cols = len(grid), len(grid[0])
#     cnt = 0
#
#     for row in range(rows):
#         for col in range(cols):
#             if grid[row][col] != '1': # 0 1
#                 continue
#
#             cnt += 1
#             stack = [(row, col)]
#
#             while stack:
#                 x, y = stack.pop()
#                 grid[x][y] = '0'
#                 for i in range(4):
#                     nx = x + dx[i]
#                     ny = y + dy[i]
#                     if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
#                         continue
#                     stack.append((nx, ny))
#     return cnt
#
#
# assert island_dfs_stack(grid=[
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]) == 1
# assert island_dfs_stack(grid=[
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]) == 3

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return

            grid[i][j] = 0

            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count
