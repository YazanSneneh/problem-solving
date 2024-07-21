import pytest
from source.basics import problems_set_one as problems


@pytest.mark.parametrize("number_one, number_two, expected, message", [
    (5, 5, 10, "the result should be 10")
])
def test_add(number_one, number_two, expected, message):
    result = problems.add(number_one, number_two)
    assert result == expected, message


@pytest.mark.parametrize("value,expected, message", [
    (3, 6, "Factorial of 3 should be 6"),
    (0, 1, "Factorial of 0 should be 1"),
    (-3, 6, "Factorial of minus value should be the factorial of it's absolute value")
])
def test_factorial(value, expected, message):
    result = problems.factorial(value)
    assert result == expected, message


@pytest.mark.parametrize( "number, expected, message", [
    (0, [], "fibonacci sequence of less than 1 should be nothing"),
    (1, [1], "fibonacci sequence of 1 should be 1"),
    (2, [1, 1], "fibonacci sequence of 2 should be 1, 1"),
    (3, [1, 1, 2, 3, 5], "fibonacci sequence of 1, 1, 2, 3, 5"),
    (10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144], "fibonacci sequence of 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144")
])
def test_fibonacci_sequence(number, expected, message):
    result = problems.fibonacci_sequence(number)
    assert result == expected, message


@pytest.mark.parametrize("str, expected, message",[
    ("nana", "anan", "expected result should be anan")
])
def test_reverse_string(str, expected, message):
    result = problems.reverse_string(str)
    assert result == expected, message