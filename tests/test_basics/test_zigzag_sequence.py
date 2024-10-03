import pytest
from source.basics.zigzag_sequence import find_zigzag_sequence
@pytest.mark.parametrize("test_numbers, number, expected_result, message", [
    ([1, 2, 3, 4, 5, 6, 7], 7, [1, 2, 3, 7, 6, 5, 4], "6 because no missing number in the list"),
    ([], 0, [], "Empty sequence should return an empty sequence."),
    ([1], 1, [1], "Sequence with a single element should return the same element."),
    ([1, 2, 3, 4, 5, 6], 6, [1, 2, 3, 6, 5, 4], "Zigzag sequence should be generated for even-length sequences."),
    ([-3, -2, -1, 0, 1, 2], 6, [-3, -2, -1, 2, 1, 0], "Zigzag sequence should work with negative numbers."),
    ([1000, 2000, 3000, 4000, 5000, 6000], 6, [1000, 2000, 3000, 6000, 5000, 4000], "Zigzag sequence should handle large numbers."),
    ([0, 1, 2, 3, 4, 5], 6, [0, 1, 2, 5, 4, 3], "Zigzag sequence should handle zero correctly."),
])
def test_find_zigzag_sequence(test_numbers, number, expected_result, message):
    result = find_zigzag_sequence(test_numbers, number)
    assert result == expected_result, message
