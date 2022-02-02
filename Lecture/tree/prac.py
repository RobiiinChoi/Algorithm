from collections import deque

from Lecture.tree.structures import TreeNode
# 9회 https://teamsparta.notion.site/9-1-44fae036478f44d1b274769e0d9cc94c
# 10회 https://teamsparta.notion.site/10-2-bfd3123f0dc44859ab9d3f618a314157

def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value is None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent

def sorted_array_to_bst(lst):
    if not lst:
        return None

    mid = len(lst) // 2

    node = TreeNode(lst[mid])
    node.left = sorted_array_to_bst(lst[:mid])
    node.right = sorted_array_to_bst(lst[mid + 1:])

    return node

def make_lst_by_bst(root, limit):
    if not root:
        return []

    lst = []
    q = deque([root])

    while q:
        if len(lst) > limit:
            break

        node = q.popleft()
        if node:
            lst.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            lst.append(None)

    return lst