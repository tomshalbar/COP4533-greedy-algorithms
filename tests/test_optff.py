import unittest
from src.optff import OPTFF as optff

class TestOPTFF(unittest.TestCase):
    def test_constructor(self):
        requests = [1, 2, 3]
        cache_size = 2
        optff_cache = optff(cache_size, requests)
        self.assertEqual(optff_cache.capacity, cache_size)
        self.assertEqual(optff_cache.requests, requests)
        self.assertEqual(len(optff_cache.cache), 0)

    def test_no_eviction_needed(self):
        requests = [1, 2, 1, 3]
        cache_size = 4
        optff_cache = optff(cache_size, requests)
        optff_misses = optff_cache.process_requests()
        self.assertEqual(optff_misses, 3)  # The number of unique requests

    def test_eviction_basic(self):
        requests = [1, 2, 3, 4, 1, 2]
        cache_size = 3
        optff_cache = optff(cache_size, requests)
        optff_misses = optff_cache.process_requests()
        self.assertEqual(optff_misses, 4)

    def test_complex_eviction_1(self):
        requests = [1, 2, 3, 4, 5, 6, 3, 5, 1, 4, 5, 3, 3, 6]
        cache_size = 4
        optff_cache = optff(cache_size, requests)
        optff_misses = optff_cache.process_requests()
        self.assertEqual(optff_misses, 7)

    def test_complex_eviction_2(self):
        requests = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
        cache_size = 3
        optff_cache = optff(cache_size, requests)
        optff_misses = optff_cache.process_requests()
        self.assertEqual(optff_misses, 9)


if __name__ == "__main__":
    unittest.main()