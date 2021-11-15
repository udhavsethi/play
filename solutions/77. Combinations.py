# review
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == k:
            return [[x for x in range(1,n+1)]]
        if k == 1:
            return [[x] for x in range(1,n+1)]
        # (n-1)C(k-1)
        res = self.combine(n-1, k-1)
        for lst in res:
            lst.append(n)
        # (n-1)C(k)
        res.extend(self.combine(n-1, k))
        return res
