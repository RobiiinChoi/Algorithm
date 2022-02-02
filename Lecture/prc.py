
# 트리 노드 클래스 (value와 자기 자식의 d
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 이진 트리 (리스트와 인덱스 번호를 매개변수로 갖는다)
def make_tree_by(lst: list, idx: int):
    # parent = None 초기화
    # 재귀를 통해 leaf node 자식에 도달했을 때 return None
    parent = None
    # 만약 리스트 길이가 idx 보다 크다면
    if idx < len(lst):
        #해당 인덱스 값을 value에 저장한다
        value = lst[idx]
        # value가 없으면 (리프노드까지 도달) 재귀함수 종료
        if value is None:
            return None

        # parent에 현재 트리 노드 저장
        parent = TreeNode(value)
        # idx값을 증가시키며 현재 노드의 오른쪽, 왼쪽 서브트리로 순회
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)
    # 루트 노드 반환하면서 함수를 종료한다
    return parent


# # 트리 노드 클래스
#
# # 왼쪽 오른쪽 자식과 value 가짐
#
# class TreeNode:
#
#     def __init__(self, val, left=None, right=None):
#         self.val = val,
#
#         self.left = left
#
#         self.right = right
#
#
# # 리스트로 이진 트리 만드는 함수
#
# def make_tree_by(lst: list, idx: int):
#     # parent 초기값은 None
#
#     # 재귀를 통해 leaf node 자식에 도달했을 떄 return 값은 None
#
#     parent = None
#
#     # idx가 리스트 길이 범위 내에 있을 때
#
#     if idx < len(lst):
#
#         value = lst[idx]
#
#         # value None이면 리턴
#
#         if value is None:
#             return None
#
#         # lst[idx] 저장된 값으로 트리 노드 생성
#
#         parent = TreeNode(value)
#
#         # 양쪽 자식을 리스트에서 idx로 찾아 재귀 호출
#
#         parent.left = make_tree_by(lst, 2 * idx + 1)
#
#         parent.right = make_tree_by(lst, 2 * idx + 2)
#
#     # 해당 노드 리턴
#
#     return parent

# 트리노드 선언

# class TreeNode:
#
#     # value, left, right를 인자로 받으며, 간선 left와 right는 None으로 초기화
#
#     def __self__(self, value, left=None,right=None):
#
#         self.value = value
#
#         self.left = left
#
#         self.right = right
#
#
#
# # 배열 역직렬화 > 트리함수 선언
#
# def make_tree_by(lst, idx):
#
#     # 부모노드 None으로 초기화, 최초의 parent는 루트
#
#     # 이후의 parent들은 서브트리의 루트가 됨
#
#     parent = None
#
#     # idx < len(lst)의 의미는 인덱스 값이 아직 lst안을 가리킬 때를 의미
#
#     # 최초에는 0이 들어가고, 재귀하면서 점차 1, 2 와 3,4,5,6 ... 이 들어간다.
#
#     if idx < len(lst):
#
#
#
#         # 조건에 만족하면 배열의 idx위치의 값을 value에 저장
#
#         value = lst[idx]
#
#         # 만약 value 값이 없다면
#
#         if value is None:
#
#             #None을 반환하고 함수 종료
#
#             return None
#
#
#
#         # value값을 value로 하는 부모 노드 생성
#
#         parent = TreeNode(value)
#
#         # 부모 노드의 left와 right에 각각 현재 인덱스를 기준으로 자식 노드 값을 인자로 함수 재귀호출
#
#         parent.left = make_tree_by(lst, 2*idx+1)
#
#         parent.right = make_tree_by(lst, 2*idx+2)
#
#
#
#     # 함수의 반환값을 현재의 parent로 설정
#
#     # 재귀하여 반환된 값이 재귀함수의 parent 즉 서브트리의 루트이므로, 상위 트리의 자식노드로 연결됨
#
#     return parent