from pv.pv_script import *
import pytest


@pytest.mark.parametrize(
    "password, max_length, expected_result",
    (pytest.param('aaa', 4, True),
     pytest.param('aaaa', 4, True),
     pytest.param('aaaaa', 4, False))
)
def test_validate_max_length(password, max_length, expected_result):
    assert validate_max_length(password=password, count=max_length) is expected_result


@pytest.mark.parametrize(
    "password, min_length, expected_result",
    (pytest.param('a', 2, False),
     pytest.param('aa', 2, True),
     pytest.param('aaa', 2, True))
)
def test_validate_min_length(password, min_length, expected_result):
    assert validate_min_length(password=password, count=min_length) is expected_result


@pytest.mark.parametrize(
    "password, min_upper_case, expected_result",
    (pytest.param('Abc', 1, True),
     pytest.param('Abc', 2, False),
     pytest.param('ABc', 2, True))
)
def test_validate_upper_case(password, min_upper_case, expected_result):
    assert validate_upper_case(password=password, count=min_upper_case) is expected_result


@pytest.mark.parametrize(
    "password, min_lower_case, expected_result",
    (pytest.param('ABC', 1, False),
     pytest.param('ABc', 2, False),
     pytest.param('abC', 2, True))
)
def test_validate_lower_case(password, min_lower_case, expected_result):
    assert validate_lower_case(password=password, count=min_lower_case) is expected_result


@pytest.mark.parametrize(
    "password, min_special_char, expected_result",
    (pytest.param('aaa%', 1, True),
     pytest.param('aaa%', 2, False),
     pytest.param('aaa%%', 2, True))
)
def test_validate_special_char(password, min_special_char, expected_result):
    assert validate_special_char(password=password, count=min_special_char) is expected_result


@pytest.mark.parametrize(
    "password, min_digit, expected_result",
    (pytest.param('aaa3', 1, True),
     pytest.param('aaa3', 2, False),
     pytest.param('aaa33', 2, True))
)
def test_validate_digits(password, min_digit, expected_result):
    assert validate_digits(password=password, count=min_digit) is expected_result


@pytest.mark.parametrize(
    "password, recent_count, expected_result",
    (pytest.param('abc', 3, True),
     pytest.param('aaa', 3, False),
     pytest.param('abc123', 3, False))
)
def test_validate_history_parametrize(password, recent_count, expected_result):
    history_passwords = ['abc', 'aaa', 'abc123', 'jjj']
    assert validate_history(password=password, history=history_passwords, recent_count=recent_count) is expected_result


