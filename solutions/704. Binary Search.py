class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bin_search(nums, 0, len(nums)-1, target)
​
    def bin_search(self, nums: List[int], left: int, right: int, target: int):
        if left > right:
            return -1
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.bin_search(nums, left, mid-1, target)
        else:
            return self.bin_search(nums, mid+1, right, target)
