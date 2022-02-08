'''

이 문제에서는 다음과 같은 2가지 사항을 판별해야 한다.

모든 노드가 신호를 받는 데 걸리는 시간
모든 노드에 도달할 수 있는지 여부
첫 번째로 판별해야 하는, 모든 노드가 신호를 받는데 걸리는 시간이란 가장 오래 걸리는 노드까지의 최단 시간을 말하며, 이는 다익스트라 알고리즘(최단경로 알고리즘)으로 추출할 수 있다.

두 번째로 모든 노드에 도달할 수 있는지 여부다. 이는 모든 노드의 다익스트라 알고리즘 계산 값이 존재하는지 유무로 판별할 수 있다.

'''
import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        Q = [(0, k)]
        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heqppush(Q, (alt, v))

        if len(dist) == n:
                return max(dist.values())

        return -1