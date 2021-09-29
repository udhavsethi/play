class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k > 0 and n > 1:
            nums[:] = nums[-k:] + nums[:(n-k)]
​
        # review
        # don't know why doesn't work:
        # n = len(nums)
        # nums[:] = [nums[(i+k+1)%n] for i in range(n)]
