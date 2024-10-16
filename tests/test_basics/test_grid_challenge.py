import pytest
from source.basics.grid_challenge import grid_challenge


@pytest.mark.parametrize("grid, expected_output, message",[
    (["ebacd", "fghij", "olmkn", "trpqs", "xywuv"], "YES", "Expected YES"),
    (["zyx"], "YES", "Expected YES"),
    (["zyx", "wvu", "tsr"], "NO", "Expected NO"),
    (["a"], "YES", "Only 1 element in the list, so technically it's sorted!"),
    (["acd", "bca", "dac"], "NO", "Expected NO"),
] )
def test_grid_challenge(grid, expected_output, message):
    result = grid_challenge(grid)
    assert result == expected_output