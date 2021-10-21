# review
# also: check time complexities in solutions
class Solution:
    
    def get_counts(self, st: str) -> dict:
        st_chars = {}
        for c in st:
            if c in st_chars:
                st_chars[c] += 1
            else:
                st_chars[c] = 1
        return st_chars
​
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len = len(s1)
        s2len = len(s2)
        if s1len > s2len:
            return False
​
        s1_chars = self.get_counts(s1)
​
        s2len = len(s2)
        s2_chars = None
        for curr in range(0, s2len-s1len+1):
            # print("curr ", curr)
            if s2_chars is not None:
                if s2[curr+s1len-1] in s2_chars:                    
                    s2_chars[s2[curr+s1len-1]] += 1
                else:
                    s2_chars[s2[curr+s1len-1]] = 1
                s2_chars[s2[curr-1]] -= 1
            else:
                s2_chars = self.get_counts(s2[curr:curr+s1len])
            # check
            if set([(k,v) for k,v in s1_chars.items() if v>0]) == set([(k,v) for k,v in s2_chars.items() if v>0]):
                    return True
        return False
​
'''
class Solution:
    
    def get_counts(self, s1: str) -> dict:
        s1_chars = {}
        for c in s1:
            if c in s1_chars:
                s1_chars[c] += 1
            else:
                s1_chars[c] = 1
        return s1_chars
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
