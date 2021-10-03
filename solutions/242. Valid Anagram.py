class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        for tchar in t:
            if tchar in count:
                count[tchar] -= 1
                if count[tchar] < 0:
                    return False
            else:
                return False
        return True
​
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(s) == sorted(t)
