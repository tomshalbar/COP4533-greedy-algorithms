# COP4533-greedy-algorithms

### Collaborators:
- Tom Shal-bar, ID 36397041
- Thomas Tavera 

### Setup: 

We did not use any package outside of python standard library, so there is no need for a new venv.

run (from home directory): 

```bash
python -m src.main inputs/example1.in
```

saved location: ```outputs/example1.out```

#### Note about our implementation:
Example files are generated using a gaussian distribution to simulate real cache querying.

---
### Written Component 

#### 1.
| input file | k | m | FIFO | LRU | OPTFF |
| :---: | :---: | :---: | :---: | :---: | :---: |
| example1.in | 10 | 40 | 29 | 30 | 23 |
| example2.in | 10 | 200 | 164 | 167 | 118 |
| example3.in | 20 | 200 | 151 | 144 | 94 |
| example4.in | 30 | 200 | 82 | 76 | 52 |
| example5.in | 40 | 500 | 268 | 3255 | 138 |

a. OPTFF had the fewest misses for each input file.

b. For our datasets, which are discrete Gaussian-based, we tried to reproduce register access requests, which naturally have some more popular registers and some less. FIFO and LRU have about the same effectiveness for a small cache size (<10), but LRU was better for a large cache size (> 20). 

#### 2.
There should be an infinite number of sequences for which OPTFF incurs strictly fewer misses than LRU or FIFO.


One template that we constructed is:

a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, ..., a<sub>k</sub>, a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, ..., a<sub>k</sub>

where ∀ i, j : a<sub>i</sub> ≠ a<sub>j</sub>

##### Some examples

a. 1, 2, 3, 4, 1, 2, 3, 4

| Cache | Misses |
|------|--------|
| LRU | 8 |
| OPTFF | 5 |
--- 
b. 5, 8, 12, 534, 31, 32, 12, 19, 432, 234, 2, 1, 5, 8, 12, 534, 31, 32, 12, 19, 432, 234, 2, 1

| Cache | Misses |
|------|--------|
| LRU | 24 |
| OPTFF | 19 |

#### 3.
Assume that there is an optimal algorithm O, that produces a different cache sequence than Belady's Farthest-in-Future algorithm, B.

Assume we have a requests sequence R = r<sub>1</sub>, r<sub>2</sub>, ..., r<sub>n</sub>, and that the cache size is m.

Let O = o<sub>1</sub>, o<sub>2</sub>, ..., o<sub>n</sub> be the sequence of caches produced by optimal algorithm O after each request.
Let B = b<sub>1</sub>, b<sub>2</sub>, ..., b<sub>n</sub> be the sequence of caches produced by OPTFF algorithm B after each request.

Since the caches do not fill until r<sub>m</sub>, O and B are by definition equivalent until that part, so
O' = b<sub>1</sub>, b<sub>2</sub>, ..., b<sub>m</sub>, o<sub>m+1</sub>, ..., o<sub>n</sub>

Let r<sub>m+1</sub> be the first time O and B differ.

At request r<sub>m+1</sub>, an element will be evicted from the cache. Let *e* be the element that OPTFF decided to evict, resulting in cache b<sub>m+1</sub>.

a) If *e* never occurs again in requests, then removing it will not lead to any more misses in the future, therefore we can exchange o<sub>m+1</sub> with b<sub>m+1</sub> in O without incurring any more misses.

b) If *e* does occur again in requests, then removing it will lead to a miss in the future. But since it is the farthest in the future, every other element in the cache also occurs again, so any other removal will also cause an additional miss. therefore we can exchange o<sub>m+1</sub> with b<sub>m+1</sub> in O without incurring any more misses.

Now, O'' = b<sub>1</sub>, b<sub>2</sub>, ..., b<sub>m</sub>, b<sub>m+1</sub>, o<sub>m+2</sub>, ..., o<sub>n</sub>

We can keep doing this exchange until we exchange O to equal b<sub>1</sub>, b<sub>2</sub>, ..., b<sub>n</sub> without incurring any additional misses.

Therefore, we prove that an optimal algorithm O is not more optimal than Belady's Farthest-in-Future algorithm, therefore Belady's Farthest-in-Future is optimal in offline conditions.

