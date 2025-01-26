import json
import time
import cProfile
import ijson


def parse_large_json_array(file_path, condition):
    """
    Parses a large JSON array and extracts specific data based on a given condition.

    Args:
        file_path (str): Path to the JSON file.
        condition (callable): A function that takes a JSON object and returns True if the object matches the condition.

    Returns:
        list: A list of JSON objects that match the condition.
    """
    extracted_data = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Use ijson to parse the large JSON array
            for item in ijson.items(file, 'item'):
                # Apply the condition to filter the data
                if condition(item):
                    extracted_data.append(item)
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return extracted_data


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
    result = parse_large_json_array(file_path, example_condition)
    print(f"Total time taken in {time.time() - start_time} secs")

    cProfile.run('parse_large_json_array(file_path, example_condition)')
    # Print the extracted data
    # for item in result:
    #     print(json.dumps(item, indent=4))

    # 0.012398719787597656 secs
