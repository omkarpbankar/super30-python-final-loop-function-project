"""
Task 11: Mini Authentication System
Objective:
    Create a robust, secure authentication program supporting:
    - Predefined user credentials database
    - Maximum login attempts (account lockout protection)
    - Successful login handling & protected session dashboard
    - Failed login tracking & attempt countdown
    - Logout and return to main screen
    - Dynamic retry logic using functions and loops
"""

from typing import Dict, Optional


def get_default_users() -> Dict[str, Dict[str, str]]:
    """
    Returns initial predefined user credentials with roles and full names.

    Returns:
        Dict[str, Dict[str, str]]: User database mapping username to record.
    """
    return {
        "admin": {
            "password": "Super30AdminPassword!123",
            "full_name": "System Administrator",
            "role": "Admin"
        },
        "omkar": {
            "password": "PythonMaster2026$",
            "full_name": "Omkar Bankar",
            "role": "Developer"
        },
        "student": {
            "password": "LearnPython#99",
            "full_name": "Super30 Student",
            "role": "Member"
        }
    }


def authenticate_user(
    users_db: Dict[str, Dict[str, str]],
    username: str,
    password: str
) -> bool:
    """
    Validates username and password credentials against the user database.

    Args:
        users_db (Dict[str, Dict[str, str]]): Registered users store.
        username (str): Entered username.
        password (str): Entered password.

    Returns:
        bool: True if authentication succeeds, False otherwise.
    """
    clean_user = username.strip().lower()
    if clean_user in users_db:
        return users_db[clean_user]["password"] == password
    return False


def login_flow(users_db: Dict[str, Dict[str, str]], max_attempts: int = 3) -> Optional[str]:
    """
    Executes the login retry loop with maximum attempt limit.

    Args:
        users_db (Dict[str, Dict[str, str]]): Registered users.
        max_attempts (int): Allowed attempts before lockout. Defaults to 3.

    Returns:
        Optional[str]: Username if successfully authenticated, None if locked out / cancelled.
    """
    attempts_left = max_attempts
    print("\n" + "=" * 50)
    print("           PORTAL LOGIN")
    print("=" * 50)

    while attempts_left > 0:
        print(f"Attempts Remaining: {attempts_left}")
        uname = input("Username (or 'cancel' to return): ").strip()
        if uname.lower() == 'cancel':
            print("[-] Login cancelled by user.")
            return None

        pwd = input("Password: ").strip()

        if authenticate_user(users_db, uname, pwd):
            clean_user = uname.lower()
            print(f"\n[+] Login Successful! Welcome back, {users_db[clean_user]['full_name']}.")
            return clean_user
        else:
            attempts_left -= 1
            print(f"\n[!] Invalid username or password.")
            if attempts_left > 0:
                print(f"    Please check your credentials and try again.")
            else:
                print("\n[ALERT] Maximum login attempts exceeded!")
                print("        Account temporarily locked for security. Please contact administrator.")
                return None

    return None


def user_dashboard(users_db: Dict[str, Dict[str, str]], active_username: str) -> None:
    """
    Displays the authenticated user session dashboard with logout capability.

    Args:
        users_db (Dict[str, Dict[str, str]]): Registered users database.
        active_username (str): Currently logged-in username.
    """
    user_info = users_db[active_username]

    while True:
        print("\n" + "=" * 50)
        print(f"  AUTHENTICATED DASHBOARD - {user_info['full_name'].upper()}")
        print("=" * 50)
        print(f"  User ID   : {active_username}")
        print(f"  Role      : {user_info['role']}")
        print("-" * 50)
        print("1. View Profile Information")
        print("2. Change Password")
        print("3. View System Status")
        print("4. Logout")
        print("-" * 50)

        choice = input("Select an action (1-4): ").strip()

        if choice == '1':
            print(f"\n[Profile] Name: {user_info['full_name']} | Role: {user_info['role']} | Account Status: Active")
        elif choice == '2':
            old_p = input("Enter current password: ").strip()
            if old_p != user_info["password"]:
                print("[!] Current password incorrect.")
                continue
            new_p = input("Enter new password: ").strip()
            if len(new_p) < 6:
                print("[!] Password must be at least 6 characters.")
                continue
            user_info["password"] = new_p
            print("[+] Password successfully updated!")
        elif choice == '3':
            print(f"\n[System Status] All services operating nominally. Session secure.")
        elif choice == '4':
            print(f"\n[+] Logged out {user_info['full_name']} successfully. Goodbye!")
            break
        else:
            print("[!] Invalid option. Select 1 to 4.")


def main_auth_system():
    """Main application loop managing user authentication lifecycle."""
    users_db = get_default_users()

    while True:
        print("\n" + "=" * 50)
        print("    SUPER30 MINI AUTHENTICATION SYSTEM")
        print("=" * 50)
        print("1. Login to Account")
        print("2. View Registered Demo Usernames")
        print("3. Exit System")
        print("=" * 50)

        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            logged_in_user = login_flow(users_db, max_attempts=3)
            if logged_in_user:
                user_dashboard(users_db, logged_in_user)
        elif choice == '2':
            print("\nAvailable demo accounts for testing:")
            for uname, details in users_db.items():
                print(f"  * Username: '{uname:<8}' (Role: {details['role']:<10} | Name: {details['full_name']})")
        elif choice == '3':
            print("\nShutting down authentication system. Goodbye!")
            break
        else:
            print("[!] Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main_auth_system()
