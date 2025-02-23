class Solution:
    def maximalSquare(self, matrix):
        @functools.cache
        def solve(i, j):
            if not 0 <= i < len(matrix) or not 0 <= j < len(matrix[i]): return 0
            if matrix[i][j] == "0": return 0
            return 1+min(solve(i-1, j-1), solve(i-1, j), solve(i, j-1))
        return max(solve(i, j)**2 for i in range(len(matrix)) for j in range(len(matrix[i])))