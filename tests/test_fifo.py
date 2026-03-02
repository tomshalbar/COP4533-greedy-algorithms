import unittest
import random
from src.fifo import Fifo as fifo


class TestFifo(unittest.TestCase):
    seed = 4
    rng = random.Random(seed)

    def test_constructor(self):
        f = fifo(2)
        self.assertEqual(f.capacity, 2)

    def test_miss_cache_not_full(self):
        f = fifo(2)
        v = f.request(1)
        self.assertEqual(v, "miss")

    def test_no_update_on_hit(self):
        f = fifo(2)
        f.request(1)
        f.request(2)
        f.request(1)
        v = f.request(1)
        self.assertEqual(v, "hit")

    def test_no_double_cache_insertion(self):
        f = fifo(2)
        f.request(1)
        f.request(1)
        self.assertEqual(len(f.cache), 1)

    def test_first_in_eviction(self):
        f = fifo(2)
        f.request(1)
        f.request(2)
        f.request(3)
        v = f.request(1)
        self.assertEqual(v, "miss")

    def test_hit_after_miss_full_cache(self):
        f = fifo(2)
        f.request(1)
        f.request(2)
        f.request(3)

        v = f.request(3)
        self.assertEqual(v, "hit")

    def test_hit_after_miss(self):
        f = fifo(2)
        f.request(1)
        v = f.request(1)
        self.assertEqual(v, "hit")

    def test_large_request_amount(self):
        capacity = 100
        request_number = 5000
        register_count = 100
        requests = [
            TestFifo.rng.randint(0, register_count) for _ in range(request_number)
        ]
        ground_truth_cache = list()
        ground_truth_results = list()
        for r in requests:
            if r in ground_truth_cache:
                ground_truth_results.append("hit")
            else:
                if len(ground_truth_cache) < capacity:
                    ground_truth_cache.append(r)
                else:
                    ground_truth_cache.pop(0)
                    ground_truth_cache.append(r)

                ground_truth_results.append("miss")

        f = fifo(capacity)
        test_results = list()
        for r in requests:
            v = f.request(r)
            test_results.append(v)

        self.assertEqual(test_results, ground_truth_results)


if __name__ == "__main__":
    unittest.main()
