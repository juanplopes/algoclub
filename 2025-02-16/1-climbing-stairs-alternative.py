import functools
class Solution:
    @functools.cache
    def climbStairs(self, n):
        if n <= 1: return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)