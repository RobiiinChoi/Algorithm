from itertools import combinations
import sys
input = sys.stdin.readline
def solution(map):
    def search(maps, pathogen : list):
        dx = (0, 0, 1, -1)
        dy = (1, -1, 0, 0)
        danger = len(pathogen)
        stack = pathogen[:]
        while stack :
            x, y = stack.pop()
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                try:
                    if maps[ny][nx] == 0:
                        maps[ny][nx] = 2
                        danger += 1
                        stack.append((nx, ny))
                except IndexError:
                    pass
        nonlocal zeros
        return zeros - danger
    ret = 0
    pathos = list()
    blanks = list()
    for row in range(len(map[0])):
        for col in range(len(map)):
            if map[col][row] == 0:
                blanks.append((row, col))
            elif map[col][row] == 2:
                pathos.append((row, col))
    zeros = len(blanks)
    queue = combinations(blanks, 3)
    for each in queue:
        temp_map = [x[:] for x in map]
        for row, col in each:
            temp_map[col][row] = 1
        ret = max(ret, search(temp_map, pathos))
    return ret
N, M = map(int, input().split())
maps = list()
for _ in range(N):
    maps.append(list(map(int, input().split())))
print(solution(maps))