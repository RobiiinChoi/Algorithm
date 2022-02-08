INF = int(1e9)


def floyd_warshall(graph):
    N = len(graph)
    print(N)
    # 시작 시 노드 0부터 시작하므로 N+1 (defaultdict - 인덱스 1부터 시작)
    # list 시작 시 N
    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    for idx in range(1, N + 1):
        dist[idx][idx] = 0

    for start, adjs in graph.items():
        for adj, d in adjs:
            dist[start][adj] = d

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

    return dist