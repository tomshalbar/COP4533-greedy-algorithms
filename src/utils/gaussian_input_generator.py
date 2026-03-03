import random
import os

"""Change the mu, sd, sample_size, cache_capacity to desired values.
run from COP4533-greedy-algorithms root like this: python src/utils/gaussian_input_generator.py"
"""

mu = 100
sd = 10
sample_size = 200
cache_capacity = 30

input_dir_path = "./inputs"
file_name = f"{cache_capacity}_{sample_size}_{mu}_{sd}.txt"
file_path = os.path.join(input_dir_path, file_name)

gaussian_integers_list = [round(random.gauss(mu, sd)) for _ in range(sample_size)]

with open(file_path, "w") as f:
    f.write(f"{cache_capacity} {sample_size}\n")
    f.write(f'{" ".join(str(i) for i in gaussian_integers_list)}\n')
