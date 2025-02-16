import collections
class Solution:
    def deleteAndEarn(self, nums):      
        C = collections.Counter(nums)
        a, b = 0, C[0]
        for i in range(1, max(nums)+1):
            a, b = b, max(C[i] * i + a, b)
        return b

