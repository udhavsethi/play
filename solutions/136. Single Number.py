class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] = 0
            else:
                seen[num] = 1
        return [k for k,v in seen.items() if v == 1][0]
                
