# simple recursion - TLE
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == "" or text2 == "":
            return 0
        if text1 == text2:
            return len(text1)
        if text1[0] == text2[0]:
            return 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
        else:
            return max(self.longestCommonSubsequence(text1[1:], text2),
                      self.longestCommonSubsequence(text1, text2[1:]))
