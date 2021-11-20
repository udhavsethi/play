# review
# see solution for explanation
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        mem = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if nums1[i] == nums2[j]:
                    mem[i][j] = 1 + mem[i+1][j+1]
        return max(max(row) for row in mem)
​
​
# brute force - TLE
# class Solution:
#     def findLength(self, nums1: List[int], nums2: List[int]) -> int:
#         res = 0
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 k = 0
#                 while i+k < len(nums1) and j+k < len(nums2) and nums1[i+k] == nums2[j+k]:
#                     k += 1
#                 res = max(res,k)
#         return res
