class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1.sort()
        nums2.sort()
        cur1, cur2 = 0, 0
        while cur1 < len(nums1) and cur2 < len(nums2):
            if nums1[cur1] == nums2[cur2]:
                result.append(nums1[cur1])
                cur1 += 1
                cur2 += 1
            elif nums1[cur1] > nums2[cur2]:
                cur2 += 1
            else:
                cur1 += 1
        return result
