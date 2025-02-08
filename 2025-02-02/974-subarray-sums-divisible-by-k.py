#https://leetcode.com/problems/subarray-sums-divisible-by-k/
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = [1] + k * [0]
        answer = 0
        s = 0
        for x in nums:
            s += x
            answer += count[(s - k) % k]
            count[s % k] += 1
        return answer