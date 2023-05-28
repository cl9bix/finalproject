from multiprocessing import Pool, cpu_count
from functools import partial
import time

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def synchronous_factorize(numbers):
    results = []
    for number in numbers:
        results.append(factorize(number))
    return results

def parallel_factorize(numbers):
    pool = Pool(cpu_count())
    results = pool.map(factorize, numbers)
    pool.close()
    pool.join()
    return results

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    start_time = time.time()
    synchronous_results = synchronous_factorize(numbers)
    end_time = time.time()
    synchronous_time = end_time - start_time

    start_time = time.time()
    parallel_results = parallel_factorize(numbers)
    end_time = time.time()
    parallel_time = end_time - start_time

    print("Synchronous Results:", synchronous_results)
    print("Parallel Results:", parallel_results)
    print("Synchronous Time:", synchronous_time)
    print("Parallel Time:", parallel_time)
