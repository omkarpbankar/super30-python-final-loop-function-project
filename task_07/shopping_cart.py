"""
Task 07: Shopping Cart Application
Objective:
    Create a menu-driven shopping cart application allowing users to:
    - Add products (name, unit price, quantity)
    - Remove products (or reduce quantity)
    - View cart contents
    - Calculate bill with subtotal, tax, discounts, and final total
    - Exit
    Application loops continuously until Exit is explicitly selected.
"""

from typing import Dict, Any, Optional


def create_cart() -> Dict[str, Dict[str, Any]]:
    """
    Initializes an empty shopping cart.

    Returns:
        Dict[str, Dict[str, Any]]: Shopping cart dictionary.
    """
    return {}


def add_to_cart(
    cart: Dict[str, Dict[str, Any]],
    product_name: str,
    unit_price: float,
    quantity: int = 1
) -> bool:
    """
    Adds a product to the cart or increments existing item quantity.

    Args:
        cart (Dict[str, Dict[str, Any]]): The user's cart.
        product_name (str): Product name.
        unit_price (float): Price per single unit (> 0).
        quantity (int): Number of items to add (> 0).

    Returns:
        bool: True if added successfully, False otherwise.
    """
    clean_name = product_name.strip()
    if not clean_name:
        print("[!] Error: Product name cannot be empty.")
        return False
    if unit_price <= 0:
        print("[!] Error: Unit price must be greater than 0.")
        return False
    if quantity <= 0:
        print("[!] Error: Quantity must be at least 1.")
        return False

    key = clean_name.lower()
    if key in cart:
        cart[key]["quantity"] += quantity
        cart[key]["unit_price"] = unit_price
        print(f"[+] Updated '{cart[key]['name']}' in cart. New quantity: {cart[key]['quantity']}")
    else:
        cart[key] = {
            "name": clean_name,
            "unit_price": float(unit_price),
            "quantity": int(quantity)
        }
        print(f"[+] Added {quantity}x '{clean_name}' at ${unit_price:.2f} each to your cart.")
    return True


def remove_from_cart(
    cart: Dict[str, Dict[str, Any]],
    product_name: str,
    quantity_to_remove: Optional[int] = None
) -> bool:
    """
    Removes an item or decreases its quantity in the cart.

    Args:
        cart (Dict[str, Dict[str, Any]]): The user's cart.
        product_name (str): Product name to remove.
        quantity_to_remove (Optional[int]): Quantity to deduct. If None or >= current quantity, removes item completely.

    Returns:
        bool: True if removed/reduced, False otherwise.
    """
    key = product_name.strip().lower()
    if key not in cart:
        print(f"[!] Error: '{product_name}' was not found in your cart.")
        return False

    item = cart[key]
    if quantity_to_remove is None or quantity_to_remove >= item["quantity"]:
        del cart[key]
        print(f"[-] Completely removed '{item['name']}' from cart.")
    else:
        if quantity_to_remove <= 0:
            print("[!] Error: Quantity to remove must be > 0.")
            return False
        item["quantity"] -= quantity_to_remove
        print(f"[-] Reduced '{item['name']}' by {quantity_to_remove}. Remaining: {item['quantity']}")
    return True


def view_cart(cart: Dict[str, Dict[str, Any]]) -> None:
    """
    Renders an itemized list of all items currently in the cart.

    Args:
        cart (Dict[str, Dict[str, Any]]): The user's cart.
    """
    print("\n" + "=" * 65)
    print(f"{'YOUR SHOPPING CART':^65}")
    print("=" * 65)

    if not cart:
        print("  Your cart is empty.")
        print("=" * 65 + "\n")
        return

    print(f"{'#':<4} {'Item Name':<28} {'Unit Price':<12} {'Qty':<6} {'Total ($)':<12}")
    print("-" * 65)
    subtotal = 0.0
    for idx, item in enumerate(cart.values(), start=1):
        item_total = item["unit_price"] * item["quantity"]
        subtotal += item_total
        print(f"{idx:<4} {item['name']:<28} ${item['unit_price']:>9.2f}  {item['quantity']:>4}  ${item_total:>10.2f}")

    print("-" * 65)
    print(f"{'Estimated Cart Subtotal:':<52} ${subtotal:>10.2f}")
    print("=" * 65 + "\n")


