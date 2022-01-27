import collections


# 단일 싱글 리스트 노드 (개별 체이닝 방식)
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashTable:
    # 초기화 (사이즈 1000 고정, 테이블을 ListNode 클래스를 베이스로 한 딕셔너리 형태로 생성)
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # 삽입
    def put(self, key: int, value: int) -> None:
        # key를 사이즈로 나눈 해시함수(나누기 방법)을 인덱스에 저장
        index = key % self.size
        # 해당 인덱스에 노드가 저장되지 않았다면, 노드를 인덱스에 삽입 후 저장
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 해당 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        # 결국 최종 노드에 도달해서 새노드를 연결하기 전 계속 노드를 타고 가는 과정
        p = self.table[index]
        while p:
            # p.key와 같은 키값을 가진 데이터가 있다면, p.value를 새 value로 갱신한다.
            if p.key == key:
                p.value = value
                return
            # p.next가 없다는 것은 가장 마지막 노드에 도달했다는 것. 그렇게 되면 while 빠져나감
            if p.next is None:
                break
            # p를 p.next로 계속 갱신해줌 (마지막 노드 도착 전까지 계속 갱신)
            p = p.next
        # 반복이 완료 되면 새노드를 p.next에 연결
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        # key를 사이즈로 나눈 해시함수(나누기 방법)을 인덱스에 저장
        index = key % self.size
        # 해당 인덱스의 값이 없을 경우 -1
        if self.table[index].value is None:
            return -1

        # 해당 인덱스 값을 p라는 변수로 받음 (첫 번째 노드)
        p = self.table[index]
        # 노드가 존재할때 일치하는 키 탐색
        while p:
            # 해당 값을 찾으면, 해당 p.value 반환
            if p.key == key:
                return p.value
            # p를 p.next로 계속 갱신해줌 (키값이 같을 때까지)
            p = p.next
        # 못찾으면 역시 -1
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        # key를 사이즈로 나눈 해시함수(나누기 방법)을 인덱스에 저장
        index = key % self.size
        # 해당 인덱스의 값이 없을 경우 -1
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일때
        p = self.table[index]
        # 만약 p.key 와 키값이 같으면
        if p.key == key:
            # p.next가 없으면(단독 노드) 새로운 노드를 생성하고 아니면 p.next로 갱신
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        # p의 노드가 체이닝으로 이미 연결되어 있을 때, 삭제 후 앞 뒤 연결이 필요하여 prev라는 변수를 p로 받음
        prev = p
        while p:
            # 해당 값을 찾으면
            if p.key == key:
                #p의 앞노드와 뒷 노드를 연결한다
                prev.next = p.next
                return
            # 반복하면서 (p.key를 찾을 때까지) p와 prev를 갱신한다
            prev, p = p, p.next