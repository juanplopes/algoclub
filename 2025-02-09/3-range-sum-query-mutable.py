#https://leetcode.com/problems/range-sum-query-mutable/submissions/1536111309/
class FenwickTree:
    def __init__(self, size):
        self.data = [0] * size 

    def add(self, index, value):
        while index <= len(self.data):
            self.data[index - 1] += value
            index += index & -index

    def query(self, index):
        value = 0
        while index > 0:
            value += self.data[index - 1]
            index -= index & -index
        return value

class NumArray:
    def __init__(self, nums):
        self.tree = FenwickTree(len(nums)+1)
        for i, num in enumerate(nums):
            self.tree.add(i+1, num)

    def update(self, index, val):
        self.tree.add(index+1, val - self.sumRange(index, index))

    def sumRange(self, left, right):
        return self.tree.query(right+1) - self.tree.query(left)