def calculate_bill(
    cart: Dict[str, Dict[str, Any]],
    tax_rate: float = 0.08,
    discount_rate: float = 0.10,
    discount_threshold: float = 100.0
) -> Dict[str, float]:
    """
    Calculates subtotal, discount, sales tax, and final grand total.

    Args:
        cart (Dict[str, Dict[str, Any]]): The user's cart.
        tax_rate (float): Sales tax rate (default 8%).
        discount_rate (float): Discount rate applied if subtotal exceeds threshold (default 10%).
        discount_threshold (float): Minimum subtotal required for discount.

    Returns:
        Dict[str, float]: Detailed bill breakdown.
    """
    subtotal = 0.0
    for item in cart.values():
        subtotal += item["unit_price"] * item["quantity"]

    discount_amount = (subtotal * discount_rate) if subtotal >= discount_threshold else 0.0
    discounted_subtotal = subtotal - discount_amount
    tax_amount = discounted_subtotal * tax_rate
    grand_total = discounted_subtotal + tax_amount

    print("\n" + "=" * 65)
    print(f"{'FINAL CHECKOUT INVOICE':^65}")
    print("=" * 65)

    if not cart:
        print("  Cannot generate bill: Cart is empty.")
        print("=" * 65 + "\n")
        return {"subtotal": 0.0, "discount": 0.0, "tax": 0.0, "grand_total": 0.0}

    print(f"{'Item Name':<30} {'Qty':<6} {'Unit Price':<12} {'Line Total':<12}")
    print("-" * 65)
    for item in cart.values():
        line_total = item["unit_price"] * item["quantity"]
        print(f"{item['name']:<30} {item['quantity']:<6} ${item['unit_price']:>10.2f} ${line_total:>10.2f}")

    print("-" * 65)
    print(f"{'Cart Subtotal:':<50} ${subtotal:>12.2f}")
    if discount_amount > 0:
        print(f"{f'Discount ({int(discount_rate*100)}% off over ${discount_threshold}):':<50} -${discount_amount:>11.2f}")
    else:
        print(f"{'Discount:':<50} ${0.00:>12.2f}")
    print(f"{f'Sales Tax ({tax_rate*100:.1f}%):':<50} +${tax_amount:>11.2f}")
    print("=" * 65)
    print(f"{'GRAND TOTAL DUE:':<50} ${grand_total:>12.2f}")
    print("=" * 65 + "\n")

    return {
        "subtotal": round(subtotal, 2),
        "discount": round(discount_amount, 2),
        "tax": round(tax_amount, 2),
        "grand_total": round(grand_total, 2)
    }


def cart_menu(cart: Dict[str, Dict[str, Any]]) -> None:
    """Main interactive menu loop for shopping cart."""
    while True:
        print("\n" + "-" * 40)
        print("     SUPER30 SHOPPING CART")
        print("-" * 40)
        print("1. Add Product to Cart")
        print("2. Remove / Reduce Product")
        print("3. View Cart")
        print("4. Calculate Bill & Checkout")
        print("5. Exit")
        print("-" * 40)

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            name = input("Enter product name: ").strip()
            try:
                price = float(input("Enter unit price ($): ").strip())
                qty_in = input("Enter quantity (default: 1): ").strip()
                qty = int(qty_in) if qty_in else 1
                add_to_cart(cart, name, price, qty)
            except ValueError:
                print("[!] Invalid numerical input.")

        elif choice == '2':
            if not cart:
                print("[!] Cart is already empty.")
                continue
            name = input("Enter product name to remove: ").strip()
            qty_in = input("Enter quantity to remove (leave blank to remove all): ").strip()
            try:
                qty_to_rem = int(qty_in) if qty_in else None
                remove_from_cart(cart, name, qty_to_rem)
            except ValueError:
                print("[!] Invalid integer for quantity.")

        elif choice == '3':
            view_cart(cart)

        elif choice == '4':
            calculate_bill(cart)

        elif choice == '5':
            print("\nThank you for visiting Super30 Store. Have a wonderful day!")
            break
        else:
            print("[!] Invalid option. Please enter 1-5.")


def main():
    """Initializes cart and runs shopping session."""
    user_cart = create_cart()
    # Preload a couple items for demonstration
    add_to_cart(user_cart, "Python Programming Guide", 39.99, 1)
    add_to_cart(user_cart, "Noise Cancelling Headphones", 79.50, 2)
    cart_menu(user_cart)


if __name__ == "__main__":
    main()
