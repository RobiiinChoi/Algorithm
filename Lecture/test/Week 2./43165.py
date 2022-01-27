from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.popleft()
        # print(temp, idx)
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            # print("temp :", queue[0][0], "index :" ,queue[0][1])
            queue.append([temp-numbers[idx], idx])
            # print("temp :", queue[0][0], "index :" ,queue[0][1])
        else:
            if temp == target:
                answer += 1
    return answer

solution([1, 1, 1, 1, 1], 3)