class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
​
        s = s.lower()
        half_len_s = int(len(s)/2)
​
        first = s[:half_len_s]
        second = s[half_len_s:]
​
        first_vowels = 0
        second_vowels = 0
​
        for char in first:
            if char in vowels:
                first_vowels += 1
        for char in second:
            if char in vowels:
                second_vowels += 1
        
        return first_vowels == second_vowels
