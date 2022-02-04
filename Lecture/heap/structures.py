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


# # 최대 힙 클래스 선언
#
# class BinaryMaxHeap:
#
#     # 힙 내부 저장공간의 0번째 인덱스 값을 None으로 초기화
#
#     # 계산상 편의를 위해
#
#     def __init__(self):
#
#         self.items = [None]
#
#     # 저장공간의 길이 반환 매직메소드 선언
#
#     def __len__(self):
#
#         return len(self.items) - 1
#
#     # 상향이동함수 선언
#
#     def _percolate_up(self):
#
#         # 힙 가장 끝에 삽입된 요소의 인덱스 값을 cur에 저장
#
#         cur = len(self)
#
#         # 부모값의 인덱스를 parent에 저장
#
#         parent = cur // 2
#
#         # 부모값의 인덱스가 0보다 크면 반복
#
#         # 부모값의 인덱스가 0이 되는 경우는 cur이 루트를 가리킬 때
#
#         # 따라서 cur이 루트가 될 때 까지 반복
#
#         while parent > 0:
#
#             # 만약 현재 가리키는 값이 부모값보다 큰 경우
#
#             if self.items[cur] > self.items[parent]:
#                 # 두 인덱스가 가리키는 값을 교환
#
#                 self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
#
#             # 가리키는 인덱스 값을 부모 값으로 최신화
#
#             cur = parent
#
#             # parent값은 cur의 부모 인덱스 값으로 최신화
#
#             parent = cur // 2
#
#     # 하향이동함수 선언
#
#     def _percolate_down(self, cur):
#
#         # 추출함수를 통해 인자값으로 1이 들어오면, biggest에 1 저장
#
#         # 해당 인덱스가 가리키는 값은, 추출을 위해 끝값과 교환한 값임
#
#         biggest = cur
#
#         # left와 right는 각각 cur의 자식 인덱스 값 저장
#
#         left = 2 * cur
#
#         right = 2 * cur + 1
#
#         # 만약 left, right가 저장공간의 인덱스 값 안을 가리키고,
#
#         # 가리키는 값이 biggest로 가리키는 값보다 크다면, 두 인덱스 값 교환
#
#         if left <= len(self) and self.items[left] > self.items[biggest]:
#             biggest = left
#
#         if right <= len(self) and self.items[right] > self.items[biggest]:
#             biggest = right
#
#         # 위의 조건문에서 인덱스 값 교환여부를 확인하고,
#
#         # 교환되었으면 현재 biggest가 가리키는 값(원래 left 혹은 right가 가리키던 자식값)과
#
#         # 현재 cur이 가리키는 값을 교환하고, 교환한 값을 인자로 다시 하향이동함수 선언
#
#         if biggest != cur:
#             self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
#
#             self._percolate_down(biggest)
#
#     # 삽입함수 선언
#
#     def insert(self, k):
#
#         # 맨 끝에 새 값을 추가하고 상향이동 함수 호출
#
#         self.items.append(k)
#
#         self._percolate_up()
#
#     # 추출함수 선언
#
#     def extract(self):
#
#         # 저장배열의 길이가 1보다 작으면, 함수 종료
#
#         if len(self) < 1:
#             return None
#
#         # 추출할 현재 최대 값을 root에 저장
#
#         root = self.items[1]
#
#         # root값과 끝 값을 교환
#
#         self.items[1] = self.items[-1]
#
#         # root에 저장된 맨 끝 값 추출
#
#         self.items.pop()
#
#         # 맨 끝에 있던 1번 인덱스 값을 인자로 하향이동함수 선언
#
#         self._percolate_down(1)
#
#         # 원래 최대값 반환
#
#         return root