from collections import deque

from Lecture.tree.prac import make_tree_by


# 이진 트리의 최대 깊이
def test_max_depth(lst):
    # 루트는 트리 만드는 노드(리스트, 0)
    root = make_tree_by(lst, 0)
    # 루트노드가 없으면 0 리턴
    if not root:
        return 0

    # 루트노드를 담은 큐 생성, 깊이 0 초기화
    q = deque([root])
    depth = 0

    # 큐가 있으면 뎁스 1 증가
    while q:
        depth += 1
        # 레인지 돌면서 팝한 노드를 cur에 담는다
        for _ in range(len(q)):
            cur = q.popleft()
            # 현재 노드의 왼쪽, 오른쪽이 있으면 큐에 어펜드 하고
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    # 뎁스를 리턴
    return depth


assert test_max_depth(lst=[]) == 0
assert test_max_depth(lst=[3, 9, 20, None, None, 15, 7]) == 3