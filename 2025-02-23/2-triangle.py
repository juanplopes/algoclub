class Solution:
    def minimumTotal(self, triangle):
        @functools.cache
        def solve(i, j):
            if i == len(triangle): return 0
            return triangle[i][j] + min(solve(i+1, j), solve(i+1, j+1))
        return solve(0, 0)
        