from argparse import ArgumentParser
from pathlib import Path

from src.fifo import Fifo as fifo
from src.lru import Lru as lru
from src.optff import OPTFF as optff


def read_file(path: Path):
    """returns a tuple of the int cache capacity and list(int) requests read from a file"""
    with open(path, "r") as f:
        meta = f.readline().strip()
        content = f.readline().strip()

        cache_capacity = int(meta.split(" ")[0])
        requests = [int(i) for i in content.split(" ")]

        return cache_capacity, requests


def get_cache_misses(cache: lru | fifo | optff, requests: list[int] | None = None) -> int:
    """
        Returns the number of cache misses for the LRU, FIFO, and OPTFF cache eviction policies
    """
    miss: int = 0
    if isinstance(cache, lru) or isinstance(cache, fifo):
        for r in requests:
            res = cache.request(r)
            if res == "miss":
                miss += 1
    elif isinstance(cache, optff):
        miss = cache.process_requests()
    else:
        print("Error: Cache eviction policy is not supported!!")
        return -1

    return miss


def main(input_filepath: Path) -> None:
    """
        Creates the cache eviction policies, calculates their misses, and writes them out into the desired format
    """
    cache_capacity, requests = read_file(input_filepath)

    fifo_cache: fifo = fifo(cache_capacity)
    fifo_misses: int = get_cache_misses(fifo_cache, requests)

    lru_cache: lru = lru(cache_capacity)
    lru_misses: int = get_cache_misses(lru_cache, requests)

    optff_cache: optff = optff(cache_capacity, requests)
    optff_misses: int = get_cache_misses(optff_cache)

    miss_stats: dict[str, int] = {
        "FIFO": fifo_misses,
        "LRU": lru_misses,
        "OPTFF": optff_misses
    }

    # ./inputs/example1.in --> ./outputs/example1.out
    output_dir: str = "./outputs/"
    output_file_base_name: str = str(input_filepath.stem)
    output_extension: str = ".out"
    output_file: Path = Path(output_dir + output_file_base_name + output_extension)

    # Write the caches and their misses to the output file
    with open(output_file, "w") as f:
        out_string: str = ""
        for cache, miss in miss_stats.items():
            out_string += f"{cache:<7}: {miss:>3}\n"  # F-string formatting for prettier outputs
        f.write(out_string.strip())


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(description="Script for comparing the number of misses for the FIFO, LRU, and OPTFF cache eviction policies.")

    parser.add_argument(
        "filepath",
        type=str,
        help="The filepath of the input file."
    )

    args = parser.parse_args()

    main(Path(args.filepath))


