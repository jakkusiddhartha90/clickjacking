"""A simple, local password strength checker.

The password is checked in memory only. This program does not save or transmit it.
"""
import getpass
import re


def analyze_password(password: str) -> dict:
    """Return a strength rating, score, checks, and improvement suggestions."""
    checks = {
        "At least 8 characters": len(password) >= 8,
        "At least 12 characters (recommended)": len(password) >= 12,
        "Contains an uppercase letter (A-Z)": bool(re.search(r"[A-Z]", password)),
        "Contains a lowercase letter (a-z)": bool(re.search(r"[a-z]", password)),
        "Contains a number (0-9)": bool(re.search(r"\d", password)),
        "Contains a special character": bool(re.search(r"[^A-Za-z0-9]", password)),
    }

    # The 12-character check is a bonus; the other five checks form the score.
    scored_checks = [
        checks["At least 8 characters"],
        checks["Contains an uppercase letter (A-Z)"],
        checks["Contains a lowercase letter (a-z)"],
        checks["Contains a number (0-9)"],
        checks["Contains a special character"],
    ]
    score = sum(scored_checks)

    if score == 5 and checks["At least 12 characters (recommended)"]:
        strength = "Very Strong"
    elif score == 5:
        strength = "Strong"
    elif score >= 4:
        strength = "Good"
    elif score >= 3:
        strength = "Moderate"
    elif score >= 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    suggestions = []
    if not checks["At least 8 characters"]:
        suggestions.append("Use at least 8 characters; 12 or more is recommended.")
    elif not checks["At least 12 characters (recommended)"]:
        suggestions.append("Make it 12 characters or longer for better protection.")
    if not checks["Contains an uppercase letter (A-Z)"]:
        suggestions.append("Add at least one uppercase letter (A-Z).")
    if not checks["Contains a lowercase letter (a-z)"]:
        suggestions.append("Add at least one lowercase letter (a-z).")
    if not checks["Contains a number (0-9)"]:
        suggestions.append("Add at least one number (0-9).")
    if not checks["Contains a special character"]:
        suggestions.append("Add a special character, such as !, @, #, or %.")
    if not suggestions:
        suggestions.append("Good work. Use a unique password and consider a password manager.")

    return {
        "strength": strength,
        "score": score,
        "maximum_score": len(scored_checks),
        "checks": checks,
        "suggestions": suggestions,
    }


def main() -> None:
    print("=" * 48)
    print("           PASSWORD STRENGTH CHECKER")
    print("=" * 48)
    print("Your password is checked locally and is not saved.")
    password = getpass.getpass("\nEnter a password to check: ")

    if not password:
        print("\nNo password entered. Please run the program again.")
        return

    result = analyze_password(password)
    print("\n--- CHECK RESULTS ---")
    for label, passed in result["checks"].items():
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")

    print(f"\nStrength: {result['strength']}")
    print(f"Score: {result['score']}/{result['maximum_score']}")
    print("\nSuggestions:")
    for suggestion in result["suggestions"]:
        print(f"- {suggestion}")
    print("\nNote: This is a basic educational checker, not a guarantee")
    print("that a password is safe from guessing or data breaches.")


if __name__ == "__main__":
    main()
