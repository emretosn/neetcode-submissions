class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ret = s[0]

        for i in range(n):
            tmp = s[i]
            for j in range(1, min(i, n-1-i) + 1):
                if s[i-j] == s[i+j]:
                    tmp = s[i-j] + tmp + s[i+j]
                    if len(tmp) > len(ret):
                        ret = tmp
                else:
                    break

        for i in range(n - 1):
            tmp = ''
            for j in range(min(i, n-2-i) + 1):
                if s[i-j] == s[i+1+j]:
                    tmp = s[i-j] + tmp + s[i+1+j]
                    if len(tmp) > len(ret):
                        ret = tmp
                else:
                    break

        return ret