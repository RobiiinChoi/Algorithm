
# 맥스힙 구현
class BinaryMaxHeap:
    def __init__(self):
        # 계산 편의를 위해 0번째 인덱스를 dummy로 만들고 시작
        self.iten = [None]

    # 길이 매직메서드를 -1 길이로 초기화 (위의 0번째 인덱스 제외하기 위해)
    def __len__(self):
        return len(self.items)-1

    # 노드를 위로 올리는 메소드 구현(삽입 시, 비교후 부모노드랑 비교)
    def _percolate_up(self):
        # 현재 노드의 인덱스 저장
        cur = len(self)
        # 현재 노드에서 부모 노드 인덱스를 찾는다 ( 자식노드가 부모노드의 *2 이므로 나누기로 찾음
        parent = cur//2

        # 최상단 노드에 도달할 때까지 (0이 더미노드이기 떄문에 0 이상으로 카운트)
        while parent > 0:
            # 현재 값이 부모노드보다 클 경우 부모와 스왑하여 자리 바꿈
            if self.item[cur] > self.items[parent]:
                self.items[cur], self.items[parent]= self.item[parent], self.item[cur]

            # 그 위의 노드와 비교해야 하기 떄문에 부모 인덱스값을 현재노드로 옮기고,
            # 현재 노드의 부모 인덱스 값을 찾아서 부모 인덱스 값에 저장한다
            cur = parent
            parent = cur//2

    # 노드를 밑으로 내리는 메소드 (추출시, 자식 노드랑 비교해서 노드 인덱스 조정)
    def _percolate_down(self, cur):
        # 현재노드를 가장 큰 인덱스 값으로 설정
        biggest = cur
        # 자식 노드의 인덱스 값의 경우 2배를 곱하고 오른쪽의 경우 +1을 해준다
        left = 2 * cur
        right = 2 * cur + 1

        # 왼쪽 노드가 전체인덱스 길이보다 작고, 현재 노드보다 큰 값일 경우 왼쪽을 biggest로 설정
        if left <= len(self) and self.items[left]>self.items[biggest]:
            biggest = left

        # 오른쪽 노드가 전체인덱스 길이보다 작고, 현재 노드보다 큰 값일 경우 오른쪽을 biggest로 설정
        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        # 현재 노드에서 biggest가 옮겨간 경우
        if biggest != cur:
            # biggest와 현재노드의 값을 스왑하고
            self.item[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            # 다시 함수 반복한다(리프노드에 도달하지 않았으므로)
            self._percolate_down(biggest)

    # 삽입 함수
    def insert(self, k):
        # 노드 맨 마지막에 k값을 붙이고
        self.item.append(k)
        # perculate_up 함수 실행
        self._percolate_up()

    # 추출 함수
    def extract(self):
        # 노드 갯수가 1이하이면
        if len(self)<1:
            # None 리턴
            return None

        # 루트를 인덱스 1번으로 맞추고, 루트를 맨 마지막 노드로 이동 후 팝, 진행
        # 스왑된 루트를 percolate_down 실행
        root = self.item[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        # 루트 반환
        return root
