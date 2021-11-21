# review
​
# bottom up DP - O(mn) time
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        mem = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if text1[i] == text2[j]:
                    mem[i][j] = 1 + mem[i+1][j+1]
                else:
                    mem[i][j] = max(mem[i+1][j], mem[i][j+1])
        return max(max(row) for row in mem)
​
# # DP - memoization - O(mn) time
# class Solution:
#     def longestCommonSubsequenceWithMem(self, text1, text2, mem):
#         if text1 == "" or text2 == "":
#             return 0
#         if text1 == text2:
#             return len(text1)
#         if (text1, text2) in mem:
#             return mem[(text1, text2)]
#         if (text2, text1) in mem:
#             return mem[(text2, text1)]
#         if text1[0] == text2[0]:
#             mem[(text1, text2)] = 1 + self.longestCommonSubsequenceWithMem(text1[1:], text2[1:], mem)
#             return mem[(text1, text2)]
#         else:
#             mem[(text1, text2)] = max(self.longestCommonSubsequenceWithMem(text1[1:], text2, mem),
#                                       self.longestCommonSubsequenceWithMem(text1, text2[1:], mem))
#             return mem[(text1, text2)]
​
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         mem = {}
#         return self.longestCommonSubsequenceWithMem(text1, text2, mem)
        
​
# # simple recursion - TLE
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         if text1 == "" or text2 == "":
#             return 0
#         if text1 == text2:
#             return len(text1)
#         if text1[0] == text2[0]:
#             return 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
#         else:
#             return max(self.longestCommonSubsequence(text1[1:], text2),
#                       self.longestCommonSubsequence(text1, text2[1:]))
