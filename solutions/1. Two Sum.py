# review
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in record:
                return [i, record[diff]]
            record[nums[i]] = i
​
    ### brute force
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     n = len(nums)
    #     for i in range(n):
    #         for j in range(n):
    #             if (i != j) and (nums[i] + nums[j] == target):
    #                 return [i, j]
