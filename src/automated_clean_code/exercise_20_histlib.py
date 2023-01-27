# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
# import argparse


def get_counter_dict(file_name: str) -> dict:
    """Imagine summary here.
    Args:
        file_name: Full path to text file

    Returns:
        counter_dict (dict): A python dictionary with key-value pairs
    """
    ret_dict = {}

    with open(file_name, "r") as f:
        for line in f:
            line = line.strip()
            if line in ret_dict:
                ret_dict[line] += 1
            else:
                ret_dict[line] = 1

    return ret_dict


def find_max_min(counter_dict: dict) -> dict:
    """

    Args:
        counter_dict: Dictionary containing key-value pairs

    Returns:
        result (dict): Dictionary containing min_key, max_key, min_value, max_value
    """
    min_key = None
    max_key = None
    min_value = 0
    max_value = 0

    for curr_key, curr_value in counter_dict.items():
        if (max_key is None) or (curr_value > max_value):
            max_key = curr_key
            max_value = curr_value
        if (min_key is None) or (curr_value < min_value):
            min_key = curr_key
            min_value = curr_value

    print(f"Min Key = {min_key} with count = {min_value}")
    print(f"Max Key = {max_key} with count = {max_value}")

    return {"min_key": min_key, "min_value": min_value, "max_key": max_key, "max_value": max_value}


# def main():
# parser = argparse.ArgumentParser(
#     description="compute the entry with the most occurrence and the least occurrence form a file"
# )
# parser.add_argument("fname", metavar="N", type=str, help="filename to compute the histogram")
# args = parser.parse_args()


# if __name__ == "__main__":
#     main()
