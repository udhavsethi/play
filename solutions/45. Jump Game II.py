class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dist = [0] * n
        dist[n-1] = 0
        cur = n-2
​
        while cur >= 0:
            steps = nums[cur]
            # store eligible distances
            # inf is needed to handle 0s since they cause len(d) == 0
            d = [float(inf)]
            rev_idx = min(cur+steps, n-1)
            while rev_idx > cur:
                d.append(1 + dist[rev_idx])
                rev_idx -= 1
            dist[cur] = min(d)
            cur -= 1
        return dist[0]
            
