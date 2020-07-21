
rules = {
    'max_length': 10,
    'min_length': 4,
    'min_upper_case': 1,
    'min_lower_case': 1,
    'min_special_char': 1,
    'min_digit': 1,
    'history_recent_count': 10
}


def validate_max_length(password, count):
    if len(password) <= count:
        return True
    else:
        return False


def validate_min_length(password, count):
    if len(password) >= count:
        return True
    else:
        return False


def validate_upper_case(password, count):
    upper_case_counter = 0
    for p in password:
        if p.isalpha() and p == p.upper():
            upper_case_counter += 1

    if upper_case_counter >= count:
        return True
    else:
        return False
    return


def validate_lower_case(password, count):
    upper_case_counter = 0
    for p in password:
        if p.isalpha() and p == p.lower():
            upper_case_counter += 1

    if upper_case_counter >= count:
        return True
    else:
        return False
    return


def validate_special_char(password, count):
    special_chars = r',~!@#$%^&*()_-+={[}}|\:;<>?/'
    special_chars_counter = 0
    for p in password:
        if p in special_chars:
            special_chars_counter += 1

    if special_chars_counter >= count:
        return True
    else:
        return False


def validate_digits(password, count):
    digit_counter = 0
    for p in password:
        if p.isdigit():
            digit_counter += 1

    if digit_counter >= count:
        return True
    else:
        return False


def validate_history(password, history, recent_count):
    """checking most recent passwords in the end of the list
    password is valid (returns True) if it hasn't been in last history items"""
    return password not in history[-recent_count:]


def validate_password(password):

    failure_list = []

    if not validate_max_length(password, rules['max_length']):
        failure_list.append('Password length should be smaller')
    if not validate_min_length(password, rules['min_length']):
        failure_list.append('Password length should be bigger')
    if not validate_upper_case(password, rules['min_upper_case']):
        failure_list.append('Password should contain more upper case chars')
    if not validate_lower_case(password, rules['min_lower_case']):
        failure_list.append('Password should contain more lower case chars')
    if not validate_digits(password, rules['min_digit']):
        failure_list.append('Password should contain more digits')
    if not validate_special_char(password, rules['min_special_char']):
        failure_list.append('Password should contain more special chars')

    history_passwords = ['abc', 'aaa', 'abc123', 'jjj']
    if not validate_history(password, history=history_passwords, recent_count=rules['history_recent_count']):
        failure_list.append('Password should be unique, you have used it before')

    if not failure_list:
        print(f'Password {password} is valid')
    else:
        print(f'Password {password} is invalid. Failures:')
        for failure in failure_list:
            print(f'\t{failure}')


if __name__ == "__main__":

    test_passwords = ['aB7$', 'AAAAA', 'c1_Df', 'De3Sp19t_M', 'aaa', '12345678', b'lalala', '', 12345]

    for p in test_passwords:
        validate_password(str(p))
