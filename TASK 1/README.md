# Password Strength Checker

A beginner-friendly Python project that checks a password using its length and character types, then gives a strength rating and improvement suggestions.

## Features

- Checks whether the password has at least 8 characters.
- Recommends 12 or more characters.
- Checks for uppercase letters, lowercase letters, numbers, and special characters.
- Classifies the password as Very Weak, Weak, Moderate, Good, Strong, or Very Strong.
- Gives clear suggestions to improve a password.
- Uses Python's built-in libraries only; no third-party packages are required.
- Uses hidden terminal input (`getpass`) so the password is not displayed while typing.

## Project structure

```text
Password_Strength_Checker/
├── password_strength_checker.py
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── tests/
│   └── test_password_strength_checker.py
└── .github/
    └── workflows/
        └── python-tests.yml
```

## Requirements

- Python 3.8 or later
- No external Python packages

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python password_strength_checker.py
   ```

   On some Windows systems, use:

   ```powershell
   py password_strength_checker.py
   ```

4. Type a test password when prompted and press Enter. The typed characters will be hidden.

## Example result

```text
================================================
           PASSWORD STRENGTH CHECKER
================================================
Your password is checked locally and is not saved.

--- CHECK RESULTS ---
[PASS] At least 8 characters
[PASS] At least 12 characters (recommended)
[PASS] Contains an uppercase letter (A-Z)
[PASS] Contains a lowercase letter (a-z)
[PASS] Contains a number (0-9)
[PASS] Contains a special character

Strength: Very Strong
Score: 5/5
```

The example above is illustrative. Do not use example passwords for real accounts.

## How the program works

1. It receives a password through hidden terminal input.
2. It checks the password length and whether it contains uppercase, lowercase, numeric, and special characters.
3. It calculates a score from five basic checks. The 12-character recommendation is an additional bonus for the rating.
4. It displays the result and suggestions for any missing criteria.

## Run the tests

From the project folder, run:

```bash
python -m unittest discover -s tests -v
```

On Windows, `py -m unittest discover -s tests -v` also works.

## Security and limitations

- The program does not write the password to a file or send it over the internet.
- Only enter a sample/test password. Do not paste your real account password into a project or share it in screenshots.
- This is a basic educational checker. It does not check password breach databases, common-password lists, or estimate real-world cracking time.
- A long, unique passphrase is generally better than a short password with many character types. Use a password manager and never reuse passwords.

## Internship task

**Task:** Develop a Python program that evaluates password strength based on length, uppercase and lowercase letters, numbers, and special characters, and provides feedback to improve security.

**Completed deliverables:** Python source code, README documentation, automated unit tests, and a GitHub Actions workflow.
