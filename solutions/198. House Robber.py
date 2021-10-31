class Solution:
    # simple recursive solution - TLE
    def robAt(self, nums, i):
        if i < 0:
            return 0
        return max(self.robAt(nums, i-2) + nums[i], self.robAt(nums, i-1))
​
    def rob(self, nums: List[int]) -> int:
        return self.robAt(nums, len(nums)-1)
