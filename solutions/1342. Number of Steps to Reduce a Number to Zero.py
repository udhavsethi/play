class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
        if num == 1:
            # base case
            return 1
        elif num % 2 == 0:
            # even number
            return self.numberOfSteps(num/2) + 1
        else:
            # odd number
            return self.numberOfSteps(num-1) + 1
        
