import pytest

from my_funcs.int32_to_ip import int32_to_ip


@pytest.mark.parametrize("int32, expected_string", [(2149583361, "128.32.10.1"),
                                                    (3232235777, "192.168.1.2"),
                                                    (32, "0.0.0.32"),
                                                    (0, "0.0.0.0")])
def test_int32_to_ip(int32, expected_string):
    assert int32_to_ip(int32) == expected_string
