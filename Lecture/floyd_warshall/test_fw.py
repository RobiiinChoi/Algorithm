import sys
from collections import defaultdict
from pprint import pprint

from Lecture.floyd_warshall.floyd_warshall import floyd_warshall

with open('testcase_fw.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline

    N = int(input())
    M = int(input())
    
    graph = defaultdict(list)
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    print(len(graph))
    pprint(floyd_warshall(graph))