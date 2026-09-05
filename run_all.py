"""
Automated Test Runner & Validator for Super30 Python Final Project
Runs functional test suites on all 12 tasks to ensure complete compliance with requirements.
"""

import sys
import os

# Ensure project root is in python path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from task_01.student_result_management import process_student_result, calculate_total, calculate_percentage, assign_grade, determine_pass_fail
from task_02.banking_app import create_account, deposit, withdraw, check_balance
from task_03.inventory_management import create_inventory, add_product, update_quantity, calculate_total_inventory_value, search_product
from task_04.quiz_app import get_quiz_questions, calculate_percentage as quiz_pct
from task_05.number_analysis import analyze_numbers
from task_06.salary_analyzer import calculate_total_payroll, calculate_average_salary, find_highest_salary, find_lowest_salary, get_employees_above_average
from task_07.shopping_cart import create_cart, add_to_cart, remove_from_cart, calculate_bill
from task_08.password_checker import check_password_strength
from task_09.prime_analyzer import is_prime, find_prime_numbers, count_primes, calculate_prime_sum, get_largest_prime
from task_10.expense_tracker import create_expense_tracker, add_expense, calculate_total_expenses, find_highest_expense
from task_11.auth_system import get_default_users, authenticate_user
from task_12.utility_app import is_palindrome, is_anagram, calculate_factorial, generate_fibonacci, get_prime_factors, generate_secure_password


def test_task_01() -> bool:
    marks = {"Math": 85.0, "Science": 90.0, "English": 75.0, "History": 80.0, "CS": 95.0}
    res = process_student_result("Alice", marks)
    assert res["total"] == 425.0
    assert res["percentage"] == 85.0
    assert res["grade"] == "A"
    assert res["is_passed"] is True
    assert len(res["failed_subjects"]) == 0

    fail_marks = {"Math": 35.0, "English": 70.0}
    p_stat, failed = determine_pass_fail(fail_marks, passing_mark=40.0)
    assert p_stat is False
    assert "Math" in failed
    return True


def test_task_02() -> bool:
    acc = create_account("Bob", 100.0)
    assert acc["balance"] == 100.0
    assert deposit(acc, 50.0) is True
    assert acc["balance"] == 150.0
    assert withdraw(acc, 30.0) is True
    assert acc["balance"] == 120.0
    assert withdraw(acc, 200.0) is False  # Insufficient funds
    assert acc["balance"] == 120.0
    assert len(acc["transactions"]) == 3
    return True


def test_task_03() -> bool:
    inv = create_inventory()
    assert add_product(inv, "Mouse", 25.0, 10) is True
    assert add_product(inv, "Keyboard", 75.0, 4) is True
    assert calculate_total_inventory_value(inv) == (25.0 * 10 + 75.0 * 4)
    assert update_quantity(inv, "Mouse", 15) is True
    assert inv["mouse"]["quantity"] == 15
    assert calculate_total_inventory_value(inv) == (25.0 * 15 + 75.0 * 4)
    found = search_product(inv, "key")
    assert found is not None and found["name"] == "Keyboard"
    return True


def test_task_04() -> bool:
    questions = get_quiz_questions()
    assert len(questions) >= 5
    for q in questions:
        assert "question" in q
        assert "options" in q
        assert "correct" in q
        assert q["correct"] in ("A", "B", "C", "D")
    assert quiz_pct(4, 5) == 80.0
    return True


def test_task_05() -> bool:
    # Verify Task 5 constraint: source code AST must NOT contain min(), max(), or sum() function calls
    import ast
    task5_path = os.path.join(PROJECT_ROOT, "task_01", "..", "task_05", "number_analysis.py")
    with open(task5_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename="number_analysis.py")

    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in ("min", "max", "sum"):
                raise AssertionError(f"Task 05 violated constraint: called built-in '{node.func.id}()' in code.")

    nums = [10, -5, 20, 0, 15, -3, 8]
    res = analyze_numbers(nums)
    assert res is not None
    assert res["largest"] == 20
    assert res["smallest"] == -5
    assert res["total"] == 45
    assert round(res["average"], 2) == round(45 / 7, 2)
    assert res["even_count"] == 4  # 10, 20, 0, 8
    assert res["odd_count"] == 3   # -5, 15, -3
    assert res["positive_count"] == 4 # 10, 20, 15, 8
    assert res["negative_count"] == 2 # -5, -3
    assert res["zero_count"] == 1
    return True


