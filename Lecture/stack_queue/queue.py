class Node:
    # 노드 초기화 (item, 노드 포인터)
    def __init__(self, item, next):
        self.item = item
        self.next = next

# 스택 구현
class Stack:
    # 초기화
    def __init__(self):
        self.top = None

    # push
    # 새 노드가 들어오면 top을 가리키게 한다
    def push(self, value):
        self.top = Node(value, self.top)

    # pop
    def pop(self):
        # 아무것도 없을 때 -> 리턴 None
        if self.top is None:
            return None

        # 그렇지 않으면 self.top을 topNode로 옮기기 (pop)
        topNode = self.top
        # self.top의 이전 노드를 self.top으로 옮기기
        self.top = self.top.next

        # topNode 리턴
        return topNode.item

    # 비었는지 확인
    # 비었으면 None
    def is_empty(self):
        return self.top is None

# 큐 구현
class Queue:
    # self.front(포인터) 초기화
    def __init__(self):
        self.front = None

    # push
    def push(self, value):
        # 큐에 아무것도 없으면 (self.front가 없으면)
        if not self.front:
            # 새롭게 들어온 노드가 self.front를 가리키도록 한다
            self.front = Node(value, None)
            return
        # self.front가 노드를 가리키게 하고
        node = self.front
        # 노드와 노드 다음이 있을 때 (큐에 데이터가 있을 때)
        while node and node.next:
            # 넥스트로 노드를 계속 타고간다
            node = node.next
        node.self = Node(value, None)

    def pop(self):
        if self.front is None:
            return None

        node = self.front
        self.front = self.front.next

        return node.item

    def is_empty(self):
        return self.front is None


class Node:

    def __init__(self, value, next):

        self.value = value

        self.next = next





class Queue:



    # self.front = None으로 초기화

    def __init__(self):

        self.front = None



    # push 함수 선언

    def push(self, value):

        # self.front가 없을 경우에, push함수가 실행되면

        if not self.front:

            # 인자값으로 들어온 value를 담는 새로운 노드를 생성하고,

            # 해당 노드로 self.front를 최신화

            self.front = Node(value, None)

            return



        # self.front가 있을 경우에

        # self.front를 node에 저장. 반복적으로 self.front가 사용되기 때문에

        # 편의성을 보완하기 위함

        node = self.front

        # node와 node.next가 있으면 반복,

        # node를 계속 가리키는 node.next값으로 최신화 하기 때문에,

        # node.next값이 없는 경우는 가장 나중에 입력된 node를 순회하는 경우임

        while node and node.next:

            node = node.next

        # 가장 마지막 노드가 가리키는 값을, 새 Node를 생성해서 저장

        node.next = Node(value, None)





    # pop 함수 선언

    def pop(self):

        # self.front로 저장된 값이 없으면, None을 반환

        if not self.front:

            return None



        # self.front로 저장된 값이 있으면

        # node에 현재 self.front값 저장

        node = self.front

        # self.front 값을 self.front.next 값으로 갱신

        self.front = self.front.next

        # 직전까지 self.front였던 값의 value값 반환

        return node.value



    # is_empty함수 선언

    def is_empty(self):

        # self.front가 노드를 담고 있으면 False, 담고있지 않으면 True를 반환

        return self.front is None