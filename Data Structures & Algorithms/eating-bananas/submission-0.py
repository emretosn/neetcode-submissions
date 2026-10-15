import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ret = r

        while r >= l:
            k = l + (r - l) // 2

            time = 0
            for p in piles:
                time += math.ceil(p/k)
            
            if time <= h:
                ret = k
                r = k - 1
            else:
                l = k + 1

        return ret