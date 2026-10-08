class Solution:
    def trap(self, height: List[int]) -> int:
        ll, lr = [], []
        hl, hr = 0, 0

        for h in height:
            if h > hl:
                hl = h
            ll.append(hl)

        for h in reversed(height):
            if h > hr:
                hr = h
            lr.append(hr)
        lr.reverse()

        water = 0
        for i, h in enumerate(height):
            water += min(ll[i], lr[i]) - h
        return water