#https://leetcode.com/problems/range-sum-query-2d-immutable/
class NumMatrix:
    def __init__(self, matrix):
        self.T = [[0] * (len(matrix[0])+1) for i in range(len(matrix)+1)]
        for i in range(1, len(self.T)):
            for j in range(1, len(self.T[i])):
                self.T[i][j] = matrix[i-1][j-1] + self.T[i-1][j] + self.T[i][j-1] - self.T[i-1][j-1]
                
    def sumRegion(self, row1, col1, row2, col2):
        return self.T[row2+1][col2+1] - self.T[row2+1][col1] - self.T[row1][col2+1] + self.T[row1][col1] 