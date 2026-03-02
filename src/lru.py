class Lru:
    def __init__(self, k: int):
        """params: k- size of cache"""
        self.capacity = k
        self.cache = list()

    def request(self, r: int) -> str:
        """
        params: r- val requested
        returns: 'miss' for miss, 'hit' for hit
        """
        ret = "hit" if r in self.cache else "miss"
        self.update(r)
        return ret

    def update(self, r):
        if r in self.cache:
            self.cache.remove(r)
            self.cache.append(r)
        else:
            if len(self.cache) < self.capacity:
                self.cache.append(r)
            else:
                self.cache.pop(0)
                self.cache.append(r)
