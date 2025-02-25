class Solution:
    def maximalSquare(self, matrix):
        @functools.cache
        def solve(i, j):
            if i < 0 or j < 0 or matrix[i][j] == "0": return 0
            return 1+min(solve(i-1, j-1), solve(i-1, j), solve(i, j-1))
        return max(solve(i, j)**2 for i in range(len(matrix)) for j in range(len(matrix[i])))