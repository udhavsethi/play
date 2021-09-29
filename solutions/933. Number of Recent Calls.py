class RecentCounter:
​
    def __init__(self):
        self.cutoff = 0
        self.requests = []
​
    def ping(self, t: int) -> int:
        self.requests.append(t)
        rlen = len(self.requests)
        for i in range(self.cutoff, rlen) :
            if t - self.requests[i] <= 3000:
                self.cutoff = i
                return rlen - i
        return rlen
​
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
​
### Alternate solution ###
​
# class RecentCounter:
​
#     def __init__(self):
#         self.slide_window = deque()
​
#     def ping(self, t: int) -> int:
#         # step 1). append the current call
#         self.slide_window.append(t)
​
#         # step 2). invalidate the outdated pings
#         while self.slide_window[0] < t - 3000:
#             self.slide_window.popleft()
​
#         return len(self.slide_window)
