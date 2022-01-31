# Given the head of a linked list, return the list after sorting it in ascending order.
'''
1. 아이디어 : 정민님 제공
리스트로 바꿔서 풀고 다시 연결해준다

2. 시간복잡도

3. 자료구조 : 리스트, 연결리스트, 정렬
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 리스트가 빈 경우 리턴 None (예외처리)
        if not head:
            return None
        # 빈리스트 변수
        array = []
        # head가 있으면 (리스트가 있으면)
        while head:
            # head값 이동하면서 빈 배열에 값 어펜드
            array.append(head.val)
            head=head.next
        # 값 다 옮긴 뒤 오름차순 정렬
        array.sort()
        # 가장 첫번째 배열을 헤드로 정하고 포인터랑 같이 초기화
        newHead = point = ListNode(0)
        # 배열 돌리면서 포인터 변수 이어나감
        for i in range(len(array)):
            point.next = ListNode(array[i])
            point = point.next
            print(point.val)
        return newHead.next

n = ListNode(4)
n.add(ListNode(2))
n.add(ListNode(1))
n.add(ListNode(3))
s = Solution()
s.sortList(n)


