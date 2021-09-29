class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = 0
        max_sum = nums[0]
        for num in nums:
            if running_sum < 0:
                running_sum = 0
            running_sum = running_sum + num
            if running_sum > max_sum:
                max_sum = running_sum
        return max_sum
