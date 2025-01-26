import time

import ijson
from multiprocessing import Pool, cpu_count
import json


def parse_large_json_array_parallel(file_path, condition, num_workers=None):
    """
    Parses a large JSON array and extracts specific data based on a given condition using multiprocessing.

    Args:
        file_path (str): Path to the JSON file.
        condition (callable): A function that takes a JSON object and returns True if the object matches the condition.
        num_workers (int, optional): Number of worker processes to use. Defaults to the number of CPU cores.

    Returns:
        list: A list of JSON objects that match the condition.
    """
    if num_workers is None:
        num_workers = cpu_count()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Use ijson to stream items lazily
            items = list(ijson.items(file, 'item'))

        # Split data into chunks for multiprocessing
        chunk_size = max(len(items) // num_workers, 1)
        chunks = [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

        # Use multiprocessing to process chunks in parallel
        with Pool(num_workers) as pool:
            results = pool.map(filter_chunk, [(chunk, condition) for chunk in chunks])

        # Flatten the list of results
        return [item for sublist in results for item in sublist]

    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def filter_chunk(args):
    """
    Filters a chunk of JSON objects based on the condition.

    Args:
        args (tuple): A tuple containing the chunk of data and the condition function.

    Returns:
        list: A list of JSON objects that match the condition.
    """
    chunk, condition = args
    return [item for item in chunk if condition(item)]


# Example condition function
def example_condition(data):
    """
    Example condition: Extract objects where 'status' is 'active'.
    """
    return data.get('status') == 'active'


# Example usage
if __name__ == "__main__":
    # Path to the large JSON file (a single large JSON array)
    file_path = 'large_file.json'

    # Extract data based on the example condition
    start_time = time.time()
    result = parse_large_json_array_parallel(file_path, example_condition)
    print(f"Total time taken in {time.time() - start_time} secs")

    # Print the extracted data
    # for item in result:
    #     print(json.dumps(item, indent=4))


# 0.12127804756164551 secs