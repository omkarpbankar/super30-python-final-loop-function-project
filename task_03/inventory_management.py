"""
Task 03: Inventory Management System
Objective:
    Maintain a store product inventory with attributes:
    - Product Name
    - Price ($)
    - Quantity (units in stock)

    Functions provided:
    - add_product: Register a new product or update existing
    - display_products: Show tabular list of inventory
    - search_product: Case-insensitive search for product details
    - update_quantity: Update stock level for a product
    - calculate_total_inventory_value: Calculate cumulative valuation (price * quantity)
"""

from typing import Dict, List, Optional, Any


def create_inventory() -> Dict[str, Dict[str, Any]]:
    """
    Initializes an empty or seeded product inventory.

    Returns:
        Dict[str, Dict[str, Any]]: Inventory mapping product_name (lowercase key) to product dict.
    """
    return {}


def add_product(
    inventory: Dict[str, Dict[str, Any]],
    name: str,
    price: float,
    quantity: int
) -> bool:
    """
    Adds a new product to inventory or updates stock if already present.

    Args:
        inventory (Dict[str, Dict[str, Any]]): The inventory storage.
        name (str): Product name.
        price (float): Price per unit (must be >= 0).
        quantity (int): Units in stock (must be >= 0).

    Returns:
        bool: True if successfully added/updated, False otherwise.
    """
    clean_name = name.strip()
    if not clean_name:
        print("[!] Error: Product name cannot be blank.")
        return False
    if price < 0:
        print("[!] Error: Price cannot be negative.")
        return False
    if quantity < 0:
        print("[!] Error: Quantity cannot be negative.")
        return False

    key = clean_name.lower()
    if key in inventory:
        inventory[key]["price"] = price
        inventory[key]["quantity"] += quantity
        print(f"[+] Existing product '{inventory[key]['name']}' updated. New total quantity: {inventory[key]['quantity']}")
    else:
        inventory[key] = {
            "name": clean_name,
            "price": float(price),
            "quantity": int(quantity)
        }
        print(f"[+] Product '{clean_name}' successfully added to inventory.")
    return True


def display_products(inventory: Dict[str, Dict[str, Any]]) -> None:
    """
    Displays all inventory items in a clean tabular format.

    Args:
        inventory (Dict[str, Dict[str, Any]]): The inventory dictionary.
    """
    print("\n" + "=" * 65)
    print(f"{'CURRENT INVENTORY STOCK':^65}")
    print("=" * 65)
    if not inventory:
        print("  Inventory is currently empty.")
        print("=" * 65 + "\n")
        return

    print(f"{'#':<4} {'Product Name':<28} {'Price ($)':<12} {'Qty':<8} {'Total Value ($)':<12}")
    print("-" * 65)
    idx = 1
    total_val = 0.0
    for key, item in inventory.items():
        subtotal = item["price"] * item["quantity"]
        total_val += subtotal
        print(f"{idx:<4} {item['name']:<28} ${item['price']:>8.2f}  {item['quantity']:>5}  ${subtotal:>12.2f}")
        idx += 1
    print("-" * 65)
    print(f"{'TOTAL INVENTORY VALUATION:':<51} ${total_val:>12.2f}")
    print("=" * 65 + "\n")


def search_product(
    inventory: Dict[str, Dict[str, Any]],
    search_term: str
) -> Optional[Dict[str, Any]]:
    """
    Searches for a product by name (exact or substring match, case-insensitive).

    Args:
        inventory (Dict[str, Dict[str, Any]]): The inventory dictionary.
        search_term (str): Name or keyword to search.

    Returns:
        Optional[Dict[str, Any]]: Found product dict, or None if not found.
    """
    term = search_term.strip().lower()
    if not term:
        print("[!] Search term cannot be empty.")
        return None

    matches: List[Dict[str, Any]] = []
    for key, product in inventory.items():
        if term in key:
            matches.append(product)

    if not matches:
        print(f"\n[?] No products found matching '{search_term}'.")
        return None

    print(f"\nFound {len(matches)} matching product(s):")
    for prod in matches:
        val = prod["price"] * prod["quantity"]
        print(f"  * Name: {prod['name']} | Price: ${prod['price']:.2f} | Quantity: {prod['quantity']} | Value: ${val:.2f}")
    return matches[0] if len(matches) == 1 else matches[0]


