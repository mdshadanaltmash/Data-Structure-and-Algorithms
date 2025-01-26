# # import multiprocessing
# # import time
# #
# #
# # def square_numbers(numbers):
# #     """
# #     Function to compute the square of a list of numbers.
# #     """
# #     return [n ** 2 for n in numbers]
# #
# #
# # if __name__ == "__main__":
# #     # Input data
# #     numbers = list(range(1, 100000000))
# #
# #     # Split data into chunks for multiprocessing
# #     num_processes = 4
# #     chunk_size = len(numbers) // num_processes
# #     chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
# #
# #     # Without multiprocessing (single process)
# #     start = time.time()
# #     results_single = [square_numbers(chunk) for chunk in chunks]
# #     end = time.time()
# #     print(f"Time without multiprocessing: {end - start:.2f} seconds")
# #
# #     # With multiprocessing
# #     start = time.time()
# #     with multiprocessing.Pool(num_processes) as pool:
# #         results_multi = pool.map(square_numbers, chunks)
# #     end = time.time()
# #     print(f"Time with multiprocessing: {end - start:.2f} seconds")
#
#
# import multiprocessing
# import time
#
#
# def square_numbers(numbers):
#     """
#     Function to compute the square of a list of numbers.
#     """
#     return [n ** 2 for n in numbers]
#
#
# def main():
#     # Input data
#     numbers = list(range(1, 100000000))
#
#     # Split data into chunks for multiprocessing
#     num_processes = 4
#     chunk_size = len(numbers) // num_processes
#     chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
#
#     # Without multiprocessing (single process)
#     start = time.time()
#     results_single = [square_numbers(chunk) for chunk in chunks]
#     end = time.time()
#     print(f"Time without multiprocessing: {end - start:.2f} seconds")
#
#     # With multiprocessing
#     start = time.time()
#     with multiprocessing.Pool(num_processes) as pool:
#         results_multi = pool.map(square_numbers, chunks)
#     end = time.time()
#     print(f"Time with multiprocessing: {end - start:.2f} seconds")
#
#
# if __name__ == "__main__":
#     main()


import multiprocessing
import time


def square_numbers(numbers):
    """
    Function to compute the square of a list of numbers.
    """
    return [n ** 2 for n in numbers]


def main():
    # Input data
    numbers = list(range(1, 1_00_000_000))  # Large dataset for noticeable multiprocessing benefit

    # Number of processes to use
    num_processes = multiprocessing.cpu_count()  # Use the number of CPU cores
    chunk_size = len(numbers) // num_processes  # Larger chunks reduce overhead
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

    # Without multiprocessing (single process)
    start = time.time()
    results_single = [square_numbers(chunk) for chunk in chunks]
    end = time.time()
    print(f"Time without multiprocessing: {end - start:.2f} seconds")

    # With multiprocessing
    start = time.time()
    with multiprocessing.Pool(num_processes) as pool:
        results_multi = pool.map(square_numbers, chunks)
    end = time.time()
    print(f"Time with multiprocessing: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()
