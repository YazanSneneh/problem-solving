import pytest
from source.basics import problems_set_two as problems


@pytest.mark.parametrize("test_numbers, expected_result, message", [
    ([], 0, "the list is empty"),
    ([1, 2, 3, 4, 5], 0, "the 0 number is missing is in the beginning"),
    ([0, 1, 2, 4, 5], 3, "the 3 number is missing is in the middle"),
    ([0, 1, 2, 3, 4, 5], 6, "6 because no missing number in the list"),
])
def test_missing_number(test_numbers, expected_result, message):
    result = problems.missing_number(test_numbers)
    assert result == expected_result, message


@pytest.mark.parametrize('test_input, expected, message', [
    ([7, 1, 9], (1, 9), "expected results are 1, 9"),
    ([], None, "the list is empty"),
])
def test_find_larges_smallest_number(test_input, expected, message):
    result = problems.find_larges_smallest_number(test_input)
    assert result == expected, message


@pytest.mark.parametrize('test_input, expected, message', [
    ([3, 1, 9], (1, 9), "expected results are 1, 9"),
    ([], None, "the list is empty"),
])
def test_find_larges_smallest_number_built_in_method(test_input, expected, message):
    result = problems.find_larges_smallest_number_built_in_method(test_input)
    assert result == expected, message