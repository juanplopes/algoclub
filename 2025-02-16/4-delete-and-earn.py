import collections, functools
class Solution:
    def deleteAndEarn(self, nums):      
        C = collections.Counter(nums)
        @functools.cache
        def solve(i):
            if i < 0: return 0
            return max(C[i] * i + solve(i - 2), solve(i-1))
        return solve(max(nums))
