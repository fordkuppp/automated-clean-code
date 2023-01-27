from automated_clean_code.exercise_20_histlib import find_max_min, get_counter_dict


def test_histlib_1(test_file_1: str):
    assert get_counter_dict(test_file_1) == {"a": 2, "b": 3}
    assert find_max_min({"a": 2, "b": 3}) == {"min_key": "a", "min_value": 2, "max_key": "b", "max_value": 3}


def test_histlib_2(test_file_2: str):
    assert get_counter_dict(test_file_2) == {"1": 7, "3": 3, "2": 4}
    assert find_max_min({"1": 7, "3": 3, "2": 4}) == {"min_key": "3", "min_value": 3, "max_key": "1", "max_value": 7}
