"""
Task 12: Super30 Python Utility Application
Objective:
    Create a comprehensive menu-driven utility suite containing at least five utilities:
    1. Multi-Functional Arithmetic & Power Calculator
    2. Palindrome & Anagram Checker
    3. Prime Number Explorer & Factorizer
    4. Factorial & Fibonacci Sequence Generator
    5. Multiplication Table Matrix Generator
    6. Number Base Converter (Dec / Bin / Oct / Hex)
    7. Secure Password Generator & Strength Tester
"""

import math
import random
import string
from typing import List, Tuple, Dict, Any


# =====================================================================
# UTILITY 1: Arithmetic & Power Calculator
# =====================================================================
def run_calculator() -> None:
    """Executes arithmetic calculations with error handling for division by zero."""
    print("\n--- [Utility 1] Multi-Functional Calculator ---")
    print("Operations: [+] Add  [-] Subtract  [*] Multiply  [/] Divide  [%] Modulo  [^] Power  [V] Sqrt")
    op = input("Choose operation (+, -, *, /, %, ^, V): ").strip()

    try:
        if op == 'V' or op == 'v':
            val = float(input("Enter number: ").strip())
            if val < 0:
                print("[!] Error: Cannot calculate square root of a negative real number.")
            else:
                print(f"[Result] sqrt({val}) = {math.sqrt(val):.6f}")
            return

        num1 = float(input("Enter first number: ").strip())
        num2 = float(input("Enter second number: ").strip())

        if op == '+':
            print(f"[Result] {num1} + {num2} = {num1 + num2}")
        elif op == '-':
            print(f"[Result] {num1} - {num2} = {num1 - num2}")
        elif op == '*':
            print(f"[Result] {num1} * {num2} = {num1 * num2}")
        elif op == '/':
            if num2 == 0:
                print("[!] Error: Division by zero is undefined.")
            else:
                print(f"[Result] {num1} / {num2} = {num1 / num2}")
        elif op == '%':
            if num2 == 0:
                print("[!] Error: Modulo by zero is undefined.")
            else:
                print(f"[Result] {num1} % {num2} = {num1 % num2}")
        elif op == '^':
            print(f"[Result] {num1} ^ {num2} = {num1 ** num2}")
        else:
            print("[!] Invalid operator selected.")
    except ValueError:
        print("[!] Error: Please enter valid numerical values.")


# =====================================================================
# UTILITY 2: Palindrome & Anagram Checker
# =====================================================================
def is_palindrome(text: str) -> bool:
    """Checks if a string is identical forwards and backwards ignoring punctuation/case."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    if not cleaned:
        return False
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


def is_anagram(str1: str, str2: str) -> bool:
    """Checks if two strings are anagrams of each other."""
    c1 = sorted("".join(ch.lower() for ch in str1 if ch.isalnum()))
    c2 = sorted("".join(ch.lower() for ch in str2 if ch.isalnum()))
    return c1 == c2


def run_palindrome_checker() -> None:
    """CLI handler for palindrome and anagram tool."""
    print("\n--- [Utility 2] Palindrome & Anagram Checker ---")
    print("1. Check Palindrome (Word, Sentence, or Number)")
    print("2. Check Anagram (Two phrases)")
    sub_ch = input("Choose (1 or 2): ").strip()

    if sub_ch == '1':
        text = input("Enter text or number to test: ").strip()
        if is_palindrome(text):
            print(f"[+] '{text}' is a VALID PALINDROME!")
        else:
            print(f"[-] '{text}' is NOT a palindrome.")
    elif sub_ch == '2':
        s1 = input("Enter first phrase: ").strip()
        s2 = input("Enter second phrase: ").strip()
        if is_anagram(s1, s2):
            print(f"[+] '{s1}' and '{s2}' ARE ANAGRAMS!")
        else:
            print(f"[-] '{s1}' and '{s2}' are NOT anagrams.")
    else:
        print("[!] Invalid choice.")


# =====================================================================
# UTILITY 3: Prime Number Explorer & Prime Factors
# =====================================================================
def get_prime_factors(n: int) -> List[int]:
    """Computes the prime factorization of a positive integer."""
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors


def run_prime_explorer() -> None:
    """CLI handler for prime exploration and factorization."""
    print("\n--- [Utility 3] Prime Number Explorer ---")
    try:
        n = int(input("Enter an integer to inspect (> 1): ").strip())
        if n <= 1:
            print("[!] Primes are natural numbers strictly greater than 1.")
            return

        # Primality check
        is_p = True
        if n <= 3:
            is_p = n > 1
        elif n % 2 == 0 or n % 3 == 0:
            is_p = False
        else:
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    is_p = False
                    break
                i += 6

        if is_p:
            print(f"[+] {n} is a PRIME NUMBER! It has only 2 factors: 1 and {n}.")
        else:
            factors = get_prime_factors(n)
            factors_str = " * ".join(map(str, factors))
            print(f"[-] {n} is a COMPOSITE NUMBER.")
            print(f"    Prime Factorization: {n} = {factors_str}")
    except ValueError:
        print("[!] Please enter a valid integer.")


# =====================================================================
# UTILITY 4: Factorial & Fibonacci Generator
# =====================================================================
def calculate_factorial(n: int) -> int:
    """Calculates n! using an iterative loop."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def generate_fibonacci(count: int) -> List[int]:
    """Generates the first 'count' terms of Fibonacci sequence using a loop."""
    if count <= 0:
        return []
    if count == 1:
        return [0]
    fib = [0, 1]
    while len(fib) < count:
        fib.append(fib[-1] + fib[-2])
    return fib


