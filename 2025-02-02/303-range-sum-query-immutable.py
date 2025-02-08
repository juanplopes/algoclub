#https://leetcode.com/problems/range-sum-query-immutable/
class NumArray:
    def __init__(self, nums):
        self.nums = [0] + nums
        for i in range(1, len(self.nums)):
            self.nums[i] += self.nums[i - 1]
        
    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1] - self.nums[left]