def update_quantity(
    inventory: Dict[str, Dict[str, Any]],
    product_name: str,
    new_quantity: int
) -> bool:
    """
    Updates the stock quantity of a specific product.

    Args:
        inventory (Dict[str, Dict[str, Any]]): The inventory dictionary.
        product_name (str): Product name.
        new_quantity (int): New quantity count (>= 0).

    Returns:
        bool: True if updated successfully, False otherwise.
    """
    key = product_name.strip().lower()
    if key not in inventory:
        print(f"[!] Error: Product '{product_name}' not found in inventory.")
        return False
    if new_quantity < 0:
        print("[!] Error: Quantity cannot be negative.")
        return False

    old_qty = inventory[key]["quantity"]
    inventory[key]["quantity"] = int(new_quantity)
    print(f"[+] Stock updated for '{inventory[key]['name']}': {old_qty} -> {new_quantity} units.")
    return True


def calculate_total_inventory_value(inventory: Dict[str, Dict[str, Any]]) -> float:
    """
    Calculates the total monetary value of all goods in inventory using a loop.

    Args:
        inventory (Dict[str, Dict[str, Any]]): The inventory dictionary.

    Returns:
        float: Total value (sum of price * quantity for all items).
    """
    total_value = 0.0
    for item in inventory.values():
        total_value += item["price"] * item["quantity"]
    return round(total_value, 2)


def inventory_menu(inventory: Dict[str, Dict[str, Any]]) -> None:
    """Interactive loop menu for inventory management."""
    while True:
        print("\n" + "=" * 45)
        print("   INVENTORY MANAGEMENT SYSTEM MENU")
        print("=" * 45)
        print("1. Add / Restock Product")
        print("2. Display All Products")
        print("3. Search Product")
        print("4. Update Product Stock Quantity")
        print("5. Calculate Total Inventory Value")
        print("6. Exit")
        print("=" * 45)

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            name = input("Enter product name: ").strip()
            if not name:
                print("[!] Name cannot be empty.")
                continue
            try:
                price = float(input("Enter unit price ($): ").strip())
                qty = int(input("Enter quantity: ").strip())
                add_product(inventory, name, price, qty)
            except ValueError:
                print("[!] Invalid numerical input for price or quantity.")

        elif choice == '2':
            display_products(inventory)

        elif choice == '3':
            term = input("Enter product name to search: ").strip()
            search_product(inventory, term)

        elif choice == '4':
            name = input("Enter product name: ").strip()
            try:
                new_qty = int(input("Enter new total quantity: ").strip())
                update_quantity(inventory, name, new_qty)
            except ValueError:
                print("[!] Invalid integer for quantity.")

        elif choice == '5':
            val = calculate_total_inventory_value(inventory)
            print(f"\n[i] Total Inventory Value: ${val:,.2f}")

        elif choice == '6':
            print("\nExiting Inventory Management System. Have a great day!")
            break
        else:
            print("[!] Invalid choice. Please enter a number between 1 and 6.")


def main():
    """Initializes inventory with sample stock and launches menu."""
    sample_inventory = create_inventory()
    # Add initial seed data
    add_product(sample_inventory, "Laptop Dell XPS 15", 1499.99, 8)
    add_product(sample_inventory, "Wireless Mouse", 29.99, 45)
    add_product(sample_inventory, "Mechanical Keyboard", 89.50, 20)
    add_product(sample_inventory, "USB-C Hub", 35.00, 30)

    print("\nStarting Super30 Inventory Manager...")
    inventory_menu(sample_inventory)


if __name__ == "__main__":
    main()
