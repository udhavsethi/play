class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0
        while i+1 < len(s):
            if s[i] == s[i+1]:
                left = i if i>=0 else i+2
                right = i+2 if i<(len(s)-2) else i
                s = s[:left] + s[right:] if left != right else s[:left]
                i = -1
            i += 1
        return s
