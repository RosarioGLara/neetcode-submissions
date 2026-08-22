class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i, j = 0, 0
        max_len = 1
        while j < len(s) - 1:
            k = j + 1
            if s[k] in s[i:j+1]:
                i += s[i:j+1].index(s[k]) + 1
                j += 1
            else:
                j += 1
                max_len = max(j - i + 1, max_len)
        return max_len