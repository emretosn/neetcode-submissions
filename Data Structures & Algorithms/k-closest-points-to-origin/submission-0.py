import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i, p in enumerate(points):
            dist = -math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(distances, (dist, i))
            if len(distances) > k:
                heapq.heappop(distances)
        
        return [points[p[1]] for p in distances]