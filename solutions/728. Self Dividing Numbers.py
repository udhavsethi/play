class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        if left <= 10:
            res = list(range(left,10))
            left = 11
        for num in range(left,right+1):
            quotient = num
            while quotient != 0:
                digit = quotient % 10
                if digit == 0:
                    break
                if not num % digit == 0:    # num not divisible by digit
                    break
                quotient = quotient // 10
            if quotient == 0:  # num is divisible by all digits
                res.append(num)
        return res
​
