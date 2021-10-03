class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for r in ransomNote:
            if r not in count:
                count[r] = 1
            else:
                count[r] += 1
        for m in magazine:
            if m in count:
                count[m] -= 1
        return all(x <= 0 for x in count.values())
