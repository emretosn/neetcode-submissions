import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        h = [-t for t in count.values()]
        heapq.heapify(h)

        time = 0
        q = deque()
        while h or q:
            time += 1

            if not h:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(h)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])
        return time