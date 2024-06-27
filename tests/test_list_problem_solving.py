import pytest
import questions.list_problem_solving as list_questions

@pytest.mark.parametrize('test_input, expected, message', [
([5, 1, 9], (1, 9), "expected results are 1, 9"),
    ([], None, "the list is empty"),
])
def test_find_larges_smallest_number(test_input, expected, message):
    result = list_questions.find_larges_smallest_number(test_input)
    assert  result == expected, message

@pytest.mark.parametrize('test_input, expected, message', [
([5, 1, 9], (1, 9), "expected results are 1, 9"),
    ([], None, "the list is empty"),
])
def find_larges_smallest_number_built_in_method(test_input, expected, message):
    result = list_questions.find_larges_smallest_number_built_in_method(test_input)
    assert  result == expected, message