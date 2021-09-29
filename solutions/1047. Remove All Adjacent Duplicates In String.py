# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         i = 0
#         while i+1 < len(s):
#             if s[i] == s[i+1]:
#                 left = i if i>=0 else i+2
#                 right = i+2 if i<(len(s)-2) else i
#                 s = s[:left] + s[right:] if left != right else s[:left]
#                 # move to previous index as it may now contribute toward duplicates
#                 i = i-2 if i-1 >= 0 else i-1
#             i += 1
#         return s
​
##############
​
# review
# alternate solution - using a stack
​
from collections import deque
​
class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0
        stack = deque([0])
        for char in s:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        stack.popleft()     # remove placeholder
        return ("").join(stack)
​
