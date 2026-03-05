from pathlib import Path
from src.fifo import Fifo as fifo
from src.lru import Lru as lru
from src.optff import OPTFF as optff

input_dir_path = Path("./inputs/")


def read_file(path: Path):
    """returns a tuple or the int cache capacity and list(int) requests read from a file"""
    with open(path, "r") as f:
        meta = f.readline().strip()
        content = f.readline().strip()

        cache_capacity = int(meta.split(" ")[0])
        requests = [int(i) for i in content.split(" ")]

        return cache_capacity, requests


def test_fifo_and_lru_caches(caches, requests):
    """ Gets the hits and misses from the lru and fifo cache eviction policies """
    results = dict()
    for cache in caches:
        results[cache.__class__.__name__] = []
        for r in requests:
            trial = cache.request(r)
            results[cache.__class__.__name__].append(trial)

    return results


def calculate_fifo_and_lru_stats(results):
    """ Sums up the hits and misses from the lru and fifo cache eviction policies """
    stats = dict()
    for cache in results:
        miss = 0
        hit = 0
        for trial in results[cache]:
            if trial == "miss":
                miss += 1
            else:
                hit += 1

        #stats[cache] = [miss, hit]
        stats[cache] = miss

    return stats


def main():
    for i, path in enumerate(input_dir_path.iterdir()):
        cache_capacity, requests = read_file(path)
        caches = [fifo(cache_capacity), lru(cache_capacity), optff(cache_capacity, requests)]
        fifo_and_lru_miss_hit_results = test_fifo_and_lru_caches(caches[:-1], requests)
        miss_stats = calculate_fifo_and_lru_stats(fifo_and_lru_miss_hit_results)
        miss_stats['OPTFF'] = caches[-1].process_requests()
        print(f"File {i} (miss): {miss_stats}")


if __name__ == "__main__":
    main()


