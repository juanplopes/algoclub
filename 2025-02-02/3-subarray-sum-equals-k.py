#https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums, k):
        count = {0: 1}
        answer = 0
        s = 0
        for x in nums:
            s += x
            answer += count.get(s - k, 0)
            count[s] = count.get(s, 0) + 1
        return answer