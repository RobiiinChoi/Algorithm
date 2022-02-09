import collections

# 런타임 에러
# class Solution:
#   memo = {1: 1, 2: 2}
#     def climbStairs(self, n: int) -> int:
#
#         if n in self.memo:
#             return self.memo[n]
#
#         self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
#         return self.memo[n]
# s = Solution()
# print(s.climbStairs(5))


class Solution:
    memo = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.memo[n]:
            return self.memo[n]
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]

