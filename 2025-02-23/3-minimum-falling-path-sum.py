class Solution:
    def minFallingPathSum(self, matrix):
        @functools.cache
        def solve(i, j):
            if i == len(matrix): return 0
            if not (0 <= j < len(matrix[i])): return float('+inf')
            return matrix[i][j] + min(solve(i+1, j-1), solve(i+1, j), solve(i+1, j+1))
        return min(solve(0, j) for j in range(len(matrix[0])))
        