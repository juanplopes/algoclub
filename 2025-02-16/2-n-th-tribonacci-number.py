import functools
class Solution:
    @functools.cache
    def tribonacci(self, n):
        if n <= 2: return (0,1,1)[n]
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)