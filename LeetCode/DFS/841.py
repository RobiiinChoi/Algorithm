'''
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
When you visit a room, you may find a set of distinct keys in it.
Each key has a number on it, denoting which room it unlocks,
and you can take all of them with you to unlock the other rooms.
Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i,
return true if you can visit all the rooms, or false otherwise.

Input: rooms = [[1],[2],[3],[]]
Output: true

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
'''
from collections import deque
from typing import List

class Solution():
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([rooms[0]])
        visited = [0] # 정현님이 알려주셨다!
        while q:
            nodes = q.popleft()
            for node in nodes:
                if node not in visited:
                    visited.append(node)
                    q.append(rooms[node])
        return len(rooms)==len(visited)

rooms = [[1],[2],[3],[]]
s = Solution()
print(s.canVisitAllRooms(rooms))

