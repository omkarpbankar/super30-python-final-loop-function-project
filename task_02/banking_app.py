"""
Task 02: Banking Application
Objective:
    Create a menu-driven banking program supporting:
    - Check balance
    - Deposit money
    - Withdraw money
    - Transaction history log
    - Exit
    Uses functions for each operation and a while loop for the application menu.
"""

from datetime import datetime
from typing import Dict, List, Any


def create_account(account_holder: str, initial_balance: float = 0.0) -> Dict[str, Any]:
    """
    Initializes a new bank account structure.

    Args:
        account_holder (str): Name of the account holder.
        initial_balance (float): Starting balance. Must be >= 0.

    Returns:
        Dict[str, Any]: Account data dictionary.
    """
    if initial_balance < 0:
        raise ValueError("Initial balance cannot be negative.")

    account: Dict[str, Any] = {
        "holder": account_holder,
        "balance": float(initial_balance),
        "transactions": []
    }
    if initial_balance > 0:
        account["transactions"].append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": "INITIAL_DEPOSIT",
            "amount": float(initial_balance),
            "balance": float(initial_balance)
        })
    return account


def check_balance(account: Dict[str, Any]) -> float:
    """
    Returns and prints the current account balance.

    Args:
        account (Dict[str, Any]): The bank account dictionary.

    Returns:
        float: Current balance.
    """
    balance = account["balance"]
    print(f"\n[i] Current Account Balance for {account['holder']}: ${balance:,.2f}")
    return balance


def deposit(account: Dict[str, Any], amount: float) -> bool:
    """
    Deposits a positive amount into the account and logs the transaction.

    Args:
        account (Dict[str, Any]): The bank account.
        amount (float): Amount to deposit.

    Returns:
        bool: True if successful, False otherwise.
    """
    if amount <= 0:
        print("\n[!] Deposit Error: Amount must be greater than zero.")
        return False

    account["balance"] += amount
    account["transactions"].append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": "DEPOSIT",
        "amount": amount,
        "balance": account["balance"]
    })
    print(f"\n[+] Successfully deposited ${amount:,.2f}.")
    print(f"    New Balance: ${account['balance']:,.2f}")
    return True


def withdraw(account: Dict[str, Any], amount: float) -> bool:
    """
    Withdraws funds from the account if sufficient balance is available.

    Args:
        account (Dict[str, Any]): The bank account.
        amount (float): Amount to withdraw.

    Returns:
        bool: True if successful, False otherwise.
    """
    if amount <= 0:
        print("\n[!] Withdrawal Error: Amount must be greater than zero.")
        return False

    if amount > account["balance"]:
        print(f"\n[!] Withdrawal Error: Insufficient funds.")
        print(f"    Requested: ${amount:,.2f} | Available Balance: ${account['balance']:,.2f}")
        return False

    account["balance"] -= amount
    account["transactions"].append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": "WITHDRAWAL",
        "amount": amount,
        "balance": account["balance"]
    })
    print(f"\n[-] Successfully withdrew ${amount:,.2f}.")
    print(f"    New Balance: ${account['balance']:,.2f}")
    return True


def view_transaction_history(account: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Displays the chronological transaction history for the account.

    Args:
        account (Dict[str, Any]): The bank account.

    Returns:
        List[Dict[str, Any]]: List of recorded transaction dicts.
    """
    transactions = account.get("transactions", [])
    print("\n" + "=" * 65)
    print(f"TRANSACTION HISTORY FOR: {account['holder']}")
    print("=" * 65)
    if not transactions:
        print("No transactions recorded yet.")
    else:
        print(f"{'#':<4} {'Date & Time':<20} {'Type':<16} {'Amount':<12} {'Balance':<12}")
        print("-" * 65)
        for idx, txn in enumerate(transactions, start=1):
            sign = "+" if txn["type"] in ("DEPOSIT", "INITIAL_DEPOSIT") else "-"
            amt_str = f"{sign}${txn['amount']:,.2f}"
            bal_str = f"${txn['balance']:,.2f}"
            print(f"{idx:<4} {txn['timestamp']:<20} {txn['type']:<16} {amt_str:<12} {bal_str:<12}")
    print("=" * 65 + "\n")
    return transactions


def banking_menu(account: Dict[str, Any]) -> None:
    """
    Runs the interactive menu loop for banking operations.

    Args:
        account (Dict[str, Any]): Active account.
    """
    while True:
        print("\n" + "-" * 40)
        print(f"  SUPER30 SECURE BANKING PORTAL")
        print(f"  Logged in as: {account['holder']}")
        print("-" * 40)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit Application")
        print("-" * 40)

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            check_balance(account)
        elif choice == '2':
            try:
                amt_str = input("Enter amount to deposit ($): ").strip()
                amt = float(amt_str)
                deposit(account, amt)
            except ValueError:
                print("\n[!] Invalid input. Please enter a valid numerical amount.")
        elif choice == '3':
            try:
                amt_str = input("Enter amount to withdraw ($): ").strip()
                amt = float(amt_str)
                withdraw(account, amt)
            except ValueError:
                print("\n[!] Invalid input. Please enter a valid numerical amount.")
        elif choice == '4':
            view_transaction_history(account)
        elif choice == '5':
            print(f"\nThank you for banking with Super30, {account['holder']}. Goodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 1 and 5.")


def main():
    """Initializes a bank session with user-defined or default account."""
    print("Welcome to Super30 Banking System")
    name = input("Enter account holder name: ").strip()
    if not name:
        name = "Guest User"

    while True:
        init_bal_input = input("Enter starting balance ($) [Default: 0]: ").strip()
        if not init_bal_input:
            init_bal = 0.0
            break
        try:
            init_bal = float(init_bal_input)
            if init_bal < 0:
                print("[!] Starting balance cannot be negative.")
                continue
            break
        except ValueError:
            print("[!] Please enter a valid numerical amount.")

    account = create_account(name, init_bal)
    banking_menu(account)


if __name__ == "__main__":
    main()
