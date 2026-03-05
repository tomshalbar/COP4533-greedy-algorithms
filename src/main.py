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


def test_caches(caches, requests):
    results = dict()
    for cache in caches:
        results[cache.__class__.__name__] = []
        for r in requests:
            trial = cache.request(r)
            results[cache.__class__.__name__].append(trial)

    return results


def calculate_stats(results):
    stats = dict()
    for cache in results:
        miss = 0
        hit = 0
        for trial in results[cache]:
            if trial == "miss":
                miss += 1
            else:
                hit += 1

        stats[cache] = [miss, hit]

    return stats


def main():
    for i, path in enumerate(input_dir_path.iterdir()):
        cache_capacity, requests = read_file(path)
        caches = [fifo(cache_capacity), lru(cache_capacity)]
        miss_hit_result = test_caches(caches, requests)
        miss_hit_stats = calculate_stats(miss_hit_result)
        print(f"File {i} (miss, hit): {miss_hit_stats}")


if __name__ == "__main__":
    main()


