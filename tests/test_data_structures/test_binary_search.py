import pytest
from source.data_structure import binary_search
@pytest.mark.parametrize("arr, value ,expected, message", [
([1,2,3,4,5,6,7,8], 5, 4, "good job"),
([1,2,3,5, 4], 5, 4, "Array is not sorted"),
([], 5, -1, "good job")
])
def test_binary_search(arr, value ,expected, message):
    result = binary_search.binary_search(arr, value)
    assert result == expected, message