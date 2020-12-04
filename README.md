# password-validator

Learning project

#### User story:
- **As** a single sigh on (SSO) PO
- **In order to** comply with secure password policy 
- **I want** password validator with configurable validation rules to check new user password against 


#### Requirements:
- Password validator (PV) as Python library
- Optional: PV as HTTP service  (http api application)
- **Validation rules**: 
    - Configurable
    - Password min / max length
    - Password history (check that pass is new, compare to last 10 user passwords), history is provided
    - Password check against dictionary words, dictionary provided
    - Password mixed case characters 
    - Password minimal special character count (example: 2 symbols of digits group and 3 from special character)
    - Negative validation result should contain explanation of reasons / rules 
    - Optional: password entropy check (how random password is) (read - how to calculate password entropy)


#### Acceptance test:
- **Given** I have password validator (PV) with rules:
    - min pass length 4, max 10
    - at least 1 upper case, at lease 1 lower case
    - at least one digit
    - at least 1 special symbol character 
- **When** I validate following passwords: { }
- **Then** validation result is VALID / INVALID

