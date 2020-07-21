"""HTTP Rest like API tests"""

import requests
from pv.pv_oop import *
import pytest


URL = 'http://localhost:5000'


@pytest.mark.parametrize("password", ("PasWor$%'", "Aa1$asd", 'Aa_zxcvbn8'))
def test_valid_password(live_server, password):
    """
    Given PV HTTP API server

    When I make POST request with valid password in POST-data

    Then I get response with HTTP code 200
    And JSON payload with validation status PASSED
    """
    url = live_server.url()

    post_data = {
        "password": password
    }

    response = requests.post(url, json=post_data)

    status_code = response.status_code
    assert response.status_code == 200, f'Expected HTTP status 200, got {status_code}'

    resp_body = response.json()

    assert resp_body["valid"] is True
    assert resp_body["reasons"] == []


@pytest.mark.parametrize(
    ("password", "rules"),
    (
        ("aa", [RuleMinLength(3)]),
        ("aaaaaa", [RuleMaxLength(5)]),
        ("aaaaaa", [RuleMaxLength(5), RuleMixedCaseLetters]),
    ),
)
def test_invalid_password(live_server, password, rules):
    """
    Given PV HTTP API server

    When I make POST request with invalid password in POST-data

    Then I get response with HTTP code 200
    And JSON payload with validation status FAILED
    """
    url = live_server.url()

    password = "aaa"
    post_data = {
        "password": password
    }

    response = requests.post(url, json=post_data)

    status_code = response.status_code
    assert response.status_code == 200, f"Expected HTTP status 200, got {status_code}"

    resp_body = response.json()

    assert resp_body["valid"] == False
    fail_reasons = sorted(resp_body["reasons"])
    expected_reasons = sorted([RuleMixedCaseLetters.REASON, RuleMinLength.REASON])
    assert fail_reasons == expected_reasons



# TODO: negative test scenarios
# - invalid request JSON payload (no password field, empty password field)
# - Add parametrization to implemented base tests
