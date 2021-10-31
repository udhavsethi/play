class Solution:
    # review
    # recursive solution with DP
    def robAt(self, nums, i, mem):
        if i < 0:
            return 0
        if i in mem:
            return mem[i]
        mem[i] = max(self.robAt(nums, i-2, mem) + nums[i], self.robAt(nums, i-1, mem))
        return mem[i]
​
    def rob(self, nums: List[int]) -> int:
        return self.robAt(nums, len(nums)-1, {})
    
    # simple recursive solution - TLE
#     def robAt(self, nums, i):
#         if i < 0:
#             return 0
#         return max(self.robAt(nums, i-2) + nums[i], self.robAt(nums, i-1))
​
#     def rob(self, nums: List[int]) -> int:
#         return self.robAt(nums, len(nums)-1)
