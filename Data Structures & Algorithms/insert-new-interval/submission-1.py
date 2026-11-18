class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = [] 
        for i, a in enumerate(intervals):
            if a[1] < newInterval[0]:
                ret.append(a)
            elif a[0] <= newInterval[1]:
                newInterval = [min(a[0], newInterval[0]), max(a[1], newInterval[1])]
            else:
                ret.append(newInterval)
                ret.extend(intervals[i:])
                return ret
        else:
            ret.append(newInterval)
            return ret