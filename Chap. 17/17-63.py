# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
'''
Input = [2, 0, 2, 1, 1, 0]
Output = [0, 0, 1, 1, 2, 2]

Input = [2, 0, 1]
Output = [0, 1, 2]

1. 아이디어
- 빈 딕셔너리로 키-밸류로(컬러-카운트) 구현
- for문에서 키값이 작은 순으로 재출력
2. 시간복잡도 - n^2
3. 자료구조 : 리스트
'''
from collections import defaultdict
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 빈 딕셔너리에 키값으로 color - count 식으로 연결
        counts = defaultdict(int)
        # 해당 색깔이 입력값에 있으면 카운트 수 1개씩 올림
        for num in nums:
            counts[num]+=1
        # 배열 재배치 할 인덱스 변수 생성
        idx = 0
        # 컬러가 3개이므로 3번 돌리고, 각 컬러별 색깔을 오름차순이므로 인덱스 앞부분 부터 대입한다.
        for k in range(3):
            for m in range(counts[k]):
                nums[idx] = k
                idx += 1

s = Solution()
print(s.sortColors([2, 0, 2, 1, 1, 0]))
