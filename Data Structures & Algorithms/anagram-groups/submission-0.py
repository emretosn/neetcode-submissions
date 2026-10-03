class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sstrs = {}
        for s in strs:
            ssort = "".join(sorted(s))
            if ssort not in sstrs:
                sstrs[ssort] = []
            sstrs[ssort].append(s)
        return [v for _, v in sstrs.items()]
