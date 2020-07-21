"""Password Validator acceptance tests"""
from pv.pv_oop import *
from conftest import *


@pytest.fixture
def pvfix(dictwords):
    validator = PasswordValidator(
        RuleMinLength(min_length=4),
        RuleMaxLength(max_length=10),
        RuleHistory(recent_len=5),
        RuleDictionaryWord(dictionary=dictwords),
        RuleMixedCaseLetters(),
    )
    return validator


@pytest.mark.validator
@pytest.mark.parametrize(
    "password, kwargs",
    (
        ("aB0_cd", dict(history=["aB0_cd", "a", "b", "c", "d", "e"])),
        ("Aa_zxcvbn8", dict()),
    ),
)
def test_password_validator_valid_passwords(pvfix, password, kwargs):
    """
    Given I have PasswordValidator configured with rules:

        min pass length 4, max 10
        password not in recent 5 password list
        password does not contain dictionary words
        password uses mixed case letters

    When I pass VALID password for validation to PasswordValidator
    Then validation result is VALID
    """
    validation_result, failures = pvfix.validate(password, **kwargs)
    assert not failures, "No validation failures expeced for valid password"
    assert validation_result is True, f"Expected password {password} to be valid"


@pytest.mark.validator
@pytest.mark.parametrize(
    "password, reasons, kwargs,",
    (
        ("aB0_cd", [RuleHistory.REASON], dict(history=["aB0_cd", "a", "b", "c", "d"])),
        ("$D_0qWertY8Us", [RuleDictionaryWord.REASON, RuleMaxLength.REASON], dict()),
        ("aaa", [RuleMixedCaseLetters.REASON, RuleMinLength.REASON], dict()),
    ),
)
def test_password_validator_invalid_passwords(pvfix, password, reasons, kwargs):
    """
    Given I have PasswordValidator configured with rules:

        min pass length 4, max 10
        password not in recent 5 password list
        password does not contain dictionary words
        password uses mixed case letters

    When I pass INVALID password for validation to PasswordValidator
    Then validation result is VALID
    And validation fails with expected reasons
    """
    validation_result, failures = pvfix.validate(password, **kwargs)
    assert failures, "Expected validation failures for invalid password"
    assert sorted(failures) == sorted(reasons)
    assert validation_result is False, f"Expected password {password} to be invalid"
