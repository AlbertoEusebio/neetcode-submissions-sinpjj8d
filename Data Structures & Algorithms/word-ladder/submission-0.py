from collections import deque
from heapq import heapify, heappush, heappop

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def is_child(w1, w2):
            c = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    if c == 1:
                        return False
                    c += 1
            return True

        que = deque([(beginWord, 1)])
        visited = set()

        while que:
            z, k = que.popleft()

            print(k, z)

            if z == endWord:
                return k

            for w in wordList:
                if w not in visited and is_child(z, w):
                    visited.add(w)
                    que.append((w, k+1))

        return 0