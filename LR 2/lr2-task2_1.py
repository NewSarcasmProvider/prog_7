import math
import timeit
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor

def integrate(func, a, b, n_iter):
    # Your existing integrate function code here...
    pass

def calculate_integration_time(func, a, b, n_iter, num_threads, num_processes):
    # Measure time for the given number of threads
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        time_thread = timeit.timeit(lambda: list(executor.map(lambda _: integrate(func, a, b, n_iter), range(num_threads))), number=100)

    # Measure time for the given number of processes
    with Pool(processes=num_processes) as pool:
        time_process = timeit.timeit(lambda: list(pool.map(lambda _: integrate(func, a, b, n_iter), range(num_processes))), number=100)

    return time_thread, time_process

if __name__ == "__main__":
    n_iter = 10**6
    func_to_integrate = math.atan
    a = 0
    b = math.pi / 2

    # Test with different numbers of threads and processes (2, 4, 6)
    for num_threads_processes in [2, 4, 6]:
        time_thread, time_process = calculate_integration_time(func_to_integrate, a, b, n_iter, num_threads_processes, num_threads_processes)

        print(f"Threads/Processes: {num_threads_processes}")
        print(f"Time (Threads): {time_thread} seconds")
        print(f"Time (Processes): {time_process} seconds")