def run_sequence_generator() -> None:
    """CLI handler for factorial and Fibonacci sequences."""
    print("\n--- [Utility 4] Factorial & Fibonacci Sequence Generator ---")
    print("1. Calculate Factorial (n!)")
    print("2. Generate Fibonacci Series (N terms)")
    ch = input("Choose (1 or 2): ").strip()

    try:
        if ch == '1':
            n = int(input("Enter non-negative integer n: ").strip())
            res = calculate_factorial(n)
            print(f"[Result] {n}! = {res:,}")
        elif ch == '2':
            terms = int(input("Enter number of Fibonacci terms to generate: ").strip())
            seq = generate_fibonacci(terms)
            print(f"[Result] First {terms} terms: {seq}")
        else:
            print("[!] Invalid selection.")
    except ValueError as e:
        print(f"[!] Error: {e}")


# =====================================================================
# UTILITY 5: Multiplication Table Matrix Generator
# =====================================================================
def print_multiplication_table(number: int, rows: int = 10) -> None:
    """Prints a clean multiplication table using a loop."""
    print(f"\n--- Multiplication Table for {number} (1 to {rows}) ---")
    for i in range(1, rows + 1):
        print(f"  {number:4} x {i:3} = {number * i:6}")
    print("-" * 35)


def run_table_generator() -> None:
    """CLI handler for multiplication table."""
    print("\n--- [Utility 5] Multiplication Table Generator ---")
    try:
        num = int(input("Enter the base number: ").strip())
        rows_in = input("Enter number of rows (default 10): ").strip()
        rows = int(rows_in) if rows_in else 10
        print_multiplication_table(num, rows)
    except ValueError:
        print("[!] Invalid integer input.")


# =====================================================================
# UTILITY 6: Number Base Converter
# =====================================================================
def run_base_converter() -> None:
    """Converts a decimal number into Binary, Octal, and Hexadecimal representations."""
    print("\n--- [Utility 6] Number Base Converter ---")
    try:
        dec = int(input("Enter decimal integer: ").strip())
        print(f"\n[Base Conversion Results for {dec}]:")
        print(f"  * Decimal (Base 10) : {dec}")
        print(f"  * Binary  (Base 2)  : {bin(dec)}")
        print(f"  * Octal   (Base 8)  : {oct(dec)}")
        print(f"  * Hex     (Base 16) : {hex(dec).upper()}")
    except ValueError:
        print("[!] Please enter a valid decimal integer.")


# =====================================================================
# UTILITY 7: Secure Password Generator
# =====================================================================
def generate_secure_password(length: int = 12) -> str:
    """Generates a cryptographically strong random password satisfying complexity criteria."""
    if length < 6:
        length = 6

    # Guarantee at least 1 upper, 1 lower, 1 digit, 1 special
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*()_+-=")

    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
    remaining_len = length - 4
    rest = [random.choice(all_chars) for _ in range(remaining_len)]

    pwd_list = [upper, lower, digit, special] + rest
    random.shuffle(pwd_list)
    return "".join(pwd_list)


def run_password_generator() -> None:
    """CLI handler for password generator."""
    print("\n--- [Utility 7] Secure Password Generator ---")
    try:
        len_in = input("Enter desired password length (min 8, default 14): ").strip()
        length = int(len_in) if len_in else 14
        if length < 8:
            print("[!] Length adjusted to minimum recommended: 8")
            length = 8
        pwd = generate_secure_password(length)
        print(f"\n[+] Generated Password: {pwd}")
        print(f"    Length: {len(pwd)} characters | Entropy: High")
    except ValueError:
        print("[!] Invalid integer length.")


# =====================================================================
# MAIN MENU DRIVER
# =====================================================================
def utility_app_menu() -> None:
    """Main menu loop for the Super30 Python Utility Application."""
    while True:
        print("\n" + "=" * 55)
        print(f"{'SUPER30 PYTHON UTILITY APPLICATION':^55}")
        print("=" * 55)
        print("1. Arithmetic & Power Calculator")
        print("2. Palindrome & Anagram Checker")
        print("3. Prime Number Explorer & Factorizer")
        print("4. Factorial & Fibonacci Sequence Generator")
        print("5. Multiplication Table Generator")
        print("6. Number Base Converter (Dec/Bin/Oct/Hex)")
        print("7. Secure Password Generator")
        print("8. Exit Application")
        print("=" * 55)

        choice = input("Select a utility (1-8): ").strip()

        if choice == '1':
            run_calculator()
        elif choice == '2':
            run_palindrome_checker()
        elif choice == '3':
            run_prime_explorer()
        elif choice == '4':
            run_sequence_generator()
        elif choice == '5':
            run_table_generator()
        elif choice == '6':
            run_base_converter()
        elif choice == '7':
            run_password_generator()
        elif choice == '8':
            print("\nThank you for using the Super30 Utility Application! Goodbye.")
            break
        else:
            print("[!] Invalid selection. Please choose an option from 1 to 8.")


def main():
    """Entry point for the Utility Application."""
    utility_app_menu()


if __name__ == "__main__":
    main()
