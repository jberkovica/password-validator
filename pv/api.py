"""HTTP REST-like API for Password Validator"""
from flask import Flask, jsonify, request

from pv.pv_oop import (
    PasswordValidator, RuleMinLength, RuleMaxLength,
    RuleMixedCaseLetters,
)


def create_app(password_validator=None):
    """Flask application factory

    :param password_validator: `PasswordValidator` instance
    :return: Flask aplication instance
    """
    app = Flask(__name__)

    if password_validator is None:
        # Create PasswordValidator instance with some "default" rules configured
        password_validator = PasswordValidator(
            RuleMinLength(min_length=4),
            RuleMaxLength(max_length=10),
            RuleMixedCaseLetters(),
        )
    assert isinstance(password_validator, PasswordValidator)

    @app.route('/', methods=["POST"])
    def validate():
        """Password validation endpoint implementation"""
        password = request.json["password"]
        validation_result, failures = password_validator.validate(password)
        return jsonify({
            "valid": validation_result,
            "reasons": failures
        })

    return app


if __name__ == '__main__':
    create_app().run()
