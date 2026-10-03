class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s)) + '@'
            ret += s
        return ret

    def decode(self, s: str) -> List[str]:
        num = ""
        ret = []
        i = 0
        while i < len(s):
            if s[i] == '@':
                n = int(num)
                ret.append(s[i+1:i+n+1])
                i = i+n+1
                num = ""
            else:
                num += s[i]
                i += 1
        return ret