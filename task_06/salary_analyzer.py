"""
Task 06: Employee Salary Analyzer
Objective:
    Given a dataset of employee salaries, create functions to determine:
    - Total payroll expenditure
    - Average salary across the company
    - Highest earning salary and corresponding employee(s)
    - Lowest earning salary and corresponding employee(s)
    - List of employees earning above average
"""

from typing import Dict, List, Tuple, Union, Optional


def calculate_total_payroll(salaries: Dict[str, float]) -> float:
    """
    Calculates total company payroll expense using a loop.

    Args:
        salaries (Dict[str, float]): Map of employee name to salary.

    Returns:
        float: Total payroll amount.
    """
    total = 0.0
    for salary in salaries.values():
        total += salary
    return round(total, 2)


def calculate_average_salary(salaries: Dict[str, float]) -> float:
    """
    Calculates average employee salary.

    Args:
        salaries (Dict[str, float]): Map of employee name to salary.

    Returns:
        float: Average salary.
    """
    if not salaries:
        return 0.0
    total = calculate_total_payroll(salaries)
    return round(total / len(salaries), 2)


def find_highest_salary(salaries: Dict[str, float]) -> Optional[Tuple[float, List[str]]]:
    """
    Finds the highest salary amount and the employees receiving it.

    Args:
        salaries (Dict[str, float]): Map of employee name to salary.

    Returns:
        Optional[Tuple[float, List[str]]]: (Highest salary, List of top earners).
    """
    if not salaries:
        return None

    highest_val: Optional[float] = None
    for salary in salaries.values():
        if highest_val is None or salary > highest_val:
            highest_val = salary

    top_earners: List[str] = []
    for emp, sal in salaries.items():
        if sal == highest_val:
            top_earners.append(emp)

    return (highest_val, top_earners)


def find_lowest_salary(salaries: Dict[str, float]) -> Optional[Tuple[float, List[str]]]:
    """
    Finds the lowest salary amount and the employees receiving it.

    Args:
        salaries (Dict[str, float]): Map of employee name to salary.

    Returns:
        Optional[Tuple[float, List[str]]]: (Lowest salary, List of lowest earners).
    """
    if not salaries:
        return None

    lowest_val: Optional[float] = None
    for salary in salaries.values():
        if lowest_val is None or salary < lowest_val:
            lowest_val = salary

    lowest_earners: List[str] = []
    for emp, sal in salaries.items():
        if sal == lowest_val:
            lowest_earners.append(emp)

    return (lowest_val, lowest_earners)


def get_employees_above_average(salaries: Dict[str, float]) -> List[Tuple[str, float]]:
    """
    Filters and returns employees whose salary exceeds the average salary.

    Args:
        salaries (Dict[str, float]): Map of employee name to salary.

    Returns:
        List[Tuple[str, float]]: List of (Employee Name, Salary) tuples earning > average.
    """
    if not salaries:
        return []

    avg_salary = calculate_average_salary(salaries)
    above_avg: List[Tuple[str, float]] = []

    for emp, sal in salaries.items():
        if sal > avg_salary:
            above_avg.append((emp, sal))

    return above_avg


def display_salary_report(salaries: Dict[str, float]) -> None:
    """
    Prints a detailed analytical payroll report.

    Args:
        salaries (Dict[str, float]): Map of employee name to salary.
    """
    print("\n" + "=" * 65)
    print(f"{'EMPLOYEE PAYROLL & SALARY ANALYSIS':^65}")
    print("=" * 65)

    if not salaries:
        print("[!] No employee data available.")
        print("=" * 65 + "\n")
        return

    total = calculate_total_payroll(salaries)
    avg = calculate_average_salary(salaries)
    high_res = find_highest_salary(salaries)
    low_res = find_lowest_salary(salaries)
    above_avg_list = get_employees_above_average(salaries)

    print(f"{'Employee Name':<35} | {'Annual Salary ($)':<25}")
    print("-" * 65)
    for emp, sal in salaries.items():
        above_flag = " (Above Avg)" if sal > avg else ""
        print(f"{emp:<35} | ${sal:>12,.2f}{above_flag}")

    print("-" * 65)
    print(f"Total Headcount         : {len(salaries)} employees")
    print(f"Total Payroll Expense   : ${total:,.2f}")
    print(f"Average Salary          : ${avg:,.2f}")

    if high_res:
        highest_amt, high_emps = high_res
        print(f"Highest Salary          : ${highest_amt:,.2f} ({', '.join(high_emps)})")

    if low_res:
        lowest_amt, low_emps = low_res
        print(f"Lowest Salary           : ${lowest_amt:,.2f} ({', '.join(low_emps)})")

    print(f"Employees Above Average : {len(above_avg_list)} / {len(salaries)}")
    for emp, sal in above_avg_list:
        diff = sal - avg
        print(f"   * {emp}: ${sal:,.2f} (+${diff:,.2f} over avg)")

    print("=" * 65 + "\n")


def main():
    """Interactive loop for adding employees and generating payroll reports."""
    # Seed sample corporate roster
    roster: Dict[str, float] = {
        "Omkar Bankar": 125000.0,
        "Alice Johnson": 92000.0,
        "Bob Smith": 65000.0,
        "Charlie Brown": 48000.0,
        "Diana Prince": 140000.0,
        "Ethan Hunt": 88000.0,
        "Fiona Gallagher": 72500.0
    }

    print("=== Super30 Employee Salary Analyzer ===")
    display_salary_report(roster)

    while True:
        print("\nOptions: [1] Add/Update Employee [2] View Report [3] Clear All [4] Exit")
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            name = input("Enter employee name: ").strip()
            if not name:
                print("[!] Name cannot be empty.")
                continue
            try:
                salary = float(input(f"Enter annual salary for {name} ($): ").strip())
                if salary < 0:
                    print("[!] Salary cannot be negative.")
                    continue
                roster[name] = salary
                print(f"[+] Recorded {name} with salary ${salary:,.2f}.")
            except ValueError:
                print("[!] Invalid number format for salary.")

        elif choice == '2':
            display_salary_report(roster)

        elif choice == '3':
            confirm = input("Are you sure you want to clear all data? (y/n): ").strip().lower()
            if confirm == 'y':
                roster.clear()
                print("[+] Roster cleared.")

        elif choice == '4':
            print("Exiting Salary Analyzer. Goodbye!")
            break
        else:
            print("[!] Invalid option. Choose between 1 and 4.")


if __name__ == "__main__":
    main()
