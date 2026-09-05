"""
Task 08: Password Strength Checker
Objective:
    Create a function that checks whether a password satisfies:
    - Contains uppercase letter (A-Z)
    - Contains lowercase letter (a-z)
    - Contains numerical digit (0-9)
    - Contains special character (!@#$%^&*()_+-=[]{}|;:,.<>? etc.)
    - Minimum length of 8 characters

    Returns a meaningful strength score, categorical rating, and actionable feedback.
"""

from typing import Dict, List, Any


SPECIAL_CHARACTERS = set("!@#$%^&*()_+-=[]{}|;:,.<>?/`~\"'\\")


def check_password_strength(password: str) -> Dict[str, Any]:
    """
    Analyzes a password against standard cybersecurity complexity criteria using loops.

    Args:
        password (str): The password to test.

    Returns:
        Dict[str, Any]: Analysis containing:
            - 'has_upper': bool
            - 'has_lower': bool
            - 'has_digit': bool
            - 'has_special': bool
            - 'has_min_length': bool
            - 'length': int
            - 'score': int (0 to 5)
            - 'strength': str ('Very Weak', 'Weak', 'Moderate', 'Strong', 'Very Strong')
            - 'feedback': List[str] of suggestions
    """
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    length = len(password)
    has_min_length = length >= 8

    # Loop through each character to inspect properties
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in SPECIAL_CHARACTERS:
            has_special = True

    # Compute score (1 point per satisfied criterion)
    criteria_checks = [has_min_length, has_upper, has_lower, has_digit, has_special]
    score = 0
    for criterion in criteria_checks:
        if criterion:
            score += 1

    # Determine qualitative strength rating
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Generate actionable suggestions for missing requirements
    feedback: List[str] = []
    if not has_min_length:
        feedback.append(f"Increase length to at least 8 characters (currently {length}).")
    if not has_upper:
        feedback.append("Include at least one uppercase letter (A-Z).")
    if not has_lower:
        feedback.append("Include at least one lowercase letter (a-z).")
    if not has_digit:
        feedback.append("Include at least one numeric digit (0-9).")
    if not has_special:
        feedback.append("Include at least one special symbol (!@#$%^&* etc.).")

    return {
        "password": password,
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
        "has_min_length": has_min_length,
        "score": score,
        "strength": strength,
        "feedback": feedback
    }


def display_password_report(analysis: Dict[str, Any], mask_password: bool = False) -> None:
    """
    Displays a formatted security evaluation report.

    Args:
        analysis (Dict[str, Any]): Result dict from check_password_strength.
        mask_password (bool): Whether to mask the password for privacy.
    """
    raw_pwd = analysis["password"]
    display_pwd = "*" * len(raw_pwd) if mask_password else raw_pwd

    print("\n" + "=" * 60)
    print(f"{'PASSWORD STRENGTH SECURITY REPORT':^60}")
    print("=" * 60)
    print(f"Password Evaluated : {display_pwd}")
    print(f"Total Length       : {analysis['length']} characters")
    print(f"Overall Strength   : {analysis['strength'].upper()} (Score: {analysis['score']}/5)")
    print("-" * 60)
    print("Criteria Breakdown:")

    def mark(val: bool) -> str:
        return "[PASS] " if val else "[FAIL] "

    print(f"  {mark(analysis['has_min_length'])} Minimum 8 Characters")
    print(f"  {mark(analysis['has_upper'])} Contains Uppercase Letter (A-Z)")
    print(f"  {mark(analysis['has_lower'])} Contains Lowercase Letter (a-z)")
    print(f"  {mark(analysis['has_digit'])} Contains Numeric Digit (0-9)")
    print(f"  {mark(analysis['has_special'])} Contains Special Character (!@#$...)")

    if analysis["feedback"]:
        print("-" * 60)
        print("Recommendations to Improve:")
        for tip in analysis["feedback"]:
            print(f"  * {tip}")
    else:
        print("-" * 60)
        print("[+] Outstanding! Your password satisfies all security standards.")

    print("=" * 60 + "\n")


def main():
    """Interactive password strength evaluator."""
    print("=== Super30 Password Security & Strength Checker ===")
    
    # Run test samples
    samples = ["admin", "password123", "SuperSecret!", "Tr0ub4dor&3"]
    print("Running initial evaluations on sample passwords:")
    for sample in samples:
        report = check_password_strength(sample)
        print(f"  • '{sample}' -> Strength: {report['strength']} (Score: {report['score']}/5)")

    print("\nTry your own passwords:")
    while True:
        pwd = input("\nEnter a password to test (or 'exit' to quit): ").strip()
        if pwd.lower() == 'exit':
            print("Exiting Password Strength Checker. Stay secure!")
            break
        if not pwd:
            print("[!] Password cannot be empty.")
            continue

        report = check_password_strength(pwd)
        display_password_report(report)


if __name__ == "__main__":
    main()
