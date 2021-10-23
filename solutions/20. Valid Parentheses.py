class Solution:
    
    oppositeof = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
​
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if len(stack) > 0 and char in self.oppositeof and stack[-1] == self.oppositeof[char]:
                stack.pop()
            else:
                stack.append(char)
        print(stack)
        return True if (len(stack) == 0) else False
​
