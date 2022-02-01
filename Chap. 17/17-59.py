'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if result and i[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result += i,
        return result
