class Solution:
    def countPaths(self, grid):
        @functools.cache
        def solve(i, j, prev=float('-inf')):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[i]) or grid[i][j] <= prev: return 0
            v = grid[i][j]
            return (1+solve(i-1, j, v)+solve(i, j-1, v)+solve(i+1, j, v)+solve(i, j+1, v))%1000000007
        return sum(solve(i, j) for i in range(len(grid)) for j in range(len(grid[i])))%1000000007
