'''

최대 서브 배열
합이 최대가 되는 연속 서브 배열을 찾아 합을 리턴하라

'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.maxSubArray(nums))
