class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        res = -1
        for i, char in enumerate(s):
            if char not in seen:
                seen[char] = i
            else:
                seen[char] = -2
        
        for key, val in seen.items():
            if val != -2:
                if res == -1:
                    res = val
                else:
                    res = min(res, val)
        return res
    
    
    
    
    # def firstUniqChar(self, s: str) -> int:
    #     curr, res = len(s)-1, -1
    #     seen = set()
    #     while curr >=0:
    #         if not s[curr] in seen:
    #             seen.add(s[curr])
    #             res = curr
    #         else:
    #             pass
    #         curr -= 1
    #     return res
                
