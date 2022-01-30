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

from collections import deque



numbers = [3,1,3,1,5]
target = 3
class ListNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def solution(numbers, target):
    lev = 0
    root = ListNode(0)
    def create(numbers, node, lev):
        node = node
        if lev >= len(numbers):
            return node
        node.left = ListNode(numbers[lev])
        node.right = ListNode(-numbers[lev])
        lev +=1
        create(numbers, node.left, lev)
        create(numbers, node.right, lev)

    create(numbers, root, lev)
    lev_=0
    count = 0
    sum = 0
    def dfs(node, count, lev_, sum):
        if node is None:
            return count
        sum += node.value
        left_count = dfs(node.left, count, lev_+1, sum)
        right_count = dfs(node.right, count, lev_+1, sum)
        if lev_ == len(numbers) and sum == target :
            count +=1
            return count
        count = left_count+right_count-count
        return count
    answer = dfs(root, count, lev_, sum)
    return answer