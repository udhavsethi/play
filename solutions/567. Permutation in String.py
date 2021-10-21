class Solution:
    
    def get_counts(self, s1: str) -> dict:
        s1_chars = {}
        for c in s1:
            if c in s1_chars:
                s1_chars[c] += 1
            else:
                s1_chars[c] = 1
        return s1_chars
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # dict containing all the chars in s1 and their count
        s1_chars = self.get_counts(s1)
        s1len = len(s1)
        s2len = len(s2)
        lastnomatch = -1
        curr = 0
​
        while curr < s2len:
            char = s2[curr]
            if char in s1_chars:
                # print("curr, char, s1_chars", curr, char, s1_chars)
                if s1_chars[char] > 0:
                    s1_chars[char] -= 1
                    # check here
                    if (curr - lastnomatch) == s1len:
                        # print("curr, lastnomatch, s2[lastnomatch:curr]: ", curr, lastnomatch, s2[lastnomatch:curr])
                        return True
                    curr += 1
                else:
                    # restart counting
                    lastnomatch += 1
                    curr = lastnomatch+1
                    s1_chars = self.get_counts(s1)
            else:
                lastnomatch = curr
                curr += 1
                s1_chars = self.get_counts(s1)
        return False
