class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        count = 0
        max_count = 0
        for i,char in enumerate(s):
            if char in seen:
                old_index = seen[char]
                for key, val in list(seen.items()):
                    if val < old_index:
                        del seen[key]
                seen[char] = i
                count = i - old_index
            else:
                seen[char] = i
                count += 1
                if count > max_count:
                    max_count = count
        return max_count
