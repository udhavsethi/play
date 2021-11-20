# review
# brute force - TLE
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                k = 0
                while i+k < len(nums1) and j+k < len(nums2) and nums1[i+k] == nums2[j+k]:
                    k += 1
                res = max(res,k)
        return res
