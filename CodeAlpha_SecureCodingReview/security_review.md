# CodeAlpha Task 3 – Secure Coding Review

## Project overview
This project compares an intentionally vulnerable Python Flask login application
with a corrected educational implementation.

## Environment
- Operating system: Windows 11
- Language: Python 3
- Framework: Flask
- Database: SQLite
- Password hashing: Werkzeug

## Findings

### 1. SQL Injection
**Vulnerable behavior:** The vulnerable app builds SQL using string concatenation.
**Impact:** Crafted input can change query logic and bypass authentication.
**Remediation:** Use parameterized SQL statements. The secure app uses `?` placeholders.

### 2. Plaintext password storage
**Vulnerable behavior:** Passwords are stored directly in the database.
**Impact:** A database disclosure exposes original passwords.
**Remediation:** Store password hashes using `generate_password_hash()` and verify
with `check_password_hash()`.

### 3. Hardcoded credentials
**Vulnerable behavior:** The vulnerable demo contains a fixed test username/password.
**Impact:** Embedded credentials can be discovered in source code.
**Remediation:** Never embed real credentials. Use secure account provisioning and
managed secrets. The demo credentials are only for local testing.

### 4. Weak input validation
**Vulnerable behavior:** The vulnerable login accepts unrestricted input.
**Impact:** Unexpected input can reach sensitive operations without validation.
**Remediation:** Validate usernames and enforce password length limits.

### 5. Information disclosure
**Vulnerable behavior:** The vulnerable app returns database exception details.
**Impact:** Internal implementation details may be exposed.
**Remediation:** Return generic client errors and log details server-side.

### 6. Secret management
**Secure behavior:** The secure app requires `FLASK_SECRET_KEY` from the environment.
**Remediation:** Use a strong, unique secret managed outside source control.

## Test record
Complete this table with your actual results after running the applications.

| Test | Expected observation |
|---|---|
| Vulnerable normal login | Demo account can log in |
| Vulnerable SQL injection | Demonstrates authentication bypass |
| Secure registration | Valid new account is created |
| Secure normal login | Correct credentials succeed |
| Secure SQL injection input | Rejected; does not bypass authentication |
| Password database check | Secure database stores a hash, not the original password |

## Limitations
This is an educational demonstration, not a production-ready authentication system.
A real deployment also needs CSRF protection, rate limiting, HTTPS, secure session
management, account recovery controls, and operational security review.

## Safety
Run both applications only on localhost and only test systems you own or are
authorized to assess. Do not expose the vulnerable app to a public network.
