class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if s.isdigit():
                return [s]
        if len(s) == 1:
            return [s.lower(), s.upper()]
        # len(s) > 1
        res = []
        if s[0].isdigit():
            for substr in self.letterCasePermutation(s[1:]):
                res.append(s[0] + substr)
        else:
            for substr in self.letterCasePermutation(s[1:]):
                res.append(s[0].lower() + substr)
                res.append(s[0].upper() + substr)
        return res
