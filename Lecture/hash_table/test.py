import collections

# 개별 체이닝 방식의 경우 싱글 리스트 노드 필요
# key, value, next None으로 초기화
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    # 해쉬테이블 사이즈 및 기본 구조 정의 (딕셔너리 형태에 ListNode 클래스 based)
    def __init__(self):
        self.size = 500
        self.table = collections.defaultdict(ListNode)

    # 삽입 연산 (삽입할 key, value를 가져옴)
    def put(self, key:int, value:int) -> None :
        # key를 size로 나눈 해시함수를 인덱스의 값으로 사용(나누기 방법)
        index = key % self.size
        # 만약 해당 인덱스의 값이 없을 경우(노드 X)
        if self.table[index].value is None:
            # 노드를 삽입
            self.table[index] = ListNode(key, value)
            return

        # 해당 인덱스 값이 있을 경우 p를 헤드로 두고
        p = self.table[index]
        # p.key와 같은 키값을 가진 데이터가 있다면 새 value로 갱신한다
        while p:
            if p.key == key:
                p.value = value
                return
            # p.next가 없으면( 마지막 노드 도달) -> while문 아웃
            if p.next is None:
                break
            # p를 다음 노드로 계속 갱신
            p = p.next
        # 반복이 완료되면 노드를 p.next에 삽입
        p.next = ListNode(key, value)

    # 조회 연산
    def get(self, key:int) -> int:
        # key를 size로 나눈 해시함수를 인덱스의 값으로 사용(나누기 방법)
        index = key % self.size
        # 만약 해당 인덱스의 값이 없을 경우(노드 X) -1 리턴
        if self.table[index].value is None:
            return -1

        p=self.table[index]
        # 해당 값을 찾으면, p.value 반환
        while p:
            if p.key == key:
                return p.value
            # p를 p.next로 계속 갱신해줌 (키값이 같을 때까지)
            p = p.next
        # 못찾으면 -1 리턴
        return -1

    # 삭제 연산
    def remove(self, key:int) -> None:
        index = key%self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때
        p = self.table[index]
        # 만약 p.key와 키값이 같으면
        if p.key==key:
            # p.next가 없으면 새 노드를 인덱스에 넣고 아니면 p.next 갱신
            self.table[index] = ListNode if p.next is None else p.next
            return

        # 연결 리스트 노드가 있을 경우, 삭제 후 앞과 p.next를 연결하기 위한 변수 설정
        prev = p
        while p:
            # 해당 값을 찾은 경우
            if p.key==key:
                # p의 앞 뒤 노드를 연결한다
                prev.next = p.next
                return
            # 반복하면서 p와 prev 갱신
            prev, p = p, p.next