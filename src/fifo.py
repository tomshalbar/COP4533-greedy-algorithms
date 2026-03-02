from collections import deque


class Fifo:

    def __init__(self, k: int):
        """params: k- size of cache"""
        self.capacity = k
        self.cache = deque()

    def request(self, r: int) -> str:
        """
        params: r- val requested
        returns: 'miss' for miss, 'hit' for hit
        """
        if r in self.cache:
            return "hit"
        else:
            self.update(r)
            return "miss"

    def update(self, r):
        if len(self.cache) < self.capacity:
            self.cache.append(r)
        else:
            self.cache.popleft()
            self.cache.append(r)
