class Solution:
    def rob_linear(self, nums, mem):
        if repr(nums) in mem:
            return mem[repr(nums)]
        n = len(nums)
        if n == 0:
            mem[repr(nums)] = 0
        elif n == 1:
            mem[repr(nums)] = nums[0]
        elif n == 2:
            mem[repr(nums)] = max(nums[0], nums[1])
        else:
            mem[repr(nums)] = max(
                nums[n-1] + self.rob_linear(nums[:n-2], mem),
                self.rob_linear(nums[:n-1], mem)
            )
        return mem[repr(nums)]
​
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        mem = {}
        return max(
            nums[n-1] + self.rob_linear(nums[1:n-2], mem),
            self.rob_linear(nums[:n-1], mem)
        )
​
#     # simple recursion - TLE
#     def rob_linear(self, nums):
#         n = len(nums)
#         if n == 0:
#             return 0
#         if n == 1:
#             return nums[0]
#         elif n == 2:
#             return max(nums[0], nums[1])
#         return max((nums[n-1] + self.rob_linear(nums[:n-2])), self.rob_linear(nums[:n-1]))
    
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         return max((nums[n-1] + self.rob_linear(nums[1:n-2])), self.rob_linear(nums[:n-1]))
