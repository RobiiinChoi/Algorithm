# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
# Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
# Example 1: Input // jewels = "aA", stones = "aAAbbbb", Output // 3
# Example 2: Input // jewels = "z", stones = "ZZ", Output // 0

class Solution:
    # 리스트로 풀 때
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        # j = list(jewels)
        # print(j)
        # s = list(stones)
        # print(s)

        # for i in jewels: #range : 수의 범위
        #     for j in stones:
        #         if(i == j):
        #             count+=1
        #         else:
        #             pass

        print(count)
        return count

        def Search(S, J):
            count = 0
            for jewel in J:
                count += S.count(jewel)
            return count

if __name__ == "__main__":
    s = Solution()
    s.numJewelsInStones('aA', 'aAAbbbb')
