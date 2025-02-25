class Solution:
    @functools.cache
    def uniquePaths(self, m, n):
        if m == 1 or n == 1: return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        