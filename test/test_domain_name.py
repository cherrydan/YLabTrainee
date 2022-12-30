import pytest

from my_funcs import domain_name


@pytest.mark.parametrize("url, expected_result", [("http://google.com", "google"),
                                                  ("http://google.co.jp", "google"),
                                                  ("www.xakep.ru", "xakep"),
                                                  ("https://youtube.com", "youtube")])
def test_domain_name(url, expected_result):
    assert domain_name.domain_name(url) == expected_result
