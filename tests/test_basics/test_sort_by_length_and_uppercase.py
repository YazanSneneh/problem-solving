import pytest
from source.basics.sort_by_length_and_uppercase import sort_by_length_and_uppercase

@pytest.mark.parametrize("test_input, expected, message", [
    (["apple", "banana", "pear", "kiwi", "plum", "orange"], [["BANANA", "ORANGE", "APPLE", "PEAR", "KIWI", "PLUM"]], ""),
    ([], None, "List is Empty"),
    ([1, "banana"], TypeError, "The list contains non-string elements.")
])
def test_sort_by_length_and_uppercase(test_input, expected, message):
    if isinstance(expected, type):
        with pytest.raises(expected, match=message):
             sort_by_length_and_uppercase(test_input)
    else:
        result = sort_by_length_and_uppercase(test_input)
        result == expected, message