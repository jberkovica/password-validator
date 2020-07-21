import re


"""Password validator"""


class PasswordValidator:
    """Defines a password validator application"""
    def __init__(self, *rules):
        """
        On instance creation we pass configured Rule instances that password
        will be checked against.
        """
        self.rules = rules

    def validate(self, password, **kw):
        """Check password against configured rules"""

        results = {}
        for rule in self.rules:
            results[rule] = rule.isvalid(password, **kw)

        failures = []
        for r, result in results.items():
            if not result:
                failures.append(r.REASON)

        if failures:
            return False, failures
        else:
            return True, []


############################################################
# Rules
############################################################

class RuleMinLength:
    """Check passwords against minimum length"""
    REASON = "Password is too short"

    def __init__(self, min_length):
        self.min_length = min_length

    def isvalid(self, password, **kw):
        """Check if given password is valid"""
        if len(password) >= self.min_length:
            return True
        else:
            return False


class RuleMaxLength:
    """Check passwords against maximum length"""
    REASON = "Password is too long"

    def __init__(self, max_length):
        self.max_length = max_length

    def isvalid(self, password, **kw):
        """Check if given password is valid"""
        if len(password) <= self.max_length:
            return True
        else:
            return False


class RuleHistory:
    """Check password against previous used password history"""
    REASON = "Password has been used recently"

    def __init__(self, recent_len):
        self.recent_len = recent_len

    def isvalid(self, password, **kw):
        """Check if given password is valid"""

        history = kw.get('history', [])
        return password not in history[-self.recent_len:]


class RuleDictionaryWord:
    """Check password against common dictionary words"""
    REASON = "Password contains a dictionary word"

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def isvalid(self, password, **kw):
        """Check if given password is valid"""

        for word in self.dictionary:
            found = re.search(word, password.lower())
            if found:
                return False

        return True


class RuleMixedCaseLetters:
    """Check password contains mixed case letters"""
    REASON = "Password does not contain mixed case letters"

    def __init__(self):
        pass

    def isvalid(self, password, **kw):
        upper_case_counter = 0
        lower_case_counter = 0

        for p in password:
            if p.isalpha() and p == p.upper():
                upper_case_counter += 1
            if p.isalpha() and p == p.lower():
                lower_case_counter += 1

        if upper_case_counter > 0 and lower_case_counter > 0:
            return True
        else:
            return False


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# TODO: Figure out what to do about character group rules
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
