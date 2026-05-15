class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = {}
        max_len = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in count and count[ch] >= left:
                left = count[ch] + 1

            count[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len
        