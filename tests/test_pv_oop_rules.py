"""Validation rules tests"""
import pytest
from pv.pv_oop import *


@pytest.mark.validatorrules
@pytest.mark.parametrize(
    ("password", "rule", "exp_result"),
    (
        ("a",      RuleMinLength(1), True),
        ("a" * 5,  RuleMinLength(5), True),
        ("a" * 10, RuleMinLength(5), True),
        ("a" * 4,  RuleMinLength(5), False),
        ("",       RuleMinLength(5), False),
        # ("a",       RuleMinLength(0), ???),
    ),
)
def test_rule_min_length(password, rule, exp_result):
    res = rule.isvalid(password)
    assert res is exp_result, "Min length rule validation failed"


@pytest.mark.validatorrules
@pytest.mark.parametrize(
    ("password", "rule", "exp_result"),
    (
        ("a",      RuleMaxLength(1), True),
        ("a" * 5,  RuleMaxLength(5), True),
        ("a" * 10, RuleMaxLength(5), False),
        ("a" * 4,  RuleMaxLength(5), True),
        ("",       RuleMaxLength(5), True),
        # ("a",       RuleMinLength(0), ???),
    ),
)
def test_rule_max_length(password, rule, exp_result):
    res = rule.isvalid(password)
    assert res is exp_result, "Max length rule validation failed"


PASSWORD_HISTORY = ["a", "b", "c", "d", "e"]


@pytest.mark.validatorrules
@pytest.mark.parametrize(
    ("password", "rule", "history", "exp_result"),
    (
        ("a", RuleHistory(len(PASSWORD_HISTORY)),     PASSWORD_HISTORY, False),
        ("a", RuleHistory(len(PASSWORD_HISTORY) + 1), PASSWORD_HISTORY, False),
        ("a", RuleHistory(len(PASSWORD_HISTORY) - 1), PASSWORD_HISTORY, True),
        ("e", RuleHistory(len(PASSWORD_HISTORY) - 1), PASSWORD_HISTORY, False),
    ),
)
def test_rule_history(password, rule, history, exp_result):
    res = rule.isvalid(password, history=history)
    assert res is exp_result, "Password history rule validation failed"


DWORDS = ["abcde", "password", "qwerty"]


@pytest.mark.validatorrules
@pytest.mark.parametrize(
    ("password", "rule", "exp_result"),
    (
        ("@passwordOpa", RuleDictionaryWord(DWORDS), False),
        ("_QweRtY_",     RuleDictionaryWord(DWORDS), False),
        ("assword",      RuleDictionaryWord(DWORDS), True),
        ("lalala",       RuleDictionaryWord(DWORDS), True),
    ),
)
def test_rule_dictionary_word(password, rule, exp_result):
    res = rule.isvalid(password)
    assert res is exp_result, "Password dictionary word rule validation failed"


@pytest.mark.validatorrules
@pytest.mark.parametrize(
    ("password", "rule", "exp_result"),
    (
        ("aA", RuleMixedCaseLetters(), True),
        ("āŠ", RuleMixedCaseLetters(), True),
        ("AB", RuleMixedCaseLetters(), False),
        ("ab", RuleMixedCaseLetters(), False),
    ),
)
def test_rule_mixed_case_letters(password, rule, exp_result):
    res = rule.isvalid(password)
    assert res is exp_result, "Password mixed case letter rule validation failed"
