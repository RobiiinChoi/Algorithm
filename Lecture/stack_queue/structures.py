class Node:
    #  노드 구조
    def __init__(self, item, next):
        self.item = item
        self.next = next
# 스택 구현
class Stack:
    def __init__(self):
        self.top = None
    # 노드가 들어오면 (노드의 밸류와 위치가) -> 셀프탑이 찬 거기 때문에 셀프탑 채워짐
    def push(self, value):
        self.top = Node(value, self.top)
        print(self.top)

    # 팝 구현 1) 아무것도 없을 때 2) 값이 채워져서 포인터가 있을 때
    def pop(self):
        if self.top is None:
            return None

        topNode = self.top
        self.top = self.top.next

        return topNode.item

    # 스택이 비었는지 확인하는 메서드
    def is_empty(self):
        return self.top is None

class Queue:
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

    def is_empty(self):
        return self.front is None
