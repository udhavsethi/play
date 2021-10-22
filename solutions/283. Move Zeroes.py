# review
class Solution:
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        toFill = 0
        n = len(nums)
        while curr < n:
            if nums[curr] != 0 and curr != toFill:
                nums[toFill] = nums[curr]
                nums[curr] = 0
                toFill += 1
            if nums[toFill] != 0:
                toFill += 1
            curr += 1
​
​
############################################################
#     # non optimal solution
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i = len(nums) - 1
#         while i >= 0:
#             if nums[i] == 0:
#                 nums[:] = nums[:i] + nums[i+1:] + [0]
#             i -= 1
​
############################################################
​
#     # time limit exceeded
#     def moveToBack(self, nums: List[int], index, length):
#         while (index+1) < length:
#             if nums[index+1] != 0:
#                 nums[index], nums[index+1] = nums[index+1], nums[index]
#             index += 1
#         return nums
        
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
