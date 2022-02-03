import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)

    while len(heap)>1:
        answer +=1
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+b*2)
        if heap[0] >= K:
            return answer
    return -1