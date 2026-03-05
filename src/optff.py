class OPTFF:
    def __init__(self, k: int, requests: list[int]):
        """
            Creates a cache (set) and stores the capacity of it (k)
            Stores a list containing all the requests (i.e. the algorithm knows future requests to make its optimal selection)
        """
        self.capacity: int = k
        self.requests: list[int] = requests
        self.cache: set[int] = set()

    def remove_request_from_cache(self) -> None:
        """
            When there is a cache miss, removes the element in the cache that occurs farthest in the future or not at all
        """
        found: set[int] = set()

        for request in self.requests:
            if request in self.cache:
                found.add(request)

                if len(found) == self.capacity:
                    # The last request found that filled the set is the one that occurs farthest in the future
                    self.cache.remove(request)
                    return

        """
            If the `found` set is not full, it means that a request in the cache does not happen again
                1. Perform a set difference to get the requests in the cache that are not in the `found` set
                2. Get an arbitrary element in this set difference by creating an iterator for it and getting the next element
                3. Remove this arbitrary request from the cache
        """
        diff_set: set[int] = self.cache.difference(found)
        request = next(iter(diff_set))
        self.cache.remove(request)

    def process_requests(self) -> int:
        """
            Iterates over the list of requests, adding them to the cache while updating the cache in the most optimal manner

            Returns the number of cache misses
        """
        num_misses: int = 0
        for request in self.requests:
            self.requests.pop(0)  # Remove the current request being processed so that the algorithm does not take it into account

            if request in self.cache:
                continue
            else:
                num_misses += 1  # Counter goes up if the item is not already in the cache (even if its empty)

                if len(self.cache) == self.capacity:
                    # The cache is full, perform the algorithm to remove the most optimal request from the cache
                    self.remove_request_from_cache()

                self.cache.add(request)

        return num_misses