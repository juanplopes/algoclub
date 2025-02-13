import functools
class Solution:
    def rob(self, nums):
        @functools.cache
        def solve(i):
            if i == 0: return 0
            if i == 1: return nums[0]
            return max(nums[i-1] + solve(i-2), solve(i-1))
        return solve(len(nums))