# s "[]()"
# s "{{{}"
from collections import deque


def is_valid(s):
    stack = []
    match = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for char in s:
        if char not in match:
            stack.append(char)
            #print(char)
            # 여기서 char와 match가 같을 경우 stack.pop()이 이루어져서 빠져나가게 된다
        elif not stack or match[char] != stack.pop():
            return False
    return len(stack) == 0

    def get_card(num):
        queue = deque([n for n in range(1, num+1)])
        while len(queue) > 1:
            queue.popleft()
            queue.append(queue.popleft())

        return queue.popleft()
    print(queue)
    assert get_card(6) == 4

# assert is_valid("{}()[]")

# assert is_valid("{[]}}}")
# # 1. 맨 위 카드를 버린다.
# queue = Queue([1,2,3,4.... N])
# while len(queue)>1:
#     front = queue.pop()
# # 2. 그 다음 제일 위 카드를 제일 뒤로 옮긴다.
#     queue.push(queue.push())
# # 3. 한 장 남은 카드를 반환한다.
# return queue.pop()

