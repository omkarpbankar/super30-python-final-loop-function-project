"""
Task 10: Expense Tracker Application
Objective:
    Create a menu-driven personal finance application allowing users to:
    - Add an expense (Name/Description, Category, Amount)
    - View all recorded expenses in a formatted table
    - Calculate total expenditure
    - Find and highlight the highest expense recorded
    - Exit
    Application loops continuously until the user explicitly selects Exit.
"""

from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple


def create_expense_tracker() -> List[Dict[str, Any]]:
    """
    Initializes a new expense list storage.

    Returns:
        List[Dict[str, Any]]: List of expense records.
    """
    return []


def add_expense(
    expenses: List[Dict[str, Any]],
    name: str,
    amount: float,
    category: str = "General"
) -> bool:
    """
    Adds a new expense entry with timestamp.

    Args:
        expenses (List[Dict[str, Any]]): Expense record list.
        name (str): Expense description.
        amount (float): Cost amount (must be > 0).
        category (str): Expense category (e.g. Food, Travel, Utilities, Books).

    Returns:
        bool: True if recorded successfully, False otherwise.
    """
    clean_name = name.strip()
    clean_cat = category.strip() if category.strip() else "General"

    if not clean_name:
        print("[!] Error: Expense name/description cannot be empty.")
        return False
    if amount <= 0:
        print("[!] Error: Expense amount must be greater than 0.")
        return False

    entry = {
        "id": len(expenses) + 1,
        "name": clean_name,
        "category": clean_cat,
        "amount": round(float(amount), 2),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    expenses.append(entry)
    print(f"[+] Recorded expense '{clean_name}' [${amount:.2f}] under '{clean_cat}'.")
    return True


def view_expenses(expenses: List[Dict[str, Any]]) -> None:
    """
    Displays all logged expenses in a clean formatted ledger.

    Args:
        expenses (List[Dict[str, Any]]): Expense record list.
    """
    print("\n" + "=" * 70)
    print(f"{'EXPENSE LEDGER & HISTORY':^70}")
    print("=" * 70)

    if not expenses:
        print("  No expenses recorded yet.")
        print("=" * 70 + "\n")
        return

    print(f"{'#':<4} {'Date & Time':<18} {'Category':<16} {'Description':<20} {'Amount ($)':<10}")
    print("-" * 70)
    total = 0.0
    for idx, item in enumerate(expenses, start=1):
        total += item["amount"]
        print(f"{idx:<4} {item['timestamp']:<18} {item['category']:<16} {item['name']:<20} ${item['amount']:>8.2f}")

    print("-" * 70)
    print(f"{'TOTAL EXPENDITURE:':<60} ${total:>8.2f}")
    print("=" * 70 + "\n")


def calculate_total_expenses(expenses: List[Dict[str, Any]]) -> float:
    """
    Calculates the sum of all expenses using a loop.

    Args:
        expenses (List[Dict[str, Any]]): Expense record list.

    Returns:
        float: Cumulative expense amount.
    """
    total = 0.0
    for item in expenses:
        total += item["amount"]
    return round(total, 2)


def find_highest_expense(expenses: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """
    Finds the single highest recorded expense record using a loop.

    Args:
        expenses (List[Dict[str, Any]]): Expense record list.

    Returns:
        Optional[Dict[str, Any]]: Highest expense record or None if list is empty.
    """
    if not expenses:
        return None

    highest_entry = expenses[0]
    for item in expenses:
        if item["amount"] > highest_entry["amount"]:
            highest_entry = item
    return highest_entry


def expense_tracker_menu(expenses: List[Dict[str, Any]]) -> None:
    """Main interactive menu loop for the Expense Tracker."""
    while True:
        print("\n" + "-" * 40)
        print("     SUPER30 EXPENSE TRACKER")
        print("-" * 40)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenditure")
        print("4. Find Highest Expense")
        print("5. Exit")
        print("-" * 40)

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            name = input("Enter expense description / name: ").strip()
            cat = input("Enter category (e.g. Food, Utilities, Transport, Study): ").strip()
            try:
                amt = float(input("Enter amount ($): ").strip())
                add_expense(expenses, name, amt, cat)
            except ValueError:
                print("[!] Invalid amount format. Please enter a valid number.")

        elif choice == '2':
            view_expenses(expenses)

        elif choice == '3':
            total = calculate_total_expenses(expenses)
            print(f"\n[i] Total Cumulative Expenses: ${total:,.2f} across {len(expenses)} transactions.")

        elif choice == '4':
            highest = find_highest_expense(expenses)
            if highest is None:
                print("\n[!] No expenses have been recorded yet.")
            else:
                print("\n" + "*" * 50)
                print(f"HIGHEST EXPENSE: {highest['name']}")
                print(f"Amount   : ${highest['amount']:,.2f}")
                print(f"Category : {highest['category']}")
                print(f"Date     : {highest['timestamp']}")
                print("*" * 50)

        elif choice == '5':
            print("\nExiting Expense Tracker. Happy budgeting!")
            break
        else:
            print("[!] Invalid choice. Please enter a number between 1 and 5.")


def main():
    """Initializes with sample expenses and launches menu."""
    tracker = create_expense_tracker()
    # Add seed data
    add_expense(tracker, "Python Course Book", 45.00, "Education")
    add_expense(tracker, "Grocery Shopping", 128.75, "Food")
    add_expense(tracker, "Electricity Bill", 85.20, "Utilities")
    add_expense(tracker, "Office Ergonomic Chair", 249.99, "Furniture")

    expense_tracker_menu(tracker)


if __name__ == "__main__":
    main()
