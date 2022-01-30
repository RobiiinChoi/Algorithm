# Given a list of non-negative integers nums, arrange them
# such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string
# instead of an integer.
# leetcode 179 (largest number)
'''
Input: nums = [10,2]
Output: "210"

Input: nums = [3,30,34,5,9]
Output: "9534330"

1. 아이디어
- 삽입 정렬로 풀기
- 함수 하나를 추가로 설정하여 값을 인덱스
2. 시간복잡도
3. 자료구조 - 리스트
'''
from typing import List


class Solution:
    def largestNumber(self, nums):
        for i in range(len(nums)):
            pos, cur = i, nums[i]
            while pos > 0 and not self.compare(nums[pos-1],cur):
                nums[pos]=nums[pos-1]
                pos-=1
            nums[pos]=cur
        return str(int("".join(map(str, nums))))

    def compare(self, n1, n2):
        # print(str(n1)+str(n2))
        # print(str(n2)+str(n1))
        return str(n1) + str(n2) > str(n2) + str(n1)

s = Solution()
print(s.largestNumber([3,30,34,5,9]))

# print(s.compare(10, 2))