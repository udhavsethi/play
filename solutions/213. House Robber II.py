class Solution:
    
    # simple recursion - TLE
    def rob_linear(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        return max((nums[n-1] + self.rob_linear(nums[:n-2])), self.rob_linear(nums[:n-1]))
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return max((nums[n-1] + self.rob_linear(nums[1:n-2])), self.rob_linear(nums[:n-1]))
