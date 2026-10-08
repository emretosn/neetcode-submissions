class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        strt, count = 0, 0
        for i, c in enumerate(s):
            if c in h:
                strt = max(strt, h[c] + 1)
            h[c] = i
            count = max(count, i + 1 - strt)
        return count