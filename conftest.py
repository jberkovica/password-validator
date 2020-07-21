import pytest
from pv.api import create_app
from pv.pv_oop import *


@pytest.fixture
def pvfix(dictwords):
    """Fixture provides PasswordValidator instance with rules"""
    validator = PasswordValidator(
        RuleMinLength(min_length=4),
        RuleMaxLength(max_length=10),
        RuleHistory(recent_len=5),
        RuleDictionaryWord(dictionary=dictwords),
        RuleMixedCaseLetters(),
    )
    yield validator


@pytest.fixture
def dictwords():
    """Fixture provides dictionary words"""
    return (
        "qwerty",
        "password",
        "passw0rd",
        "abcde",
    )


@pytest.fixture
def app(pvfix):
    """Fixture provides Flask application instance

    This is required by `live_server` fixture from pytest-flask plugin.
    """
    app = create_app(password_validator=pvfix)
    return app
