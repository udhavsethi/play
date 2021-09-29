class Solution:
​
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == 0:
                nums[:] = nums[:i] + nums[i+1:] + [0]
            i -= 1
​
#     # slow solution
#     def moveToBack(self, nums: List[int], index, length):
#         while (index+1) < length:
#             if nums[index+1] != 0:
#                 nums[index], nums[index+1] = nums[index+1], nums[index]
#             index += 1
#         return nums
        
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         right = n-2
#         while right >= 0:
#             if nums[right] == 0:
#                 nums = self.moveToBack(nums, right, n)
#             right = right - 1
