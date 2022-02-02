class BinaryMaxHeap:
    def __init__(self):
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
        # 따라서 0번째 인덱스를 None으로 미리 지정함
        self.items = [None]

    def __len__(self):
        # 맨 밑에 삽입되는 노드의 경우 전체 길이에서 -1 한 인덱스에 위치.
        # 매직 매서드에서 바로 호출 할 수 있게 조정
        return len(self.items) - 1

    def _percolate_up(self):
        # cur(현재노드)의 인덱스 저장
        cur = len(self)
        # left 라면 2*cur, right 라면 2*cur + 1 이므로 parent 는 항상 cur // 2
        # 현재 노드에서 부모 노드 인덱스 찾기
        parent = cur // 2

        # parent가 0보다 클 때까지 (최상단 노드에 도달 할 때까지. 인덱스 0은 None으로 더미노드)
        while parent > 0:
            # 현재 값이 부모노드보다 큰 경우, 위치를 스왑한다
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            # 그 위의 노드와 또 비교해야 하므로 (맥스힙) 부모 인덱스 값을 현재로 변경하고,
            # 현재 노드의 부모 인덱스 값을 찾아서 부모 인덱스 값에 저장
            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest)

    # 삽입 (리스트에 파라미터 k를 붙이고, percolate up 함수를 실행)
    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root