class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for num in nums:
            perm = self.permute([x for x in nums if x != num])
            perm = [[num] + lst for lst in perm]
            res.extend(perm)
        return res
