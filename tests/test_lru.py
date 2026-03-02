import unittest
import random
from src.lru import Lru as lru


class Testlru(unittest.TestCase):
    seed = 4
    rng = random.Random(seed)

    def test_constructor(self):
        f = lru(2)
        self.assertEqual(f.capacity, 2)

    def test_miss_cache_not_full(self):
        f = lru(2)
        v = f.request(1)
        self.assertEqual(v, "miss")

    def test_hit_after_miss_cache_not_full(self):
        f = lru(2)
        f.request(1)
        v = f.request(1)
        self.assertEqual(v, "hit")

    def test_no_double_cache_insertion(self):
        f = lru(2)
        f.request(1)
        f.request(1)
        self.assertEqual(len(f.cache), 1)

    def test_request_of_not_least_recent_eviction(self):
        f = lru(2)
        f.request(1)
        f.request(2)
        f.request(1)
        f.request(3)
        v = f.request(1)
        self.assertEqual(v, "hit")
        self.assertEqual(f.cache, [3, 1])

    def test_request_of_least_recent_eviction(self):
        f = lru(2)
        f.request(1)
        f.request(2)
        f.request(1)
        f.request(3)
        v = f.request(2)
        self.assertEqual(v, "miss")

    def test_hit_after_miss_full_cache(self):
        f = lru(2)
        f.request(1)
        f.request(2)
        f.request(3)

        v = f.request(3)
        self.assertEqual(v, "hit")
        self.assertEqual(f.cache, [2, 3])

    def test_hit_after_miss_non_full_cache(self):
        f = lru(2)
        f.request(1)
        v = f.request(1)
        self.assertEqual(v, "hit")

    def test_large_request_amount(self):
        capacity = 4  # must stay two for manual gt calculation truth to hold
        requests = [1, 2, 3, 4, 5, 6, 3, 5, 1, 4, 5, 3, 3, 6]
        gt_results = [
            "miss",
            "miss",
            "miss",
            "miss",
            "miss",
            "miss",
            "hit",
            "hit",
            "miss",
            "miss",
            "hit",
            "hit",
            "hit",
            "miss",
        ]

        final_gt_cache = [4, 5, 3, 6]
        f = lru(capacity)
        test_results = list()
        for r in requests:
            v = f.request(r)
            test_results.append(v)

        self.assertEqual(test_results, gt_results)
        self.assertEqual(f.cache, final_gt_cache)


if __name__ == "__main__":
    unittest.main()
