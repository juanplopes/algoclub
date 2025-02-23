class Solution:
    @functools.cache
    def uniquePaths(self, m, n):
        if m <= 0 or n <= 0: return 0
        if m == 1 and n == 1: return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        