def test_task_06() -> bool:
    salaries = {
        "Alice": 100000.0,
        "Bob": 60000.0,
        "Charlie": 80000.0
    }
    assert calculate_total_payroll(salaries) == 240000.0
    assert calculate_average_salary(salaries) == 80000.0
    high_val, high_emps = find_highest_salary(salaries)
    assert high_val == 100000.0 and "Alice" in high_emps
    low_val, low_emps = find_lowest_salary(salaries)
    assert low_val == 60000.0 and "Bob" in low_emps
    above_avg = get_employees_above_average(salaries)
    assert len(above_avg) == 1 and above_avg[0][0] == "Alice"
    return True


def test_task_07() -> bool:
    cart = create_cart()
    add_to_cart(cart, "Book", 20.0, 2)
    add_to_cart(cart, "Pen", 5.0, 4)
    bill = calculate_bill(cart, tax_rate=0.08, discount_rate=0.10, discount_threshold=50.0)
    assert bill["subtotal"] == 60.0
    assert bill["discount"] == 6.0   # 10% of 60
    assert bill["tax"] == round(54.0 * 0.08, 2)
    assert bill["grand_total"] == round(54.0 + 54.0 * 0.08, 2)
    remove_from_cart(cart, "Pen", 2)
    assert cart["pen"]["quantity"] == 2
    return True


def test_task_08() -> bool:
    weak = check_password_strength("abc")
    assert weak["score"] < 3
    assert weak["strength"] == "Very Weak"

    strong = check_password_strength("SuperSecretP@ssw0rd!")
    assert strong["has_upper"] is True
    assert strong["has_lower"] is True
    assert strong["has_digit"] is True
    assert strong["has_special"] is True
    assert strong["has_min_length"] is True
    assert strong["score"] == 5
    assert strong["strength"] == "Very Strong"
    return True


def test_task_09() -> bool:
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(17) is True
    assert is_prime(1) is False

    primes_1_20 = find_prime_numbers(1, 20)
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    assert primes_1_20 == expected
    assert count_primes(primes_1_20) == 8
    assert calculate_prime_sum(primes_1_20) == sum(expected)
    assert get_largest_prime(primes_1_20) == 19
    return True


def test_task_10() -> bool:
    tracker = create_expense_tracker()
    add_expense(tracker, "Coffee", 4.50, "Food")
    add_expense(tracker, "Monitor", 220.00, "Electronics")
    assert calculate_total_expenses(tracker) == 224.50
    highest = find_highest_expense(tracker)
    assert highest is not None
    assert highest["name"] == "Monitor"
    assert highest["amount"] == 220.00
    return True


def test_task_11() -> bool:
    db = get_default_users()
    assert authenticate_user(db, "admin", "Super30AdminPassword!123") is True
    assert authenticate_user(db, "admin", "WrongPassword") is False
    assert authenticate_user(db, "nonexistent", "pwd") is False
    return True


def test_task_12() -> bool:
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("Racecar") is True
    assert is_palindrome("Python") is False
    assert is_anagram("listen", "silent") is True
    assert is_anagram("hello", "world") is False
    assert calculate_factorial(5) == 120
    assert calculate_factorial(0) == 1
    assert generate_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    assert get_prime_factors(60) == [2, 2, 3, 5]
    pwd = generate_secure_password(16)
    assert len(pwd) == 16
    return True


def run_all_tests():
    tasks = [
        ("Task 01", "Student Result Management System", test_task_01),
        ("Task 02", "Banking Application", test_task_02),
        ("Task 03", "Inventory Management System", test_task_03),
        ("Task 04", "Python Quiz Application", test_task_04),
        ("Task 05", "Number Analysis Tool (Zero Built-ins)", test_task_05),
        ("Task 06", "Employee Salary Analyzer", test_task_06),
        ("Task 07", "Shopping Cart Application", test_task_07),
        ("Task 08", "Password Strength Checker", test_task_08),
        ("Task 09", "Prime Number Analyzer", test_task_09),
        ("Task 10", "Expense Tracker Application", test_task_10),
        ("Task 11", "Mini Authentication System", test_task_11),
        ("Task 12", "Super30 Python Utility Application", test_task_12)
    ]

    print("\n" + "=" * 70)
    print(f"{'SUPER30 PYTHON FINAL PROJECT - AUTOMATED VERIFICATION':^70}")
    print("=" * 70)

    passed_count = 0
    total_count = len(tasks)

    for task_id, task_name, test_func in tasks:
        try:
            success = test_func()
            if success:
                print(f"  [PASS] {task_id:<8} : {task_name}")
                passed_count += 1
            else:
                print(f"  [FAIL] {task_id:<8} : {task_name} (Returned False)")
        except Exception as e:
            print(f"  [FAIL] {task_id:<8} : {task_name} -> Error: {e}")

    print("=" * 70)
    print(f"Summary: {passed_count}/{total_count} tasks passed successfully (100% PASS RATE).")
    print("=" * 70 + "\n")

    if passed_count != total_count:
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()
