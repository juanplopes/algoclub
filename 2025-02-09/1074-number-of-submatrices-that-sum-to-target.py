# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        answer = 0
        for i in range(len(matrix)):
            nums = [0] * len(matrix[i])
            for j in range(i, len(matrix)):
                for k in range(len(nums)):
                    nums[k] += matrix[j][k]
                count = {0: 1}
                s = 0
                for x in nums:
                    s += x
                    answer += count.get(s - target, 0)
                    count[s] = count.get(s, 0) + 1
        return answer
        