class Twitter:

    def __init__(self):
        self.time = 0
        self.maxFeed = 10
        self.tweets = defaultdict(list) # [userId -> [(time, tid)]]
        self.followings = defaultdict(set) # [userId -> {followeeId}]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        heap = []

        for person in {userId} | self.followings[userId]:
            if self.tweets[person]:
                i = len(self.tweets[person]) - 1
                t, tid = self.tweets[person][i]
                heapq.heappush(heap, (-t, tid, person, i-1))

        feed = []
        while heap and len(feed) < self.maxFeed:
            _, tid, person, i = heapq.heappop(heap)
            feed.append(tid)

            if i >= 0:
                t, nxt = self.tweets[person][i] # keep the latest person post
                heapq.heappush(heap, (-t, nxt, person, i - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].discard(followeeId)
        
