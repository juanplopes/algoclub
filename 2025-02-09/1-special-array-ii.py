#https://leetcode.com/problems/special-array-ii/
class Solution:
    def isArraySpecial(self, nums, queries):
        T = [0] * len(nums)
        for i in range(1, len(nums)):
            T[i] = T[i-1] + (nums[i]%2 == nums[i-1]%2)
        return [T[b] - T[a] == 0 for a, b in queries]