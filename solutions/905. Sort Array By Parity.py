class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        even.extend(odd)
        return even
