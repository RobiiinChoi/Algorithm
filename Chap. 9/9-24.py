# 스택을 이용해 다음 연산을 지원하는 큐를 구현하라
# push(x) : x를 큐 맨 마지막에 삽입
# pop() : 큐 맨 처음에 있는 요소 제거
# peek() : 큐 맨 처음에 있는 요소를 조회
# empty() : 큐가 비어 있는지 여부 리턴
# MyQueue queue = new MyQueue():
# queue.push(1)
# queue.push(2)
# queue.peek()
# queue.pop()
# queue.empty()

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class MyQueue:
    def __init__(self):
        self.front = None

    def push(self, value):
        if not self.front:
            self.front = Node(value, None)
            return

        node = self.front
        while node and node.next:
            node = node.next
        node.self = Node(value, None)

    def pop(self):
        # queue가 비어있을 경우
        if self.front is None:
            return None

        node = self.front
        self.front = self.front.next

        return node.item

    def peep(self):
        # 큐 처음에 있는 요소를 조회한다
        if not self.front:



