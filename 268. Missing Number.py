"""05-28-2022 Leetcode 268. Missing Number"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return ((len(nums) * (len(nums) + 1)) // 2) - sum(nums)
