from collections import deque

# 트리 노드
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 트리만드는 함수
def make_tree_by(lst, idx):
    # parent = None 초기화
    parent = None
    # 만약 리스트길이가 idx보다 크다면
    if idx < len(lst):
        # 해당 인덱스의 값을 value에 저장
        value = lst[idx]
        # value가 없으면 (리프노드까지 도달)
        if value is None:
            # 재귀함수 종료
            return

        # parent에 현재 트리 노드 저장
        parent = TreeNode(value)
        # 현재 노드의 오른쪽, 왼쪽 노드로 이동하면서 idx값 증가시키고 재귀함수 호출
        parent.left = make_tree_by(lst, 2 * idx +1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    # 루트 노드 반환하면서 함수 종료
    return parent

# 정렬된 리스트를 이진 탐색 트리로
def sorted_array_to_bst(lst):
    # 리스트에 노드가 없으면 빈 배열 리턴
    if not lst:
        return None

    # 리스트 길이의 반을 중앙값으로 산정
    mid = len(lst)

    # 트리의 중앙값으로 트리 노드 생성, 왼쪽 오른쪽을 중앙값 기준으로 재귀 호출
    node = TreeNode(lst[mid])
    node.left = sorted_array_to_bst(lst[:mid])
    node.right = sorted_array_to_bst(lst[mid+1:])

    return node

# 이진 탐색 트리 -> 리스트 만드는 함수
def make_lst_by_bst(root, limit):
    # 루트 노드가 없으면 빈 배열 리턴
    if not root:
        return []

    # 리스트 빈배열 생성, 루트노드를 담은 데크 생성
    lst = []
    q = deque([root])

    # 큐가 남아있다면, 리스트의 길이가 더 크다면 break
    while q:
        if len(lst) > limit:
            break
        # 큐를 팝하여 노드에 담음
        node = q.popleft()
        # 노드가 있다면
        if node:
            # 리스트에 노드 값을 넣고 큐에 left, right를 붙이고
            lst.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            # 노드가 없으면 None을 붙인다
            lst.append(None)

    # 리스트 반환
    return lst

def test_sorted_array_to_bst(lst):
    if not lst:
        return []
    root = sorted_array_to_bst(lst)
    return make_lst_by_bst(root, len(lst))

from collections import deque





# 이진 트리 노드

# 왼쪽, 오른쪽 자식을 갖는다

class TreeNode:

    def __init__(self, val, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right





# 리스트를 받아 이진 트리로 만드는 함수

def make_tree_by(lst, idx):

    # idx가 리스트 범위내에 있ㅌ을 때

    parent = None

    if idx < len(lst):

        # idx에 해당하는 값이 없으면 리턴

        value = lst[idx]

        if value is None:

            return



        # 해당 value로 트리 노드 생성

        # 왼쪽, 오른쪽 자식을 재귀적으로 생성

        parent = TreeNode(value)

        parent.left = make_tree_by(lst, 2 * idx + 1)

        parent.right = make_tree_by(lst, 2 * idx + 2)



    return parent





# 정렬된 리스트를 이진 탐색 트리로 만드는 함수

def sorted_array_to_bst(lst):

    # 리스트에 값이 없으면 리턴

    if not lst:

        return None



    # 중앙은 리스트 길의 반

    mid = len(lst) // 2



    # 리스트의 중앙값으로 트리 노드 생성

    # 왼쪽, 오른쪽 자식은 리스트를 중앙값을 기준으로 반으로 나누어 재귀적으로 생성

    node = TreeNode(lst[mid])

    node.left = sorted_array_to_bst(lst[:mid])

    node.right = sorted_array_to_bst(lst[mid + 1:])



    return node





# 이진 탐색 트리의 루트를 받아 리스트로 만드는 함수

def make_lst_by_bst(root, limit):

    if not root:

        return []



    lst = []

    # 큐에 루트 노드를 넣고 시작

    q = deque([root])



    while q:

        if len(lst) > limit:

            break



        # 큐에서 노드를 꺼내 값이 None이 아니면 lst에 추가

        # 양쪽 자식을 큐에 추가

        node = q.popleft()

        if node:

            lst.append(node.val)

            q.append(node.left)

            q.append(node.right)

        else:

            # node None일 시 lst에 None 추가

            lst.append(None)



    return lst

