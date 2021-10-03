class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_len = 0
        start, running_len, max_len = 0, 0, 0
        for curr,char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
                seen[char] = curr
                running_len = curr - start + 1
            else:
                seen[char] = curr
                running_len += 1
                if running_len > max_len:
                    max_len = running_len
        return max_len
    
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     seen = {}
    #     count = 0
    #     max_count = 0
    #     for i,char in enumerate(s):
    #         if char in seen:
    #             old_index = seen[char]
    #             for key, val in list(seen.items()):
    #                 if val < old_index:
    #                     del seen[key]
    #             seen[char] = i
    #             count = i - old_index
    #         else:
    #             seen[char] = i
    #             count += 1
