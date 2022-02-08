'''
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)
모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다.
셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다.
서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오.
단, 모든 간선의 가중치는 10 이하의 자연수이다.

첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다.
시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
'''
import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
v, e = map(int, input().split())
k = int(input())
graph = [[] * (v+1) for _ in range(v+1)]
INF = sys.maxsize
dist = [INF] * (v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra_pq(start):

    q = []
    # 튜플일 경우 0번째 요소 기준으로 최소 힙 구조.
    # 첫 번째 방문 누적 비용은 0이다.
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        # 누적 비용이 가장 작은 녀석을 꺼낸다.
        distance, now = heapq.heappop(q)

        # 이미 답이 될 가망이 없다.
        if dist[now] < distance:
            continue

        # 인접 노드를 차례대로 살펴보며 거리를 업데이트한다.
        for next, weight in graph[now]:
            cost = weight + distance
            if cost < dist[next]:
                dist[next] = cost
                heapq.heappush(q, (cost, next))

    return dist

dijkstra_pq(k)

for i in range(1, v+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])