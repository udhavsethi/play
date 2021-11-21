# review
​
import math
class Solution:
    def longestPalindrome(self, s: str) -> str:
        palins = []
        for idx in range(2*len(s)):
            i = idx/2
            j = 0
            left, right = math.floor(i-j), math.ceil(i+j)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palins.append(s[left:right+1])
                j += 1
                left, right = math.floor(i-j), math.ceil(i+j)
        palins.sort(key=lambda x: len(x), reverse=True)
        return palins[0]
​
