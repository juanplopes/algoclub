#https://leetcode.com/problems/find-pivot-index/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        s2 = 0
        for i, x in enumerate(nums):
            if s2 == s - s2 - x: return i
            s2 += x
        return -1