from collections import defaultdict, deque

class Twitter:

    def __init__(self):
        self.users = defaultdict(deque)
        self.following = defaultdict(set)
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t += 1
        self.users[userId].append((-self.t, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = list(self.following[userId]) + [userId]
        feed = []

        for user in users:
            feed += self.users[user]

        heapq.heapify(feed)
        print(feed)

        ids = []
        i = 0
        while feed and i < 10:
            x = heapq.heappop(feed)
            t, pid = x
            ids.append(pid)    
            i += 1

        print(ids)
        return ids

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId] and followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId] and followerId != followeeId:
            self.following[followerId].remove(followeeId)
