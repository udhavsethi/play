class Solution:
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     nums1[:] = nums1[:m]
    #     currIndex = 0
    #     j = 0
    #     while j < len(nums2):
    #         if (currIndex == len(nums1)) or (nums1[currIndex] > nums2[j]):
    #             nums1.insert(currIndex, nums2[j])
    #             j += 1
    #         currIndex += 1
​
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums_sol = []
        nums1[:] = nums1[:m]
        ind1 = 0
        ind2 = 0
        while ind1 < len(nums1) and ind2 < len(nums2):
            if nums1[ind1] <= nums2[ind2]:
                nums_sol.append(nums1[ind1])
                ind1 += 1
            else:
                nums_sol.append(nums2[ind2])
                ind2 += 1
        # append the rest of the array
        if ind2 < len(nums2):
            nums_sol[:] = nums_sol + nums2[ind2:]
        elif ind1 < len(nums1):
            nums_sol[:] = nums_sol + nums1[ind1:]
        
        nums1[:] = nums_sol
​
