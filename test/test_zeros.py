import pytest

from my_funcs.zeros import zeros


@pytest.mark.parametrize("n, expected_result", [(0, 0), (6, 1), (30, 7), (12, 2)])
def test_zeros(n, expected_result):
    assert zeros(n) == expected_result
    assert zeros(n) == expected_result
    assert zeros(n) == expected_result
