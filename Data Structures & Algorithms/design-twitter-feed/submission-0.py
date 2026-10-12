import heapq

class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId}

        for u in users:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                counter, tweetId = self.tweets[u][idx]
                heapq.heappush(heap, (-counter, tweetId, u, idx))
        feed = []
        while heap and len(feed) < 10:
            _, tweetId, u, idx = heapq.heappop(heap)
            feed.append(tweetId)
            if idx > 0:
                counter, nextId = self.tweets[u][idx - 1]
                heapq.heappush(heap, (-counter, nextId, u, idx - 1))
        return feed



    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].discard(followeeId)