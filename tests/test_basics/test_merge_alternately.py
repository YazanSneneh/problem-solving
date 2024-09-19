import pytest
from source.basics.merge_alternately import merge_alternately


@pytest.mark.parametrize("word1, word2, expected, message", [
    ("ace", "bdf", "abcdef", "the result miss matched"),
    ("", "ace", "ace", "the result miss matched"),
    ("test", "", "test", "the result miss matched")
])
def test_merge_alternately(word1, word2, expected, message):
    result = merge_alternately(word1, word2)
    assert result == expected, message
