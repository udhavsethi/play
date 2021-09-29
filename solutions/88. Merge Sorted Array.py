class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        currIndex = 0
        j = 0
        while j < len(nums2):
            if (currIndex == len(nums1)) or (nums1[currIndex] > nums2[j]):
                nums1.insert(currIndex, nums2[j])
                j += 1
            currIndex += 1
