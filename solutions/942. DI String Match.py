class Solution:
    
    def invalid(self, lst):
        # last number negative or duplicates in lst
        if len(lst) != len(set(lst)) or lst[-1] < 0:
            return True
        return False
        
    def diStringMatch(self, s: str) -> List[int]:
        perm = [0]
        for i, char in enumerate(s):
            if char == 'I':
                perm.append(i+1)
                while self.invalid(perm):
                    perm[-1] += 1
            elif char == 'D':
                perm.append(perm[i]-1)
                j=0
                while self.invalid(perm):
                    perm[j-1] += 1
                    j -= 1
        return perm
​
    '''
    Optimal solution
    
    class Solution(object):
    def diStringMatch(self, S):
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1
​
        return ans + [lo]
    '''
