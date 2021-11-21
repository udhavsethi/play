# review
​
import heapq
​
# Time complexity: O(nlogk), Space: log(k)
# Push top k elements, then push only if val>top
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for i in range(k):
            heappush(h, nums[i])
        for j in range(k, len(nums)):
            if nums[j] > h[0]:
                heappop(h)
                heappush(h, nums[j])
        return h[0]
​
# Time complexity: O(nlogn) - push one by one and pop one by one
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heapq.heapify(nums)
#         return heapq.nlargest(k, nums)[-1]
        
